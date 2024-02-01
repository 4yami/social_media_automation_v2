import json
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory, QTableWidgetItem, QCheckBox, QMessageBox
from PySide6.QtCore import Qt

from main_ui import Ui_MainWindow


DATA_JSON_PATH = "data.json"
HOME_COLUMN_WIDTHS = [40, 197]
ACCOUNT_COLUMN_WIDTHS = [40, 200, 450]


class LinkManager:
    @staticmethod
    def read_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            return {}

    @staticmethod
    def add_data_to_json(file_path, new_data):
        data = LinkManager.read_json(file_path)
        data.update(new_data)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def save_json(file_path, data):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
            
            
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.link_manager = LinkManager()
        self.account_checkboxes = {}
        self.setup_ui()
        self.connect_signals()
        
    def setup_ui(self):
        self.ui.setupUi(self)
        QApplication.setStyle(QStyleFactory.create("fusion"))
        self.ui.page_widget.setCurrentIndex(0)
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
        self.ui.home_btn.clicked.connect(self.show_home_page)
        self.ui.account_btn.clicked.connect(self.show_account_page)
        self.ui.add_link_btn.clicked.connect(self.add_link)
        for radio_button in self.ui.radio_buttons_dict:
            radio_button.toggled.connect(self.get_radio_btn)
        self.ui.remove_link_btn.clicked.connect(self.remove_link)
        self.ui.edit_link_btn.clicked.connect(self.edit_link)

    # home_page function
    def populate_home_table(self):
        self.ui.home_table.clearContents()
        self.ui.home_table.setRowCount(0)
        self.home_header_label = ['', 'Name']
        self.ui.home_table.setColumnCount(len(self.home_header_label))
        self.ui.home_table.setHorizontalHeaderLabels(self.home_header_label)
        self.read_json(DATA_JSON_PATH)
        for row_index, (key_name, data) in enumerate(self.data.items()):
            self.ui.home_table.insertRow(row_index)
            for index2, (header, cell_data) in enumerate(data.items()):
                if header == "checkbox":
                    checkbox = QCheckBox()
                    checkbox.setChecked(int(cell_data) == 1)
                    self.ui.home_table.setCellWidget(row_index, 0, checkbox)
                    checkbox_identifier = f"{key_name}"
                    self.account_checkboxes[checkbox_identifier] = checkbox
                    self.account_checkboxes[checkbox_identifier].stateChanged.connect(lambda state, name=key_name: self.checkbox_changed(state, name))
                elif header == 'link_name':
                    item = QTableWidgetItem(str(cell_data))
                    self.ui.home_table.setItem(row_index, 1, item)
        
    # account_page function
    def get_radio_btn(self):
        selected_option = "No option selected"
        for radio_button, text in self.ui.radio_buttons_dict.items():
            if radio_button.isChecked():
                selected_option = text
        return selected_option

    def add_link(self):
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
        if radio_btn == "No option selected":
            return QMessageBox.warning(self, "Input Error", "No social media selected")
        if not link_name or not link:
            return QMessageBox.warning(self, "Input Error", "Link name and link cannot be empty.")
        self.link_manager.add_data_to_json(DATA_JSON_PATH, new_data)
        self.populate_account_table()

    def read_json(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.data = json.load(file)
            return self.data
        else:
            with open(file_path, 'w') as file:
                json.dump({}, file)
            return {}  
    
    def checkbox_changed(self, state, data_name):
        data = self.link_manager.read_json(DATA_JSON_PATH)
        data[data_name]["checkbox"] = int(state == Qt.Checked)
        self.link_manager.save_json(DATA_JSON_PATH, data)
        self.populate_account_table()

    def populate_account_table(self):
        self.ui.account_table.clearContents()
        self.ui.account_table.setRowCount(0)
        self.account_header_labels = ["", "Name", "Link", "Social Media"]
        self.ui.account_table.setColumnCount(len(self.account_header_labels))
        self.ui.account_table.setHorizontalHeaderLabels(self.account_header_labels)
        keys_order = ["checkbox", "link_name", "link", "radio_btn"]
        self.read_json(DATA_JSON_PATH)
        for row_index, (row_name, row_data) in enumerate(self.data.items()):
            self.ui.account_table.insertRow(row_index)
            for col_index, header_label in enumerate(keys_order):
                cell_data = row_data.get(header_label)
                if header_label == "checkbox":
                    checkbox = QCheckBox()
                    checkbox.setChecked(int(cell_data) == 1)
                    self.ui.account_table.setCellWidget(row_index, col_index, checkbox)
                    
                    # Store the checkbox in the dictionary with a unique identifier
                    checkbox_identifier = f"{row_name}"
                    self.account_checkboxes[checkbox_identifier] = checkbox
                    self.account_checkboxes[checkbox_identifier].stateChanged.connect(lambda state, name=row_name: self.checkbox_changed(state, name))
                else:
                    item = QTableWidgetItem(str(cell_data))
                    self.ui.account_table.setItem(row_index, col_index, item)
                    
    def remove_link(self):
        row_index = self.ui.account_table.currentRow()
        link_name = self.ui.account_table.item(row_index, 1).text()
        data = self.link_manager.read_json(DATA_JSON_PATH)

        if link_name in data:
            del data[link_name]
            self.link_manager.save_json(DATA_JSON_PATH, data)
            if row_index >= 0:
                self.ui.account_table.removeRow(row_index)
            else:
                print("No row selected.")
        else:
            print(f"Can't find {link_name}\n", data)

    def edit_link(self):
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
        self.populate_home_table()
        self.ui.page_widget.setCurrentIndex(0)

    def show_account_page(self):
        self.populate_account_table()
        self.ui.page_widget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
