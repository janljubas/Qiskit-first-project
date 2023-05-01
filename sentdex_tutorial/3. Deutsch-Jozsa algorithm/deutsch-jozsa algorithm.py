import qiskit
from qiskit.visualization import plot_histogram, plot_bloch_multivector

qasm_sim = qiskit.Aer.get_backend('qasm_simulator')         # generating a distribution of measurements for a given circuit
statevec_sim = qiskit.Aer.get_backend('statevector_simulator')  # generating a statevector (which collapses into |0⟩ or |1⟩ when measured)

def balanced_black_box(circuit):
    circuit.cx(0, 2)
    circuit.cx(1, 2)
    return circuit

def constant_black_box(circuit):
    return circuit


circuit = qiskit.QuantumCircuit(3, 2)

circuit.x(2)
circuit.barrier()


circuit.h([0, 1, 2])    # q0 and q1 are in the state |+⟩, while q2 is in the state |-⟩  
''' notice that the order: 1. h-gate, 2. x-gate would not equate to this! not(|+⟩) = |+⟩ != |-⟩ '''

circuit.barrier()
circuit = constant_black_box(circuit)
circuit.barrier()

circuit.h([0, 1, 2])    # the second h-gate on the q2 is not neccessary

circuit.measure([0,1], [0, 1])
print(circuit.draw())
counts = qiskit.execute(circuit, backend=qasm_sim, shots = 1024).result().get_counts()
plot_histogram([counts]).show()
''' the |11⟩ result we are getting when using 'balanced_black_box' is not the output od the circuit, but rather a sign that this is a balanced circuit '''

''' the |00⟩ result we are getting when using 'constant_black_box' is, likewise, a sign of a constant circuit '''

# the 100% result means we would've gotten the same result always, meaning, only 1 query to the oracle will suffice! 

input("Press Enter to close the window...")


'''
Important to know: the D-J algo can be reproduced using many other quantum gates, for example the h-gate and the y-rotation gate
'''