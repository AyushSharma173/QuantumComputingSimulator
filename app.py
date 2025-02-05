# # app.py
# from flask import Flask, render_template, request
# import simulator_core

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     result = None
#     circuit_text = ""
#     if request.method == "POST":
#         circuit_text = request.form.get("circuit", "")
#         commands = circuit_text.splitlines()
#         n_qbits, state, probabilities = simulator_core.run_circuit(commands)
#         # Determine number of digits (qubits) to format the binary strings
#         n_digits = n_qbits
#         state_str = ""
#         for i, amplitude in enumerate(state):
#             bin_str = format(i, '0{}b'.format(n_digits))
#             state_str += f"|{bin_str}>: {amplitude.real:.3f}"
#             # If the imaginary part is nonzero, display it.
#             if abs(amplitude.imag) > 1e-6:
#                 state_str += f" + {amplitude.imag:.3f}i"
#             state_str += "<br>"
#         prob_str = ""
#         for i, p in enumerate(probabilities):
#             bin_str = format(i, '0{}b'.format(n_digits))
#             prob_str += f"P(|{bin_str}>) = {p:.3f}<br>"
#         result = {"state": state_str, "probabilities": prob_str, "circuit": circuit_text}
#     return render_template("index.html", result=result)

# if __name__ == '__main__':
#     # Run the Flask app on port 5000 by default.
#     app.run(host="0.0.0.0", debug=True)



import os
from flask import Flask, render_template, request
import simulator_core

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    circuit_text = ""
    if request.method == "POST":
        circuit_text = request.form.get("circuit", "")
        commands = circuit_text.splitlines()
        n_qbits, state, probabilities = simulator_core.run_circuit(commands)
        
        # Format the quantum state output
        n_digits = n_qbits
        state_str = ""
        for i, amplitude in enumerate(state):
            bin_str = format(i, f'0{n_digits}b')
            state_str += f"|{bin_str}>: {amplitude.real:.3f}"
            if abs(amplitude.imag) > 1e-6:
                state_str += f" + {amplitude.imag:.3f}i"
            state_str += "<br>"
        
        # Format probability output
        prob_str = ""
        for i, p in enumerate(probabilities):
            bin_str = format(i, f'0{n_digits}b')
            prob_str += f"P(|{bin_str}>) = {p:.3f}<br>"
        
        result = {"state": state_str, "probabilities": prob_str, "circuit": circuit_text}
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the assigned port from Heroku
    app.run(host="0.0.0.0", port=port, debug=True)

