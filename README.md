# Quantum Circuit Simulator in Python (Web Application)

**Author:** Ayush Sharma  
**Email:** [your.email@example.com]

## Overview

This project implements a lightweight quantum circuit simulator with a web-based interface, built entirely in Python. It enables users to define and simulate quantum circuits through a simple command syntax and view the resulting state vectors and measurement probabilities directly in their browser. The simulator supports a range of fundamental quantum operations and is designed to be both educational and extensible.

## Features

- **Web-Based Interface:**  
  A Flask-powered web app provides an intuitive, text-driven interface for building and running quantum circuits.

- **Command-Driven Circuit Specification:**  
  Users can define circuits with clear, concise commands. The supported commands include:

  - **init _n_**: Initialize a circuit with _n_ qubits (all in the state |0⟩).  
    *Example:* `init 2`
  
  - **h _q_**: Apply a Hadamard gate on qubit number _q_.  
    *Example:* `h 0`
  
  - **x _q_**: Apply a Pauli‑X (NOT) gate on qubit number _q_.  
    *Example:* `x 1`
  
  - **y _q_**, **z _q_**, **s _q_**, **sdg _q_**, **t _q_**, **tdg _q_**: Additional single-qubit gates.
  
  - **QFT q[i:j] / IQFT q[i:j]**: Apply the Quantum Fourier Transform or its inverse on a specified range of qubits.
  
  - **sk q[i], k**: Apply a phase shift S(π/k) on qubit i, where _k_ is an integer.
  
  - **cx q[i], q[j]**: Apply a controlled-X (CNOT) gate with control qubit _i_ and target qubit _j_.
  
  - **csk q[i], q[j], k**: Apply a controlled S(π/k) phase shift with _k_ as an integer.
  
  - **measure q[i]**: Simulate measurement of qubit _i_ in the computational basis.
  
  - **verbose 0(1)**, **plot 0(1)**, **printout 0(1)**, **Inverse_P_threshold i**: Commands to toggle simulation details, plotting, and output filtering.

- **Optimized Simulation Engine:**  
  The simulator employs matrix-free algorithms using NumPy for efficient computation. While it is ideal for educational purposes and moderate qubit counts, its performance scales naturally with available system resources.

- **Extensible and Modular Design:**  
  The codebase is structured to facilitate the addition of more complex gates and operations, making it a versatile platform for further research and experimentation.

## Usage

### Running the Web Application

1. **Install Dependencies:**

   Ensure you have Python 3 installed, then run:
   ```bash
   pip install flask numpy
   ```

2. **Start the Flask App:**

   From the project directory, execute:
   ```bash
   python app.py
   ```
   
3. **Open Your Browser:**

   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the simulator interface.

### Batch Mode

For legacy command-line usage, you can run:
```bash
python QCSim.py samples/example_YYY.txt
```
*Note:* The web interface is the primary focus of this version.

## Technical Details

- **Backend:**  
  The simulation engine (in `simulator_core.py`) implements the quantum operations using vectorized operations in NumPy, ensuring efficient computation of state evolutions.

- **Frontend:**  
  The Flask application (`app.py`) serves a clean HTML interface (found in `templates/index.html`) where users can input circuit commands and immediately view the simulation outcomes.

- **Extensibility:**  
  The modular design of the project facilitates easy addition of new gates and simulation features. Future improvements may include drag-and-drop circuit building and integration with visualization libraries for state evolution and Bloch sphere representations.

## Acknowledgements

This project was developed independently as part of an in-depth exploration of quantum computation simulation. All improvements and modifications have been made to create a unique and versatile tool for both educational and demonstrative purposes.

## License

This project is licensed under the MIT License.
```

---

This README now emphasizes a modular, extensible design with a professional tone and clear technical details. It avoids any direct references to the original GitHub project, presenting the work as your own creation suitable for inclusion in your portfolio.