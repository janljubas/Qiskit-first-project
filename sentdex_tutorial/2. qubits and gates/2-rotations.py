import math
import qiskit
from qiskit import Aer 
from qiskit.visualization import plot_bloch_multivector
from qiskit.visualization import plot_histogram


statevector_simulator = Aer.get_backend("statevector_simulator")     # za plottanje Blochove sfere
qasm_sim = Aer.get_backend("qasm_simulator")     # za outpute distribucije

def do_job(circuit):
    result = qiskit.execute(circuit, backend=statevector_simulator).result()
    statevector = result.get_statevector()

    n_qubits = circuit._qubits

    circuit.measure([ i for i in range(len(n_qubits)) ],   [ i for i in range(len(circuit.clbits)) ])     # [klasični registar], [kvantni registar] -> uglavnom jednak broj bitova :)

    qasm_job = qiskit.execute(circuit, backend=qasm_sim, shots = 1024).result()
    counts = qasm_job.get_counts()

    return statevector, counts


circuit = qiskit.QuantumCircuit(3, 3)
circuit.h(0)    # hadamard
circuit.h(1)    # hadamard
# circuit.rx(math.pi, 2)  # pi/2 rotacija     < = >   circuit.x(2)        :)
circuit.rx(math.pi/7, 2)
print(circuit.draw())

statevec, counts = do_job(circuit)
plot_bloch_multivector(statevec).show()


# how does that collapse? What are the possible states and what is their distribution?
plot_histogram([counts]).show()


# now what is the distribution of the qubit 2? (could be read out in the previous diagram, but this way it's cleaner)
circuit = qiskit.QuantumCircuit(3, 1)
circuit.h(0)    # hadamard
circuit.h(1)    # hadamard
circuit.rx(math.pi/7, 2)

circuit.measure([2], [0])
result = qiskit.execute(circuit, backend=qasm_sim, shots = 1024).result()  # sad nisam koristio funkciju jer mjerim samo 1 qubit, ne njih n
counts = result.get_counts()
plot_histogram([counts]).show()


input("Press Enter to close the window...")