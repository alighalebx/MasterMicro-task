import sys
import re
from math import pow
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide2.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.function_label = QLabel("Enter a function of x:")
        self.layout.addWidget(self.function_label)

        self.function_input = QLineEdit()
        self.layout.addWidget(self.function_input)

        self.range_label = QLabel("Enter the range of x:")
        self.layout.addWidget(self.range_label)

        self.range_layout = QHBoxLayout()
        self.layout.addLayout(self.range_layout)

        self.min_label = QLabel("Min:")
        self.range_layout.addWidget(self.min_label)

        self.min_input = QLineEdit()
        self.range_layout.addWidget(self.min_input)

        self.max_label = QLabel("Max:")
        self.range_layout.addWidget(self.max_label)

        self.max_input = QLineEdit()
        self.range_layout.addWidget(self.max_input)

        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.plot_button)

    def validate_input(self, function_str, min_str, max_str):
        # Validate function
        if not re.match(r"^[0-9+\-*/^x\s]+$", function_str):
            return False, "Invalid function. Only numeric values, '+', '-', '*', '/', '^', and 'x' are allowed."

        # Validate min and max
        try:
            min_value = float(min_str)
            max_value = float(max_str)
            if min_value >= max_value:
                return False, "Invalid range. The minimum value must be less than the maximum value."
        except ValueError:
            return False, "Invalid range. Min and max values must be numeric."

        return True, ""

    def evaluate_function(self, function_str, x):
        function_str = function_str.replace('^', '**')  # Convert ^ to ** for power operator
        function_str = function_str.replace('x', str(x))  # Replace x with the given value
        try:
            result = eval(function_str)
            return result
        except (SyntaxError, NameError):
            return None

    def plot_function(self):
        function_str = self.function_input.text()
        min_str = self.min_input.text()
        max_str = self.max_input.text()

        valid, message = self.validate_input(function_str, min_str, max_str)
        if not valid:
            QMessageBox.critical(self, "Error", message)
            return

        try:
            min_value = float(min_str)
            max_value = float(max_str)

            x = [x_val for x_val in range(int(min_value), int(max_value) + 1)]
            y = [self.evaluate_function(function_str, x_val) for x_val in x]

            plt.figure()
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Plot of f(x)')
            plt.show()
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid range. Min and max values must be numeric.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())