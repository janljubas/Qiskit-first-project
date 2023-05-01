import qiskit
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import math


qasm_sim = qiskit.Aer.get_backend('qasm_simulator')         # generating a distribution of measurements for a given circuit
statevec_sim = qiskit.Aer.get_backend('statevector_simulator')  # generating a statevector (which collapses into |0⟩ or |1⟩ when measured)


# --------------------------------------------------------------------------------------------------
# GENERATING CIRCUIT WITH NON-CERTAIN MEASUREMENT RESULTS

circuit1 = qiskit.QuantumCircuit(2,2)

circuit1.ry(math.pi/4, 0)   # y-axis rotation is 'asymmetrical' - it puts |0⟩ and |1⟩ on the equator
circuit1.ry(math.pi/4, 1)

original_statevec = qiskit.execute(circuit1, backend=statevec_sim).result().get_statevector()

circuit1.measure([0,1], [0,1])
print(circuit1.draw())

plot_bloch_multivector(original_statevec).show()

original_counts = qiskit.execute(circuit1, backend=qasm_sim, shots = 1024).result().get_counts()
plot_histogram([original_counts]).show()

# --------------------------------------------------------------------------------------------------
# -||-, BUT WITH THE HADAMARD GATES IN FRONT


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


# --------------------------------------------------------------------------------------------------
# THE 'HADAMARD SANDWICH'


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

# having in mind that hadamard rotations equate to rotations about the (x+z)/2 axis, it all makes sense!

'''
IMPORTANT TO NOTICE:
    since the circuit1 statevector and circuit3 statevector point to the same parallel, the measurements follow the same distribution! :)
'''


input("Press Enter to close the window...")