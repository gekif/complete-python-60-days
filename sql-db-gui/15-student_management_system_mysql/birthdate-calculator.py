from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        # Create Widgets
        self.name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth MM/DD/YYYY:")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)

        self.output_label = QLabel("")

        # Add Widget to Grid
        grid.addWidget(self.name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)
        self.setWindowTitle("Age Calculator")

    def calculate_age(self):
        name = self.name_line_edit.text()
        date_birth = self.date_birth_line_edit.text()

        try:
            birth_date = datetime.strptime(date_birth, "%m/%d/%Y")
            today = datetime.today()
            age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day)
            )

            self.output_label.setText(f"{name.capitalize()}, you are {age} years old.")

        except ValueError:
            self.output_label.setText("Invalid date format. Please use MM/DD/YYYY.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
