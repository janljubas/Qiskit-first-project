import qiskit
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import math

qasm_sim = qiskit.Aer.get_backend('qasm_simulator')         # generating a distribution of measurements for a given circuit
statevec_sim = qiskit.Aer.get_backend('statevector_simulator')  # generating a statevector (which collapses into |0⟩ or |1⟩ when measured)

'''
Now we wish to explore the behaviour of the '100% certain measurement circuits (their statevectors)'  when a H-gate sandwich is applied
'''

circuit1 = qiskit.QuantumCircuit(2,2)

circuit1.h([0, 1])

original_statevec = qiskit.execute(circuit1, backend=statevec_sim).result().get_statevector()

circuit1.measure([0,1], [0,1])
print(circuit1.draw())

plot_bloch_multivector(original_statevec).show()

original_counts = qiskit.execute(circuit1, backend=qasm_sim, shots = 1024).result().get_counts()
plot_histogram([original_counts]).show()

# --------------------------------------------------------------------------------------------------


circuit = qiskit.QuantumCircuit(2,2)

circuit.h(0)
circuit.h(1)
circuit.rx(math.pi/4, 0)    # x-rotation doesn't change the 'parallel' (analogous to the latitude on a globe) of a Bell state
circuit.rx(math.pi/4, 1)    # --> it doesn't change  measurement probabilities
circuit.h(0)
circuit.h(1)


statevec_after_hadamard_sandwich = qiskit.execute(circuit, backend=statevec_sim).result().get_statevector()
circuit.measure([0,1], [0,1])
print(circuit.draw())
plot_bloch_multivector(statevec_after_hadamard_sandwich).show()
counts_after_hadamard_sandwich = qiskit.execute(circuit, backend=qasm_sim, shots = 1024).result().get_counts()
plot_histogram([counts_after_hadamard_sandwich]).show()




input("Press Enter to close the window...")