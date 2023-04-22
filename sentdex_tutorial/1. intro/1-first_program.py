import qiskit as q
from qiskit.visualization import circuit_drawer

circuit = q.QuantumCircuit(2,2)     # 2 qubits, 2 classical bits

# currently: 0,0
circuit.x(0)    # not gate
# 1, 0
circuit.cx(0, 1)    # cnot -> flips 2nd value IFF first qubit is 1

circuit.measure([0, 1], [0, 1])     # how quantum register is mapped to classical register

# version 1 (in terminal)
print(circuit.draw())
# version 2 (matplotlib window)
circuit_drawer(circuit, output='mpl').show()

input("Press Enter to close the window...")     # this line is important just for the matplotlib window not to close instantlys
