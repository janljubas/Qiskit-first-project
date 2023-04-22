import qiskit
from qiskit import Aer  # local simulator framework for qiskit
from qiskit.visualization import plot_histogram
from qiskit import compiler
import matplotlib_inline

circuit = qiskit.QuantumCircuit(2,2)
circuit.cx(0,1)
circuit.h(1)
circuit.measure([0, 1], [0, 1])
print(circuit.draw())

sim_backend = Aer.get_backend("qasm_simulator")

# for backend in Aer.backends():
#     print(backend)

mapped_circuit = compiler.transpile(circuit, backend=sim_backend)
job = sim_backend.run(mapped_circuit, shots=1024)   # definiramo posao koji taj backend izvodi za nas
result = job.result()
counts = result.get_counts()

plt = plot_histogram([counts])
plt.show()
input("Press Enter to close the window...")