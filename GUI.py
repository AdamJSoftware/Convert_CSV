from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import sys
import os
from tkinter import filedialog
import tkinter
import Engine
import csv

class CreateConfig(QDialog):
    def __init__(self, parent=None):
        super(CreateConfig, self).__init__(parent)

        self.columns_to_remove_label = QLabel("Columns To Remove")
        self.columns_to_rename_label = QLabel("Columns To Rename")
        self.columns_to_add_label = QLabel("Columns To Add")
        self.columns_to_reorganize_label = QLabel("Columns To Reorganize")
        self.crop_label = QLabel("Crop")
        self.rows_to_remove_label = QLabel("Rows to remove")
        self.rows_to_switch_label = QLabel("Rows to witch")

        self.columns_to_remove_add_row = QPushButton("Add row")
        self.columns_to_remove_add_column = QPushButton("Add column")
        self.columns_to_add_add_row = QPushButton("Add row")
        self.columns_to_add_add_column = QPushButton("Add column")
        self.columns_to_rename_add_row = QPushButton("Add row")
        self.columns_to_rename_add_column = QPushButton("Add column")
        self.columns_to_reorganize_add_row = QPushButton("Add row")
        self.columns_to_reorganize_add_column = QPushButton("Add column")
        self.rows_to_remove_add_row = QPushButton("Add row")
        self.crop_add_row = QPushButton("Add row")
        self.crop_add_column = QPushButton("Add column")
        self.live_view = QPushButton("Live View")
        self.save = QPushButton("Save")
        self.help = QPushButton("Help")
        self.load = QPushButton("Load Configuration")
        self.rows_to_remove_add_column = QPushButton("Add column")
        self.rows_to_switch_add_column = QPushButton("Add column")
        self.rows_to_switch_add_row = QPushButton("Add row")

        self.crop_table = QTableWidget()
        self.crop_table.setRowCount(2)
        self.crop_table.setColumnCount(1)
        header = self.crop_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.columns_to_remove_table = QTableWidget()
        self.columns_to_remove_table.setRowCount(2)
        self.columns_to_remove_table.setColumnCount(1)
        header = self.columns_to_remove_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        #
        self.columns_to_add_table = QTableWidget()
        self.columns_to_add_table.setRowCount(2)
        self.columns_to_add_table.setColumnCount(1)
        header = self.columns_to_add_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.columns_to_rename_table = QTableWidget()
        self.columns_to_rename_table.setRowCount(2)
        self.columns_to_rename_table.setColumnCount(1)
        header = self.columns_to_rename_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.columns_to_reorganize_table = QTableWidget()
        self.columns_to_reorganize_table.setRowCount(2)
        self.columns_to_reorganize_table.setColumnCount(1)
        header = self.columns_to_reorganize_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.rows_to_remove_table = QTableWidget()
        self.rows_to_remove_table.setRowCount(2)
        self.rows_to_remove_table.setColumnCount(1)
        header = self.rows_to_remove_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.rows_to_switch_table = QTableWidget()
        self.rows_to_switch_table.setRowCount(2)
        self.rows_to_switch_table.setColumnCount(1)
        header = self.rows_to_switch_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # new_array = [self.columns_to_remove_table, self.columns_to_add_table]
        # for i in new_array:
        #     print(i)
        #     i = QTableWidget()
        #     i.setRowCount(2)
        #     i.setColumnCount(1)
        #     header = i.horizontalHeader()
        #     header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #     header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


        self.columns_to_remove_add_row.clicked.connect(lambda: self.handle_remove_add_row_button())
        self.columns_to_remove_add_column.clicked.connect(lambda: self.handle_remove_add_column_button())
        self.columns_to_rename_add_row.clicked.connect(lambda: self.handle_rename_add_row_button())
        self.columns_to_rename_add_column.clicked.connect(lambda: self.handle_rename_add_column_button())
        self.columns_to_add_add_row.clicked.connect(lambda: self.handle_add_add_row_button())
        self.columns_to_add_add_column.clicked.connect(lambda: self.handle_add_add_column_button())
        self.columns_to_reorganize_add_row.clicked.connect(lambda: self.handle_reorganize_add_row_button())
        self.columns_to_reorganize_add_column.clicked.connect(lambda: self.handle_reorganize_add_column_button())
        self.crop_add_row.clicked.connect(lambda: self.handle_crop_add_row_button())
        self.crop_add_column.clicked.connect(lambda: self.handle_crop_add_column_button())
        self.rows_to_remove_add_column.clicked.connect(lambda: self.handle_remove_rows_add_column_button())
        self.rows_to_remove_add_row.clicked.connect(lambda: self.handle_remove_rows_add_row_button())
        self.rows_to_switch_add_column.clicked.connect(lambda: self.handle_switch_rows_add_column_button())
        self.rows_to_switch_add_row.clicked.connect(lambda: self.handle_switch_rows_add_row_button())
        self.live_view.clicked.connect(lambda: self.handle_button())
        self.save.clicked.connect(lambda: self.handle_save())
        self.help.clicked.connect(lambda: self.handle_help())
        self.load.clicked.connect(lambda: self.handle_load())
        # self.label.setBuddy(self.text_edit)

        # self.setLayout(grid)

        self.columns_to_remove_func()
        self.columns_to_rename_func()
        self.columns_to_add_func()
        self.columns_to_reorganize_func()
        self.crop_func()
        self.settings_func()
        self.rows_to_remove_func()
        self.rows_to_switch_func()
        window_layout = QGridLayout()

        # self.columns_to_remove.setFixedSize(200,250)

        window_layout.addWidget(self.columns_to_remove, 0 ,0)
        window_layout.addWidget(self.columns_to_rename, 0 ,1)
        window_layout.addWidget(self.columns_to_add, 0 ,2)
        window_layout.addWidget(self.columns_to_reorganize, 0 ,3)
        window_layout.addWidget(self.crop, 1 ,3)
        window_layout.addWidget(self.settings, 0 ,4)
        window_layout.addWidget(self.rows_to_remove, 1 ,0)
        window_layout.addWidget(self.rows_to_switch, 1 ,1)
        self.setLayout(window_layout)



        self.setWindowTitle("Convert_CSV")

    def columns_to_remove_func(self):
        self.columns_to_remove = QGroupBox('Columns to Remove')
        layout = QVBoxLayout()

        layout.addWidget(self.columns_to_remove_table)
        layout.addWidget(self.columns_to_remove_add_column)
        layout.addWidget(self.columns_to_remove_add_row)


        self.columns_to_remove.setLayout(layout)

    def columns_to_rename_func(self):
        self.columns_to_rename = QGroupBox('Columns to Rename')
        layout = QVBoxLayout()

        layout.addWidget(self.columns_to_rename_table)
        layout.addWidget(self.columns_to_rename_add_column)
        layout.addWidget(self.columns_to_rename_add_row)



        self.columns_to_rename.setLayout(layout)

    def columns_to_add_func(self):
        self.columns_to_add = QGroupBox('Columns to Add')
        layout = QVBoxLayout()

        layout.addWidget(self.columns_to_add_table)
        layout.addWidget(self.columns_to_add_add_column)
        layout.addWidget(self.columns_to_add_add_row)


        self.columns_to_add.setLayout(layout)

    def columns_to_reorganize_func(self):
        self.columns_to_reorganize = QGroupBox('Columns to Reorganize')
        layout = QVBoxLayout()

        layout.addWidget(self.columns_to_reorganize_table)
        layout.addWidget(self.columns_to_reorganize_add_column)
        layout.addWidget(self.columns_to_reorganize_add_row)


        self.columns_to_reorganize.setLayout(layout)

    def crop_func(self):
        self.crop = QGroupBox('Crop')
        layout = QVBoxLayout()

        layout.addWidget(self.crop_table)
        layout.addWidget(self.crop_add_column)
        layout.addWidget(self.crop_add_row)

        self.crop.setLayout(layout)

    def handle_help(self):
        self.help = Help()
        self.help.show()

    def rows_to_remove_func(self):
        self.rows_to_remove = QGroupBox('Rows to Remove')
        layout = QVBoxLayout()

        layout.addWidget(self.rows_to_remove_table)
        layout.addWidget(self.rows_to_remove_add_row)
        layout.addWidget(self.rows_to_remove_add_column)

        self.rows_to_remove.setLayout(layout)

    def rows_to_switch_func(self):
        self.rows_to_switch = QGroupBox('Rows to Switch')
        layout = QVBoxLayout()

        layout.addWidget(self.rows_to_switch_table)
        layout.addWidget(self.rows_to_switch_add_row)
        layout.addWidget(self.rows_to_switch_add_column)

        self.rows_to_switch.setLayout(layout)

    def settings_func(self):
        self.settings = QGroupBox('Settings')
        layout = QVBoxLayout()

        layout.addWidget(self.save)
        layout.addWidget(self.live_view)
        layout.addWidget(self.help)
        layout.addWidget(self.load)

        self.settings.setLayout(layout)

    def handle_remove_add_row_button(self):
        i = self.columns_to_remove_table.rowCount()
        self.columns_to_remove_table.setRowCount(i+1)

    def handle_remove_add_column_button(self):
        i = self.columns_to_remove_table.columnCount()
        self.columns_to_remove_table.setColumnCount(i+1)

    def handle_rename_add_row_button(self):
        i = self.columns_to_rename_table.rowCount()
        self.columns_to_rename_table.setRowCount(i + 1)

    def handle_rename_add_column_button(self):
        i = self.columns_to_rename_table.columnCount()
        self.columns_to_rename_table.setColumnCount(i + 1)

    def handle_add_add_row_button(self):
        i = self.columns_to_add_table.rowCount()
        self.columns_to_add_table.setRowCount(i+1)

    def handle_add_add_column_button(self):
        i = self.columns_to_add_table.columnCount()
        self.columns_to_add_table.setColumnCount(i + 1)

    def handle_reorganize_add_row_button(self):
        i = self.columns_to_reorganize_table.rowCount()
        self.columns_to_reorganize_table.setRowCount(i+1)

    def handle_reorganize_add_column_button(self):
        i = self.columns_to_reorganize_table.columnCount()
        self.columns_to_reorganize_table.setColumnCount(i + 1)

    def handle_remove_rows_add_column_button(self):
        i = self.rows_to_remove_table.columnCount()
        self.rows_to_remove_table.setColumnCount(i + 1)

    def handle_remove_rows_add_row_button(self):
        i = self.rows_to_remove_table.rowCount()
        self.rows_to_remove_table.setRowCount(i + 1)

    def handle_switch_rows_add_column_button(self):
        i = self.rows_to_switch_table.columnCount()
        self.rows_to_switch_table.setColumnCount(i + 1)

    def handle_switch_rows_add_row_button(self):
        i = self.rows_to_switch_table.rowCount()
        self.rows_to_switch_table.setRowCount(i + 1)

    def handle_crop_add_row_button(self):
        i = self.crop_table.rowCount()
        self.crop_table.setRowCount(i+1)

    def handle_crop_add_column_button(self):
        i = self.crop_table.columnCount()
        self.crop_table.setColumnCount(i + 1)

    def handle_load(self):
        path = QFileDialog.getOpenFileName(directory=current_directory+"\\Configurations", filter="Convert_CSV file(*.cpycsv)")[0]
        with open(path) as f:
            f = f.read()
            columnsToRemove, f = f.split("\n|||NEW&TABLE2|||")
            f = "|||NEW&TABLE2|||" + f
            self.columns_to_remove_data_func(columnsToRemove)
            columnsToRename, f = f.split("\n|||NEW&TABLE3|||")
            f = "|||NEW&TABLE3|||" + f
            self.columns_to_rename_data_func(columnsToRename)
            columnsToAdd, f = f.split("\n|||NEW&TABLE4|||")
            f = "|||NEW&TABLE4|||" + f
            self.columns_to_add_data_func(columnsToAdd)
            columnsToReorganize, f = f.split("\n|||NEW&TABLE5|||")
            f = "|||NEW&TABLE5|||" + f
            self.columns_to_reorganize_data_func(columnsToReorganize)
            rowsToRemove, f = f.split("\n|||NEW&TABLE6|||")
            f = "|||NEW&TABLE6|||" + f
            self.rows_to_remove_data_func(rowsToRemove)
            rowsToSwitch, f = f.split("\n|||NEW&TABLE7|||")
            f = "|||NEW&TABLE7|||" + f
            self.rows_to_switch_data_func(rowsToSwitch)
            # cropData, f = f.split("\n|||NEW&TABLE8|||")
            # f = "|||NEW&TABLE8|||" + f
            # self.crop_data_func(cropData)

    def columns_to_remove_data_func(self, input):
        input = input.split("|||NEW&TABLE1|||\n")[1]
        input = input.split("\n")
        num = input.count('|NEWCOLUMN|')
        self.columns_to_remove_table.setColumnCount(num)
        self.columns_to_remove_table.setRowCount([index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][1] - [index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][0] -1)

    def columns_to_rename_data_func(self, input):
        input = input.split("|||NEW&TABLE2|||\n")[1]
        input = input.split("\n")
        num = input.count('|NEWCOLUMN|')
        self.columns_to_rename_table.setColumnCount(num)
        self.columns_to_rename_table.setRowCount([index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][1] - [index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][0] -1)

    def columns_to_add_data_func(self, input):
        input = input.split("|||NEW&TABLE3|||\n")[1]
        input = input.split("\n")
        num = input.count('|NEWCOLUMN|')
        self.columns_to_add_table.setColumnCount(num)
        self.columns_to_add_table.setRowCount([index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][1] - [index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][0] -1)

    def columns_to_reorganize_data_func(self, input):
        input = input.split("|||NEW&TABLE4|||\n")[1]
        input = input.split("\n")
        num = input.count('|NEWCOLUMN|')
        self.columns_to_reorganize_table.setColumnCount(num)
        self.columns_to_reorganize_table.setRowCount([index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][1] - [index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][0] -1)

    def rows_to_remove_data_func(self, input):
        input = input.split("|||NEW&TABLE5|||\n")[1]
        input = input.split("\n")
        num = input.count('|NEWCOLUMN|')
        self.rows_to_remove_table.setColumnCount(num)
        self.rows_to_remove_table.setRowCount([index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][1] - [index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][0] -1)

    def rows_to_switch_data_func(self, input):
        input = input.split("|||NEW&TABLE6|||\n")[1]
        input = input.split("\n")
        num = input.count('|NEWCOLUMN|')
        self.rows_to_switch_table.setColumnCount(num)
        self.rows_to_switch_table.setRowCount([index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][1] - [index for index, char in enumerate(input) if char == '|NEWCOLUMN|'][0] -1)

    def crop_data_func(self, cropData):
        pass


    def handle_button(self):
        pass

    def handle_save(self):
        a = []

        c = self.columns_to_remove_table.columnCount()
        r = self.columns_to_remove_table.rowCount()
        j = 0
        a.append("|||NEW&TABLE1|||")
        while j != c:
            a.append("|NEWCOLUMN|")
            i = 0
            while i != r:
                try:
                    a.append(self.columns_to_remove_table.item(i,j).text())
                except:
                    a.append("")

                i += 1
            j += 1

        c = self.columns_to_rename_table.columnCount()
        r = self.columns_to_rename_table.rowCount()
        j = 0
        a.append("|||NEW&TABLE2|||")
        while j != c:
            a.append("|NEWCOLUMN|")
            i = 0
            while i != r:
                try:
                    a.append(self.columns_to_rename_table.item(i, j).text())
                except:
                    a.append("")

                i += 1
            j += 1

        c = self.columns_to_add_table.columnCount()
        r = self.columns_to_add_table.rowCount()
        j = 0
        a.append("|||NEW&TABLE3|||")
        while j != c:
            a.append("|NEWCOLUMN|")
            i = 0
            while i != r:
                try:
                    a.append(self.columns_to_add_table.item(i, j).text())
                except:
                    a.append("")
                i += 1
            j += 1

        c = self.rows_to_remove_table.columnCount()
        r = self.rows_to_remove_table.rowCount()
        j = 0
        a.append("|||NEW&TABLE4|||")
        while j != c:
            a.append("|NEWCOLUMN|")
            i = 0
            while i != r:
                try:
                    a.append(self.columns_to_reorganize_table.item(i, j).text())
                except:
                    a.append("")
                i += 1
            j += 1

        c = self.rows_to_switch_table.columnCount()
        r = self.rows_to_switch_table.rowCount()
        j = 0
        a.append("|||NEW&TABLE5|||")
        while j != c:
            a.append("|NEWCOLUMN|")
            i = 0
            while i != r:
                try:
                    a.append(self.rows_to_remove_table.item(i, j).text())
                except:
                    a.append("")

                i += 1
            j += 1

        c = self.columns_to_reorganize_table.columnCount()
        r = self.columns_to_reorganize_table.rowCount()
        j = 0
        a.append("|||NEW&TABLE6|||")
        while j != c:
            a.append("|NEWCOLUMN|")
            i = 0
            while i != r:
                try:
                    a.append(self.rows_to_switch_table.item(i, j).text())
                except:
                    a.append("")
                i += 1
            j += 1

        c = self.crop_table.columnCount()
        r = self.crop_table.rowCount()
        j = 0
        a.append("|||NEW&TABLE7|||")
        while j != c:
            a.append("|NEWCOLUMN|")
            i = 0
            while i != r:
                try:
                    a.append(self.crop_table.item(i,j).text())
                except:
                    a.append("")
                i += 1
            j += 1
        print(a)
        current_directory = os.getcwd()
        file_path = QFileDialog.getSaveFileName(directory=current_directory+"\\Configurations", filter="Convert_CSV file(*.cpycsv)")[0]
        print(file_path)
        new_file_path = "test"+file_path
        with open(file_path, 'w') as f:
            for item in a:
                f.writelines(item + "\n")



