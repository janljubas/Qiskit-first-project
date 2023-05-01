import qiskit
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import math


qasm_sim = qiskit.Aer.get_backend('qasm_simulator')
statevec_sim = qiskit.Aer.get_backend('statevector_simulator')

circuit1 = qiskit.QuantumCircuit(2,2)
circuit1.ry(math.pi/4, 0)
circuit1.ry(math.pi/4, 1)

original_statevec = qiskit.execute(circuit1, backend=statevec_sim).result().get_statevector()

circuit1.measure([0,1], [0,1])
print(circuit1.draw())

plot_bloch_multivector(original_statevec).show()

original_counts = qiskit.execute(circuit1, backend=qasm_sim, shots = 1024).result().get_counts()
plot_histogram([original_counts]).show()

# --------------------------------------------------------------------------------------------------

circuit2 = qiskit.QuantumCircuit(2,2)
circuit2.h(0)
circuit2.h(1)
circuit2.ry(math.pi/4, 0)
circuit2.ry(math.pi/4, 1)

statevec = qiskit.execute(circuit2, backend=statevec_sim).result().get_statevector()

circuit2.measure([0,1], [0,1])
print(circuit2.draw())

plot_bloch_multivector(statevec).show()

counts = qiskit.execute(circuit2, backend=qasm_sim, shots = 1024).result().get_counts()
plot_histogram([counts]).show()

# quite opposite results!

# --------------------------------------------------------------------------------------------------

circuit3 = qiskit.QuantumCircuit(2,2)
circuit3.h(0)
circuit3.h(1)
circuit3.ry(math.pi/4, 0)
circuit3.ry(math.pi/4, 1)
circuit3.h(0)   # completing the `hadamard sandwich`
circuit3.h(1)


statevec_after_hadamard_sandwich = qiskit.execute(circuit3, backend=statevec_sim).result().get_statevector()
circuit3.measure([0,1], [0,1])
print(circuit3.draw())
plot_bloch_multivector(statevec_after_hadamard_sandwich).show()
counts_after_hadamard_sandwich = qiskit.execute(circuit3, backend=qasm_sim, shots = 1024).result().get_counts()
plot_histogram([counts_after_hadamard_sandwich]).show()

# the histogram is the same as without the hadamard sandwich!


input("Press Enter to close the window...")