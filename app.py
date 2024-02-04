# auto-py-to-exe
import json
import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from threading import Thread
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QStyleFactory,
    QTableWidgetItem, QCheckBox, QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt, QFile, QTextStream
from PySide6.QtGui import QPixmap, QIcon

from main_ui import Ui_MainWindow
from post_automation import PostAutomation

APPDATA_PATH = os.path.join(os.getenv('APPDATA'), 'Social_Media_Automation')
DATA_JSON_PATH = os.path.join(APPDATA_PATH, "data.json")
APP_LOG_PATH = os.path.join(APPDATA_PATH, 'app.log')

HOME_COLUMN_WIDTHS = [40, 197]
ACCOUNT_COLUMN_WIDTHS = [40, 200, 450]

NO_SOCIAL_MEDIA_SELECTED = "No option selected"
CHECKBOX = "checkbox"
LINK_NAME = "link_name"
LINK = 'link'

CHECKBOX_COLUMN_INDEX = 0
NAME_COLUMN_INDEX = 1
LINK_COLUMN_INDEX = 2
SOCIAL_MEDIA_COLUMN_INDEX = 3

class LinkManager:
    """Manage reading and writing JSON data."""
    
    @staticmethod
    def read_json(file_path):
        """Read JSON data from a file and return it."""
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    return json.load(file)
            else:
                return {}
        except Exception as e:
            logging.error(f"Error reading JSON file: {e}")
            return {}

    @staticmethod
    def add_data_to_json(file_path, new_data):
        try:
            data = LinkManager.read_json(file_path)
            data.update(new_data)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
        except Exception as e:
            logging.error(f"Error adding data to JSON file: {e}")

    @staticmethod
    def save_json(file_path, data):
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=2)
        except Exception as e:
            logging.error(f"Error saving JSON data to file: {e}")