class Help(QDialog):
    def __init__(self, parent=None):
        super(Help, self).__init__(parent)

        self.label = QLabel('Columns to Remove - COLUMN NAME\n'
                            '   if==VALUE\n'
                            '   if!==VALUE\n'
                            '   if=VALUES\n'
                            '   if!=VALUE\n'
                            'Columns to Rename - COLUMN NAME\n'
                            '   NEW NAME FOR COLUMN\n'
                            'Columns to Add - COLUMN NAME\n'
                            '   CELL VALUES\n'
                            'Columns to Reorganize - COLUMN NAME\n'
                            '   0-LAST COLUMN\n'
                            'Rows to Remove - ROW NAME\n'
                            '   if==VALUE\n'
                            '   if!==VALUE\n'
                            '   if=VALUES\n'
                            '   if!=VALUE\n'
                            'Rows to Switch - ROW NAME\n'
                            '   if CELL VALUE==VALUE --> NEW VALUE\n'
                            '   if CELL VALUE!==VALUE --> NEW VALUE\n'
                            '   if CELL VALUE=VALUE --> NEW VALUE\n'
                            '   if CELL VALUE!=VALUE --> NEW VALUE\n'
                            'Crop - COLUMN NAME\n'
                            '   ROW VALUE>\n'
                            '   ROW VALUE<\n'
                            'LOGICAL VALUES\n'
                            '   == EQUALS TO\n'
                            '   !== NOT EQUAL TO\n'
                            '   = CONTAINS\n'
                            '   != DOES NOT CONTAIN\n'
                            '   > REMOVE START\n'
                            '   < REMOVE END\n'
                            '   _ NULL VALUE\n')

        self.help()

        window_layout = QGridLayout()
        window_layout.addWidget(self.help_layout, 0 ,0)
        self.setLayout(window_layout)

    def help(self):
        self.help_layout = QGroupBox()
        layout = QVBoxLayout()

        layout.addWidget(self.label)

        self.help_layout.setLayout(layout)

