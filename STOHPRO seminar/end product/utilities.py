## just a useful directory tree function
# def print_directory_tree(path):
#     for root, directories, files in os.walk(path):
#         level = root.replace(path, '').count(os.sep)
#         indent = '  ' * (level)
#         print(f'{indent}{os.path.basename(root)}/')
#         subindent = '  ' * (level + 1)
#         for file in files:
#             print(f'{subindent}{file}')

# print_directory_tree('STOHPRO seminar')

from qiskit.visualization import *
from qiskit.circuit.library import QFT
from numpy import pi
from qiskit.quantum_info import Statevector
from matplotlib import pyplot as plt
import numpy as np

class SecondStep:

    def __init__(self, one_step_circuit, inversed):

        self.one_step_circuit = one_step_circuit
        self.inversed = inversed
        
    def second_a_step(self):
        # Make controlled gates
        inv_cont_one_step = self.inversed.control()
        inv_cont_one_step_gate = inv_cont_one_step.to_instruction()
        cont_one_step = self.one_step_circuit.control()
        cont_one_step_gate = cont_one_step.to_instruction()


        inv_qft_gate = QFT(4, inverse=True).to_instruction()  
        qft_gate = QFT(4, inverse=False).to_instruction()

        QFT(4, inverse=True).decompose().draw("mpl")