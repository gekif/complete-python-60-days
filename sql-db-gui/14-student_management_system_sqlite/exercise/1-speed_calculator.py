import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, \
    QGridLayout, QPushButton


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel('Distance:')
        self.distance_input = QLineEdit()

        time_label = QLabel('Time (hours):')
        self.time_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        try:
            # Convert input to float
            distance = float(self.distance_input.text())
            time = float(self.time_input.text())

            # Prevent division by zero
            if time == 0:
                raise ZeroDivisionError

            # Calculate speed
            speed = distance / time

            # Prevent speed from being negative
            if speed < 0:
                self.result_label.setText("Distance and time must be positive.")
                return

            # Check selected unit
            if self.unit_combo.currentText() == 'Metric (km)':
                speed = round(speed, 2)
                unit = 'km/h'
            else:
                speed = round(speed * 0.621371, 2)
                unit = 'mph'

            # Display result
            self.result_label.setText(f"Average Speed: {speed} {unit}")

        except ValueError:
            self.result_label.setText("Please enter valid numbers.")

        except ZeroDivisionError:
            self.result_label.setText("Time cannot be zero.")


app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())