class Main(QDialog):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.file_radio_button = QRadioButton()
        self.files_radio_button = QRadioButton()
        self.folder_radio_button = QRadioButton()

        self.file_text_edit = QTextEdit()
        self.file_text_edit.setFixedSize(500, 30)
        self.files_text_edit = QTextEdit()
        self.files_text_edit.setFixedSize(500, 30)
        self.folder_text_edit = QTextEdit()
        self.folder_text_edit.setFixedSize(500, 30)
        self.output_text_edit = QTextEdit()
        self.output_text_edit.setFixedSize(500, 30)
        self.config_text_edit = QTextEdit()
        self.config_text_edit.setFixedSize(500, 30)

        self.file_label = QLabel("Path:")
        self.files_label = QLabel("Path:")
        self.folder_label = QLabel("Path:")
        self.output_label = QLabel("Path:")
        self.config_label = QLabel("Path:")

        self.file_button = QPushButton("Select file")
        self.files_button = QPushButton("Select files")
        self.folder_button = QPushButton("Select folder")
        self.output_button = QPushButton("Select output")
        self.config_button = QPushButton("Select configuration")
        self.create_config_button = QPushButton("Create Configuration")
        self.start_button = QPushButton("START")

        self.file_button.clicked.connect(lambda: self.handle_file_button())
        self.files_button.clicked.connect(lambda: self.handle_files_button())
        self.folder_button.clicked.connect(lambda: self.handle_folder_button())
        self.output_button.clicked.connect(lambda: self.handle_output_button())
        self.config_button.clicked.connect(lambda: self.handle_config_button())
        self.create_config_button.clicked.connect(lambda: self.handle_create_config_button())
        self.start_button.clicked.connect(lambda: self.handle_start_button())

        self.file_radio_button.toggled.connect(self.onClicked)
        self.files_radio_button.toggled.connect(self.onClicked)
        self.folder_radio_button.toggled.connect(self.onClicked)
        # self.label.setBuddy(self.text_edit)

        # self.setLayout(grid)

        self.file_radio_button.setChecked(True)
        if self.file_radio_button.isChecked():
            pass

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.setWindowTitle("Convert_CSV")

    def handle_file_button(self):
        self.file_text_edit.setText(QFileDialog.getOpenFileName(filter="CSV(*.csv)")[0])

    def handle_files_button(self):
        self.files_text_edit.setText(str((QFileDialog.getOpenFileNames(filter="CSV(*.csv)")[0])))

    def handle_folder_button(self):
        self.folder_text_edit.setText(QFileDialog.getExistingDirectory()[0])

    def handle_output_button(self):
        self.output_text_edit.setText(QFileDialog.getSaveFileName(directory=current_directory+"\\Output", filter="CSV(*.csv)")[0])

    def handle_create_config_button(self):
        self.create_config = CreateConfig()
        self.create_config.show()


    def handle_start_button(self):
        input = self.file_text_edit.toPlainText()
        output = self.output_text_edit.toPlainText()
        config = self.config_text_edit.toPlainText()
        Engine.main(input, output, config)

    def handle_config_button(self):
        current_directory = os.getcwd()
        self.config_text_edit.setText(QFileDialog.getOpenFileName(directory=current_directory+"\\Configurations", filter="Convert_CSV file(*.cpycsv)")[0])

    def onClicked(self):
        if self.file_radio_button.isChecked():
            self.file_label.setDisabled(False)
            self.files_label.setDisabled(True)
            self.folder_label.setDisabled(True)

            self.file_text_edit.setDisabled(False)
            self.files_text_edit.setDisabled(True)
            self.folder_text_edit.setDisabled(True)

            self.file_button.setDisabled(False)
            self.files_button.setDisabled(True)
            self.folder_button.setDisabled(True)

        elif self.files_radio_button.isChecked():
            self.file_label.setDisabled(True)
            self.files_label.setDisabled(False)
            self.folder_label.setDisabled(True)

            self.file_text_edit.setDisabled(True)
            self.files_text_edit.setDisabled(False)
            self.folder_text_edit.setDisabled(True)

            self.file_button.setDisabled(True)
            self.files_button.setDisabled(False)
            self.folder_button.setDisabled(True)

        else:
            self.file_label.setDisabled(True)
            self.files_label.setDisabled(True)
            self.folder_label.setDisabled(False)

            self.file_text_edit.setDisabled(True)
            self.files_text_edit.setDisabled(True)
            self.folder_text_edit.setDisabled(False)

            self.file_button.setDisabled(True)
            self.files_button.setDisabled(True)
            self.folder_button.setDisabled(False)

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox('Grid')
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        layout.setColumnStretch(3, 4)
        layout.setColumnStretch(4, 4)
        layout.setColumnStretch(5, 4)
        layout.setColumnStretch(6, 4)

        layout.addWidget(self.file_radio_button, 0, 0)
        layout.addWidget(self.file_label, 0, 1)
        layout.addWidget(self.file_text_edit, 0, 2)
        layout.addWidget(self.file_button, 0, 3)

        layout.addWidget(self.files_radio_button, 1, 0)
        layout.addWidget(self.files_label, 1, 1)
        layout.addWidget(self.files_text_edit, 1, 2)
        layout.addWidget(self.files_button, 1, 3)

        layout.addWidget(self.folder_radio_button, 2, 0)
        layout.addWidget(self.folder_label, 2, 1)
        layout.addWidget(self.folder_text_edit, 2, 2)
        layout.addWidget(self.folder_button, 2, 3)

        layout.addWidget(self.output_label, 3, 1)
        layout.addWidget(self.output_text_edit, 3, 2)
        layout.addWidget(self.output_button, 3, 3)

        layout.addWidget(self.config_label, 4, 1)
        layout.addWidget(self.config_text_edit, 4, 2)
        layout.addWidget(self.config_button, 4, 3)

        layout.addWidget(self.create_config_button, 5, 3)
        layout.addWidget(self.start_button, 5, 2)

        self.horizontalGroupBox.setLayout(layout)


def app():
    app = QApplication(sys.argv)
    main_layout = Main()
    main_layout.show()
    sys.exit(app.exec_())


def main():
    current_directory = os.getcwd()
    if os.path.isdir(current_directory + "\\Configurations"):
        pass
    else:
        os.mkdir(current_directory + "\\Configurations")
    if os.path.isdir(current_directory + "\\Output"):
        pass
    else:
        os.mkdir(current_directory + "\\Output")
    app()

if __name__ == '__main__':
    main()