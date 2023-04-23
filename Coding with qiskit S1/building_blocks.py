import qiskit
from qiskit.visualization import plot_bloch_multivector
from qiskit.visualization import plot_histogram
import matplotlib

'''
The goal of this excercise is to demonstrate the 3 common ways of representing  qubits/measurement results
'''

circuit = qiskit.QuantumCircuit(1, 1)
circuit.x(0)



''' 1. statevector '''
simulator = qiskit.Aer.get_backend('statevector_simulator') # statevector describes the quantum state of circuit qubits

result = qiskit.execute(circuit, backend = simulator).result()
statevector = result.get_statevector()

print(statevector)
circuit.draw(output="mpl").show()


''' 2. bloch sphere (bloch multivector) '''

plot_bloch_multivector(statevector).show()      # prikaz Blochovom sferom

circuit.measure([0], [0])
simulator = qiskit.Aer.get_backend('qasm_simulator')
result = qiskit.execute(circuit, backend = simulator, shots = 1024).result()
counts = result.get_counts()
plot_histogram([counts]).show()     # prikaz rezultata mjerenja



''' 3. matrix representation '''

circuit = qiskit.QuantumCircuit(1, 1)       # iz nekog razloga trebalo je ponovno tu napisati kod za circuit? Možda se mijenjalo nakon mjerenja itd
circuit.x(0)

simulator = qiskit.Aer.get_backend('unitary_simulator') # statevector describes the quantum state of circuit qubits

result = qiskit.execute(circuit, backend = simulator).result()
unitary = result.get_unitary()

print(unitary.data)     # printanje matrice operatora koji predstavlja NOT u ovom slučaju

input("Press Enter to close the window...")
