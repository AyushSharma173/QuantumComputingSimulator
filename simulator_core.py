# simulator_core.py
import numpy as np
import math

def set_bit(value, bit):
    """Set the given bit (turn it to 1) in an integer value."""
    return value | (1 << bit)

def clear_bit(value, bit):
    """Clear the given bit (turn it to 0) in an integer value."""
    return value & ~(1 << bit)

def hadamard(n_qbits, qbit, state):
    """
    Apply a Hadamard gate on the specified qubit.
    """
    new_state = np.zeros(2**n_qbits, dtype=np.complex128)
    isqrt2 = 1 / np.sqrt(2)
    for j in range(2**n_qbits):
        if state[j] != 0:
            bit = (j >> qbit) & 1
            if bit == 0:
                new_state[j] += isqrt2 * state[j]
                new_state[ set_bit(j, qbit) ] += isqrt2 * state[j]
            else:
                new_state[ clear_bit(j, qbit) ] += isqrt2 * state[j]
                new_state[j] += -isqrt2 * state[j]
    return new_state

def x_gate(n_qbits, qbit, state):
    """
    Apply a Pauli-X (NOT) gate on the specified qubit.
    """
    new_state = np.zeros(2**n_qbits, dtype=np.complex128)
    for j in range(2**n_qbits):
        if state[j] != 0:
            bit = (j >> qbit) & 1
            if bit == 0:
                new_state[ set_bit(j, qbit) ] += state[j]
            else:
                new_state[ clear_bit(j, qbit) ] += state[j]
    return new_state

def run_circuit(commands):
    """
    Run a circuit based on a list of command strings.
    
    Supported commands:
      - init n     : Initialize the circuit with n qubits (default state |0...0⟩).
      - h q        : Apply a Hadamard gate on qubit number q.
      - x q        : Apply a Pauli-X (NOT) gate on qubit number q.
    
    If no 'init' command is provided, the default is 1 qubit.
    
    Returns:
        tuple: (n_qbits, final_state, probabilities)
    """
    # Default: 1 qubit in state |0>
    n_qbits = 1
    state = np.zeros(2**n_qbits, dtype=np.complex128)
    state[0] = 1.0

    for command in commands:
        cmd = command.strip().lower()
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] == 'init':
            try:
                n_qbits = int(parts[1])
            except (IndexError, ValueError):
                n_qbits = 1
            state = np.zeros(2**n_qbits, dtype=np.complex128)
            state[0] = 1.0
        elif parts[0] == 'h':
            try:
                q = int(parts[1])
            except (IndexError, ValueError):
                continue
            state = hadamard(n_qbits, q, state)
        elif parts[0] == 'x':
            try:
                q = int(parts[1])
            except (IndexError, ValueError):
                continue
            state = x_gate(n_qbits, q, state)
        # You can extend with more commands here.
    probabilities = np.abs(state)**2
    return n_qbits, state, probabilities

def get_n_qubits_from_state(state):
    """Return the number of qubits from the state vector length."""
    return int(math.log2(len(state)))
