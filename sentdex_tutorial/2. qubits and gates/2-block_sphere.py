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


circuit1 = qiskit.QuantumCircuit(2, 2)
circuit1.h(1)

statevector, counts = do_job(circuit1)
plt = plot_bloch_multivector(statevector)
plt.show()


circuit2 = qiskit.QuantumCircuit(3, 3)
circuit2.h(0)
circuit2.h(1)
circuit2.ccx(0, 1, 2)   # ccx je dvostruki cnot, odnosno 0. i 1. qubit kontroliraju 2.

statevector, counts2 = do_job(circuit2)
plt2 = plot_bloch_multivector(statevector)
plt2.show()

plot_histogram([counts2], legend=["output"]).show()   # -> cca 25% za svaki moguci ishod
'''
note 1: nisu moguci ishodi 011, 101, 110, 100 jer bi to znacilo da ne radi cnot
note 2: u zapisu '001' redom su qubiti 2. 1. 0. !
'''

# ima smisla da se dogadaj 111 pojavljuje 25% vremena -> jedini s flippanim 2. qubitom -> 50% × 50% da svaki od prva 2 qubita bude 1 !

# dokaz:

circuit3 = qiskit.QuantumCircuit(3, 1)  # 1 bit u klasicnom registru -> u biti samo mjerimo 1 qubit i spremamo ga u klasicni
circuit3.h(0)
circuit3.h(1)
circuit3.ccx(0, 1, 2)   
circuit3.draw()
circuit3.measure([2], [0])  # taj qubit koji mjerimo je 2. qubit

result = qiskit.execute(circuit3, backend=qasm_sim, shots = 1024).result()  # sad nisam koristio funkciju jer mjerim samo 1 qubit, ne njih n
counts = result.get_counts()
plot_histogram([counts]).show() # dobivamo 75%-25% omjer koji je očekivan!

input("Press Enter to close the window...")