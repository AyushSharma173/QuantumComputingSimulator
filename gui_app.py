# gui_app.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QSizePolicy
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import simulator_core

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        super().__init__(self.figure)
        self.setParent(parent)
        self.figure.tight_layout()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Quantum Computer Simulator")
        self.setGeometry(100, 100, 800, 600)

        # Central widget and layout.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        # Button to run simulation.
        self.run_button = QPushButton("Run Simulation")
        self.run_button.clicked.connect(self.run_simulation)
        self.layout.addWidget(self.run_button)

        # Text edit to show simulation output.
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.layout.addWidget(self.output_text)

        # Matplotlib canvas for plotting probabilities.
        self.canvas = MplCanvas(self, width=5, height=3, dpi=100)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.canvas)

    def run_simulation(self):
        # Update output text area.
        self.output_text.append("Simulation started...\n")
        
        # Run simulation from the core engine.
        state, probabilities = simulator_core.run_simulation()

        # Display the final state vector.
        state_str = "Final State Vector:\n"
        for i, amplitude in enumerate(state):
            state_bin = format(i, '01b')  # For a single qubit, use 1 digit.
            state_str += f"|{state_bin}>: {amplitude:.3f}\n"
        self.output_text.append(state_str)

        # Display measurement probabilities.
        prob_str = "Measurement Probabilities:\n"
        for i, p in enumerate(probabilities):
            state_bin = format(i, '01b')
            prob_str += f"P(|{state_bin}>) = {p:.3f}\n"
        self.output_text.append(prob_str)

        # Plot probabilities as a bar chart.
        self.canvas.axes.clear()
        x = list(range(len(probabilities)))
        labels = [format(i, '01b') for i in x]
        self.canvas.axes.bar(x, probabilities, tick_label=labels)
        self.canvas.axes.set_xlabel("Basis States")
        self.canvas.axes.set_ylabel("Probability")
        self.canvas.axes.set_title("Measurement Probabilities")
        self.canvas.draw()
        
        self.output_text.append("Simulation completed!\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
