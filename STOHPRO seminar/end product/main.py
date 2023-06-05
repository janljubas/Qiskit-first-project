import sys
import os
from utilities import SecondStep
'''
In short, we will implement the algorithm as follows:

-> We achieve step 1, a uniform superposition over all edges, by applying Hadamard gates to the node qubits
as well as the coin qubits.

-> For step 2(a), we implement a phase oracle.

-> Step 2(b) is implemented by a phase estimation on one step of the quantum walk on the hypercube followed by
marking all quantum states where θ != 0. We do this by rotating an auxiliary qubit.
In the last part of this step, we reverse the phase estimation.
The number of theta qubits depends on the precision of θ.

-> Step 3 is just measuring in the computational basis

'''

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    # getting the project main folder path
utils_path = os.path.join(parent_dir, 'proba+primjeri')
sys.path.append(utils_path)

from utils import OneStepCircuit

def __main__():
    one_step_circuit = OneStepCircuit()

    one_step_circuit.coin_operator()
    one_step_circuit.shift_operator()

    instruction = one_step_circuit.to_instruction()

    inversed = one_step_circuit.inverse() 
    print(inversed.draw())

    second_step = SecondStep(one_step_circuit, inversed)

    second_step.second_a_step()


__main__()