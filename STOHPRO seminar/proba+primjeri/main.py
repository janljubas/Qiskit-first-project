from utils import OneStepCircuit

from qiskit import QuantumCircuit, execute, Aer, IBMQ, QuantumRegister, ClassicalRegister
from qiskit.compiler import transpile, assemble
from qiskit.visualization import *
from qiskit.circuit.library import QFT

def __main__():

    one_step_circuit = OneStepCircuit()

    one_step_circuit.coin_operator()
    one_step_circuit.shift_operator()

    instruction = one_step_circuit.to_instruction()

    new_circuit = QuantumCircuit(3, 3)
    new_circuit.h([0, 1, 2])
    new_circuit.measure([0, 1, 2], [0, 1, 2])
    print(new_circuit.draw())

    backend = Aer.get_backend('qasm_simulator') 
    job = execute( new_circuit, backend, shots=1000 ) 
    hist = job.result().get_counts() 
    plot_histogram( hist )

    input("Press Enter to close the window...")

__main__()