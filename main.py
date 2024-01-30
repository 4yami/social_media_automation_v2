import json
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory, QTableWidgetItem, QCheckBox, QMessageBox

from main_ui import Ui_MainWindow

DATA_JSON_PATH = "data.json"
COLUMN_WIDTHS = [40, 200, 450]

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        self.ui.setupUi(self)
        QApplication.setStyle(QStyleFactory.create("fusion"))
        self.ui.page_widget.setCurrentIndex(1)
        self.ui.radio_buttons_dict = {
            self.ui.facebook_group_rbtn: 'Facebook Group',
            self.ui.rbtn2: "rbtn2",
        }
        self.populate_table(self.read_json(DATA_JSON_PATH))
        for i, width in enumerate(COLUMN_WIDTHS):
            self.ui.account_table.horizontalHeader().resizeSection(i, width)

    def connect_signals(self):
        self.ui.home_btn.clicked.connect(self.show_home_page)
        self.ui.account_btn.clicked.connect(self.show_account_page)
        self.ui.add_link_btn.clicked.connect(self.add_link)
        for radio_button in self.ui.radio_buttons_dict:
            radio_button.toggled.connect(self.get_radio_btn)

    def show_home_page(self):
        self.ui.page_widget.setCurrentIndex(0)

    def show_account_page(self):
        self.ui.page_widget.setCurrentIndex(1)

    def get_radio_btn(self):
        selected_option = "No option selected"
        for radio_button, text in self.ui.radio_buttons_dict.items():
            if radio_button.isChecked():
                selected_option = text
        return selected_option

    def add_link(self):
        check_box = "1"
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
        # messagebox warning
        if radio_btn == "No option selected":
            return QMessageBox.warning(self, "Input Error", "No social media selected")
        if not link_name or not link:
            return QMessageBox.warning(self, "Input Error", "Link name and link cannot be empty.")
        self.add_data_to_json(DATA_JSON_PATH, new_data)
        self.populate_table(self.read_json(DATA_JSON_PATH))
        self.ui.link_name_input.clear()
        self.ui.link_input.clear()

    def read_json(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        else:
            with open(file_path, 'w') as file:
                json.dump({}, file)
            return {}

    def write_json(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def add_data_to_json(self, file_path, new_data):
        data = self.read_json(file_path)
        data.update(new_data)
        self.write_json(file_path, data)
        print(f"Data added to {file_path}")

    def populate_table(self, json_data):
        self.ui.account_table.clearContents()
        self.ui.account_table.setRowCount(0)
        header_labels = ["Select", "Name", "Link", "Social Media"]
        self.ui.account_table.setColumnCount(len(header_labels))
        self.ui.account_table.setHorizontalHeaderLabels(header_labels)

        for row_index, (row_name, row_data) in enumerate(json_data.items()):
            self.ui.account_table.insertRow(row_index)

            keys_order = ["checkbox", "link_name", "link", "radio_btn"]
            for col_index, header_label in enumerate(keys_order):
                cell_data = row_data.get(header_label, "")

                if header_label == "checkbox":
                    checkbox = QCheckBox()
                    checkbox.setChecked(int(cell_data) == 1)
                    self.ui.account_table.setCellWidget(row_index, col_index, checkbox)
                else:
                    item = QTableWidgetItem(str(cell_data))
                    self.ui.account_table.setItem(row_index, col_index, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
