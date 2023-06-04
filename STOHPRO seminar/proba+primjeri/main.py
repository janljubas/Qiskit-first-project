from utils import OneStepCircuit

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, execute, Aer, IBMQ, QuantumRegister, ClassicalRegister
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.circuit.library import QFT
from numpy import pi
from qiskit.quantum_info import Statevector
from matplotlib import pyplot as plt
import numpy as np



def __main__():

    one_step_circuit = OneStepCircuit()

    one_step_circuit.coin_operator()
    one_step_circuit.shift_operator()

    instruction = one_step_circuit.to_instruction()

__main__()