class MainWindow(QMainWindow):
    """Main application window."""
    def __init__(self):
        """Initialize the main window."""
        super(MainWindow, self).__init__()
        self.create_dir_jsonlog()
        self.ui = Ui_MainWindow()
        self.link_manager = LinkManager()
        self.post_automation = PostAutomation()
        self.account_checkboxes = {}
        self.selected_files_list = []
        self.current_images_index = 0
        self.style()
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        """Set up the user interface."""
        self.ui.setupUi(self)
        
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(sys.argv[0]), 'images\\auto.png')))
        QApplication.setStyle(QStyleFactory.create("fusion"))
        self.show_home_page()
        self.ui.radio_buttons_dict = {
            self.ui.facebook_group_rbtn: 'Facebook Group',
            self.ui.rbtn2: "rbtn2",
        }
        self.populate_home_table()
        for i, width in enumerate(HOME_COLUMN_WIDTHS):
            self.ui.home_table.horizontalHeader().resizeSection(i, width)
        self.populate_account_table()
        for i, width in enumerate(ACCOUNT_COLUMN_WIDTHS):
            self.ui.account_table.horizontalHeader().resizeSection(i, width)

    def connect_signals(self):
        # Connect signals to their respective slots
        try:
            # for all
            self.ui.home_btn.clicked.connect(self.show_home_page)
            self.ui.account_btn.clicked.connect(self.show_account_page)
            
            # for home
            self.ui.add_btn.clicked.connect(self.add)
            self.ui.previous_btn.clicked.connect(self.previous)
            self.ui.next_btn.clicked.connect(self.next)
            self.ui.remove_btn.clicked.connect(self.remove)
            self.ui.post_btn.clicked.connect(self.post)
            
            # for account
            self.ui.add_link_btn.clicked.connect(self.add_link)
            for radio_button in self.ui.radio_buttons_dict:
                radio_button.toggled.connect(self.get_radio_btn)
            self.ui.remove_link_btn.clicked.connect(self.remove_link)
            self.ui.edit_link_btn.clicked.connect(self.edit_link)
            
        except Exception as e:
            logging.error(f"Error connecting signals: {e}")
    
    def style(self):
        style_file = QFile("style\\style.qss")
        style_file.open(QFile.ReadOnly | QFile.Text)
        style_stream = QTextStream(style_file)
        app.setStyleSheet(style_stream.readAll())

    # background function
    def create_dir_jsonlog(self):
        try:
            if not os.path.exists(APPDATA_PATH):
                os.makedirs(APPDATA_PATH)
            # Configure logging with TimedRotatingFileHandler
            log_handler = TimedRotatingFileHandler(APP_LOG_PATH, when="midnight", interval=1, backupCount=7)
            log_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s'))
            logging.getLogger().addHandler(log_handler)
            logging.getLogger().setLevel(logging.INFO)  # Adjust the log level as needed
        except Exception as e:
            logging.error(f"Error creating directories: {e}")
    
    def get_radio_btn(self):
        # Get the selected radio button's text
        selected_option = NO_SOCIAL_MEDIA_SELECTED
        for radio_button, text in self.ui.radio_buttons_dict.items():
            if radio_button.isChecked():
                selected_option = text
        return selected_option

    def unchecked_radio_btn(self):
        for radio_button, text in self.ui.radio_buttons_dict.items():
            radio_button.setAutoExclusive(False)
            radio_button.setChecked(False)
            radio_button.setAutoExclusive(False)

    def checkbox_changed(self, state, data_name):
        # Update the checkbox state in the JSON data and refresh the account table
        data = self.link_manager.read_json(DATA_JSON_PATH)
        data[data_name][CHECKBOX] = int(state == 2)
        self.link_manager.save_json(DATA_JSON_PATH, data)
        self.populate_account_table()

    def resizeEvent(self, event):
        """Handle the window resize event."""
        super(MainWindow, self).resizeEvent(event)
        self.image_label()

    
    # home page ui function
    def image_label(self):
        if self.selected_files_list:
            pixmap = QPixmap(self.selected_files_list[self.current_images_index]).scaled(
            self.ui.image_label.size(),
            aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
            mode=Qt.TransformationMode.SmoothTransformation
        )
            self.ui.image_label.setPixmap(pixmap)
            self.image_nav_label()
            
    def image_nav_label(self):
        self.ui.image_nav_label.setText(f"Image {self.current_images_index + 1}/{len(self.selected_files_list)}")
    
    def add(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        if file_dialog.exec() == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            self.selected_files_list.extend(selected_files)
            self.image_label()
    
    def previous(self):
        """Show the next image in the list."""
        self.current_images_index = (self.current_images_index - 1) % len(self.selected_files_list)
        self.image_label()
    
    def next(self):
        """Show the next image in the list."""
        self.current_images_index = (self.current_images_index + 1) % len(self.selected_files_list)
        self.image_label()
    
    def remove(self):
        """Remove the currently displayed image."""
        if self.selected_files_list:
            self.selected_files_list.pop(self.current_images_index)
            if not self.selected_files_list:
                self.reset_viewer_state()
            else:
                self.current_images_index = min(self.current_images_index, len(self.selected_files_list) - 1)
            self.image_label()
    
    def reset_viewer_state(self):
        """Reset the state of the image viewer."""
        self.current_images_index = 0
        self.ui.image_label.clear()
        self.ui.image_nav_label.clear()
    
    def populate_home_table(self):
            # Populate the home table with data from the JSON file
            self.ui.home_table.clearContents()
            self.ui.home_table.setRowCount(0)
            self.home_header_label = ['', 'Name']
            self.ui.home_table.setColumnCount(len(self.home_header_label))
            self.ui.home_table.setHorizontalHeaderLabels(self.home_header_label)
            data = self.link_manager.read_json(DATA_JSON_PATH)
            for home_row_index, (key_name, data1) in enumerate(data.items()):
                self.ui.home_table.insertRow(home_row_index)
                for index2, (header, cell_data) in enumerate(data1.items()):
                    if header == CHECKBOX:
                        # Create a checkbox for the checkbox column
                        checkbox = QCheckBox()
                        checkbox.setChecked(int(cell_data) == 1)
                        self.ui.home_table.setCellWidget(home_row_index, CHECKBOX_COLUMN_INDEX, checkbox)
                        checkbox_identifier = f"{key_name}"
                        self.account_checkboxes[checkbox_identifier] = checkbox
                        self.account_checkboxes[checkbox_identifier].stateChanged.connect(
                            lambda state, name=key_name: self.checkbox_changed(state, name)
                        )
                    elif header == LINK_NAME:
                        # Populate other columns with data
                        home_table_item = QTableWidgetItem(str(cell_data))
                        self.ui.home_table.setItem(home_row_index, NAME_COLUMN_INDEX, home_table_item)

    def post(self):
        try:
            text = self.ui.post_text_input.toPlainText()
            data = self.link_manager.read_json(DATA_JSON_PATH)
            def post_thread():
                try:
                    for index, (key_name, object) in enumerate(data.items()):
                        if object[CHECKBOX] == 1:
                            url = object[LINK]
                            self.post_automation.post_fb_group(url, text, self.selected_files_list)
                except Exception as e:
                    logging.error(f"Error in the background thread: {e}")
            post_thread_instance = Thread(target=post_thread)
            post_thread_instance.start()
            post_thread_instance.join()
        except Exception as e:
            logging.error(f"Error in the post method: {e}")


    # account page ui function
    def add_link(self):
        # Add a new link with data from the input fields
        check_box = 1
        link_name = self.ui.link_name_input.text()
        link = self.ui.link_input.text()
        radio_btn = self.get_radio_btn()
        new_data = {
            link_name: {
                "link_name": link_name,
                "checkbox": check_box,
                "link": link,
                "radio_btn": radio_btn,
            },
        }
        if radio_btn == NO_SOCIAL_MEDIA_SELECTED:
            QMessageBox.warning(self, "Input Error", "No social media selected")
            return
        if not link_name or not link:
            QMessageBox.warning(self, "Input Error", "Link name and link cannot be empty.")
            return
        self.link_manager.add_data_to_json(DATA_JSON_PATH, new_data)
        self.populate_account_table()
        self.ui.link_name_input.clear()
        self.ui.link_input.clear()
        self.unchecked_radio_btn()    

    def populate_account_table(self):
        # Populate the account table with data from the JSON file
        self.ui.account_table.clearContents()
        self.ui.account_table.setRowCount(0)
        self.account_header_labels = ["", "Name", "Link", "Social Media"]
        self.ui.account_table.setColumnCount(len(self.account_header_labels))
        self.ui.account_table.setHorizontalHeaderLabels(self.account_header_labels)
        keys_order = ["checkbox", "link_name", "link", "radio_btn"]
        data = self.link_manager.read_json(DATA_JSON_PATH)
        for row_index_account_table, (row_name, row_data) in enumerate(data.items()):
            self.ui.account_table.insertRow(row_index_account_table)
            for col_index_account, header_label in enumerate(keys_order):
                cell_data = row_data.get(header_label)
                if header_label == CHECKBOX:
                    # Create a checkbox for the checkbox column
                    checkbox = QCheckBox()
                    checkbox.setChecked(int(cell_data) == 1)
                    self.ui.account_table.setCellWidget(row_index_account_table, col_index_account, checkbox)

                    # Store the checkbox in the dictionary with a unique identifier
                    checkbox_identifier = f"{row_name}"
                    self.account_checkboxes[checkbox_identifier] = checkbox
                    self.account_checkboxes[checkbox_identifier].stateChanged.connect(
                        lambda state, name=row_name: self.checkbox_changed(state, name)
                    )
                else:
                    # Populate other columns with data
                    account_table_item = QTableWidgetItem(str(cell_data))
                    self.ui.account_table.setItem(row_index_account_table, col_index_account, account_table_item)

    def remove_link(self):
        # Remove the selected link and update the account table
        row_index = self.ui.account_table.currentRow()
        link_name = self.ui.account_table.item(row_index, NAME_COLUMN_INDEX).text()
        data = self.link_manager.read_json(DATA_JSON_PATH)

        if link_name in data:
            del data[link_name]
            self.link_manager.save_json(DATA_JSON_PATH, data)
            if row_index >= 0:
                self.ui.account_table.removeRow(row_index)
            else:
                QMessageBox.warning(self, "Error", "No row selected.")
        else:
            QMessageBox.warning(self, "Error", f"Can't find {link_name}\n{data}")

    def edit_link(self):
        # Edit the selected link and update the input fields
        row_index = self.ui.account_table.currentRow()
        for col_index, header in enumerate(self.account_header_labels):
            if header == "Name":
                item = self.ui.account_table.item(row_index, col_index).text()
                self.ui.link_name_input.setText(item)
            if header == "Link":
                item = self.ui.account_table.item(row_index, col_index).text()
                self.ui.link_input.setText(item)
            if header == "Social Media":
                item = self.ui.account_table.item(row_index, col_index).text()
                for radio_button, text in self.ui.radio_buttons_dict.items():
                    if text == item:
                        radio_button.setChecked(True)
        self.remove_link()


    # show page
    def show_home_page(self):
        # Switch to the home page and refresh the home table
        self.populate_home_table()
        self.ui.page_widget.setCurrentIndex(0)
        self.ui.home_btn.setChecked(True)

    def show_account_page(self):
        # Switch to the account page and refresh the account table
        self.populate_account_table()
        self.ui.page_widget.setCurrentIndex(1)
        self.ui.account_btn.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Social Media Automation")
    window.showMaximized()
    sys.exit(app.exec())
