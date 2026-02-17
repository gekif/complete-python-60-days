import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton,
    QMainWindow, QTableWidget, QTableWidgetItem,
    QDialog, QVBoxLayout, QComboBox,
    QToolBar, QStatusBar, QMessageBox
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt


# ==========================
# DATABASE MANAGER
# ==========================
class DatabaseManager:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.initialize_database()

    def initialize_database(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                course TEXT,
                mobile TEXT
            )
        """)
        connection.commit()
        connection.close()

    def execute(self, query, params=(), fetch=False):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)

        data = cursor.fetchall() if fetch else None

        connection.commit()
        connection.close()

        return data


# ==========================
# MAIN WINDOW
# ==========================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = DatabaseManager()

        self.setWindowTitle("Student Management System")
        self.setGeometry(200, 200, 800, 450)

        self.create_ui()
        self.load_data()

    def create_ui(self):
        # ===== TABLE =====
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.setCentralWidget(self.table)

        self.table.selectionModel().selectionChanged.connect(self.update_button_state)

        # ===== TOOLBAR =====
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        add_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_action.triggered.connect(self.open_insert)
        toolbar.addAction(add_action)

        search_action = QAction(QIcon("icons/search.png"), "Search Student", self)
        search_action.triggered.connect(self.open_search)
        toolbar.addAction(search_action)

        # ===== STATUS BAR BUTTONS =====
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.edit_button = QPushButton("Edit Record")
        self.delete_button = QPushButton("Delete Record")

        self.edit_button.setEnabled(False)
        self.delete_button.setEnabled(False)

        self.edit_button.clicked.connect(self.open_edit)
        self.delete_button.clicked.connect(self.open_delete)

        self.status_bar.addPermanentWidget(self.edit_button)
        self.status_bar.addPermanentWidget(self.delete_button)

    # ======================
    # DATA METHODS
    # ======================
    def load_data(self):
        records = self.db.execute("SELECT * FROM students", fetch=True)

        self.table.setRowCount(0)

        for row_number, row_data in enumerate(records):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(str(data))
                )

        self.table.clearSelection()
        self.update_button_state()

    def get_selected_id(self):
        row = self.table.currentRow()
        if row < 0:
            return None

        item = self.table.item(row, 0)
        if item is None:
            return None

        return int(item.text())

    def update_button_state(self):
        has_selection = self.table.currentRow() >= 0
        self.edit_button.setEnabled(has_selection)
        self.delete_button.setEnabled(has_selection)

    # ======================
    # OPEN DIALOGS
    # ======================
    def open_insert(self):
        dialog = InsertDialog(self)
        if dialog.exec():
            self.load_data()

    def open_edit(self):
        student_id = self.get_selected_id()
        if student_id is None:
            QMessageBox.warning(self, "Warning", "Select a row first.")
            return

        dialog = EditDialog(self, student_id)
        if dialog.exec():
            self.load_data()

    def open_delete(self):
        student_id = self.get_selected_id()
        if student_id is None:
            QMessageBox.warning(self, "Warning", "Select a row first.")
            return

        dialog = DeleteDialog(self, student_id)
        if dialog.exec():
            self.load_data()

    def open_search(self):
        dialog = SearchDialog(self)
        dialog.exec()


# ==========================
# INSERT DIALOG
# ==========================
class InsertDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.db = parent.db
        self.setWindowTitle("Insert Student")
        self.setFixedWidth(300)

        layout = QVBoxLayout(self)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Student Name")

        self.course_input = QComboBox()
        self.course_input.addItems(["Biology", "Math", "Astronomy", "Physics"])

        self.mobile_input = QLineEdit()
        self.mobile_input.setPlaceholderText("Mobile Number")

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save)

        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Course"))
        layout.addWidget(self.course_input)
        layout.addWidget(QLabel("Mobile"))
        layout.addWidget(self.mobile_input)
        layout.addWidget(save_button)

    def save(self):
        self.db.execute(
            "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
            (
                self.name_input.text(),
                self.course_input.currentText(),
                self.mobile_input.text()
            )
        )
        self.accept()


# ==========================
# EDIT DIALOG
# ==========================
class EditDialog(QDialog):
    def __init__(self, parent, student_id):
        super().__init__(parent)

        self.db = parent.db
        self.student_id = student_id

        self.setWindowTitle("Edit Student")
        self.setFixedWidth(300)

        layout = QVBoxLayout(self)

        student_data = self.db.execute(
            "SELECT name, course, mobile FROM students WHERE id=?",
            (self.student_id,),
            fetch=True
        )

        if not student_data:
            QMessageBox.critical(self, "Error", "Student not found.")
            self.reject()
            return

        name, course, mobile = student_data[0]

        self.name_input = QLineEdit(str(name))

        self.course_input = QComboBox()
        self.course_input.addItems(["Biology", "Math", "Astronomy", "Physics"])
        self.course_input.setCurrentText(str(course))

        self.mobile_input = QLineEdit(str(mobile))

        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update)

        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Course"))
        layout.addWidget(self.course_input)
        layout.addWidget(QLabel("Mobile"))
        layout.addWidget(self.mobile_input)
        layout.addWidget(update_button)

    def update(self):
        self.db.execute(
            "UPDATE students SET name=?, course=?, mobile=? WHERE id=?",
            (
                self.name_input.text(),
                self.course_input.currentText(),
                self.mobile_input.text(),
                self.student_id
            )
        )
        self.accept()


# ==========================
# DELETE DIALOG
# ==========================
class DeleteDialog(QDialog):
    def __init__(self, parent, student_id):
        super().__init__(parent)

        self.db = parent.db
        self.student_id = student_id

        self.setWindowTitle("Confirm Delete")
        self.setFixedWidth(250)

        layout = QVBoxLayout(self)

        label = QLabel("Are you sure you want to delete this student?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        yes_button.clicked.connect(self.delete)
        no_button.clicked.connect(self.reject)

        layout.addWidget(label)
        layout.addWidget(yes_button)
        layout.addWidget(no_button)

    def delete(self):
        self.db.execute("DELETE FROM students WHERE id=?", (self.student_id,))
        self.accept()


# ==========================
# SEARCH DIALOG
# ==========================
class SearchDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.db = parent.db
        self.parent_window = parent

        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)

        layout = QVBoxLayout(self)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter student name")

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)

        layout.addWidget(self.name_input)
        layout.addWidget(search_button)

    def search(self):
        keyword = self.name_input.text().strip()

        results = self.db.execute(
            "SELECT id FROM students WHERE name LIKE ?",
            (f"%{keyword}%",),
            fetch=True
        )

        if results:
            student_id = results[0][0]
            for row in range(self.parent_window.table.rowCount()):
                if int(self.parent_window.table.item(row, 0).text()) == student_id:
                    self.parent_window.table.selectRow(row)
                    break

        self.accept()


# ==========================
# RUN APPLICATION
# ==========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())