import qiskit
from qiskit.visualization import plot_histogram
import numpy as np

my_list = [1, 3, 5, 2, 4, 9, 5, 9, 0, 7, 6]     # an unsorted list of N elements
    # we want to locate an element called winner (w) - let's say 7

'''
CLASSICAL APPROACH:     linear search of the list and comparing it to the value w
    => we can model this with a so called ORACLE - a black box which answers if a given number is w
    => we have to call the oracle function on average in N/2 times ( O(N+1) )

def the_oracle(input):
    winner = 7
    if input == winner: return True
    return False

for index, trial_element in enumerate(my_list):
    if the_oracle(trial_element):
        print(f"Winner found at index {index},\n{index + 1} calls to the Oracle used.")
        break

'''



''' QUANTUM APPROACH (  O(sqrt(N)) )        -> theory details in notebook and Umesh Vazirani lectures '''

# define the oracle circuit (in this case, only a controlled-Z gate)
oracle = qiskit.QuantumCircuit(2, name = 'oracle')
oracle.cz(0, 1)
oracle.to_gate()    # we make a gate of our circuit to use it in other complex circuits
# print(oracle.draw())  # !!!

# --------------------------------------------------------------------------------------------

reflection = qiskit.QuantumCircuit(2, name = 'reflection')  # the AMPLITUDE AMPLIFICATION -> more on Qiskit
reflection.h([0, 1])
reflection.z([0,1])
reflection.cz(0,1)    # will only apply a negative phase only to |00⟩ state
reflection.h([0, 1])

reflection.to_gate()    # we make a gate of our circuit to use it in other complex circuits
# print(reflection.draw())

# --------------------------------------------------------------------------------------------
# just a vizualizuation of what the oracle does

backend = qiskit.Aer.get_backend('statevector_simulator')
grover_circuit = qiskit.QuantumCircuit(2, 2)
grover_circuit.h([0, 1])
grover_circuit.append(oracle, [0, 1])
print(grover_circuit.draw())

result = qiskit.execute(grover_circuit, backend).result()

sv = result.get_statevector()
print(f"The statevector: {np.around(sv, 2)}")

# --------------------------------------------------------------------------------------------


backend = qiskit.Aer.get_backend('qasm_simulator')
grover_circuit = qiskit.QuantumCircuit(2, 2)
grover_circuit.h([0, 1])
grover_circuit.append(oracle, [0, 1])
grover_circuit.append(reflection, [0, 1])
grover_circuit.measure([0,1], [0,1])

print(grover_circuit.draw())

result = qiskit.execute(grover_circuit, backend, shots = 1).result()    # here we see that in only one shot we will assess it right

print(result.get_counts())  # the result is '11' ✓


input("Press Enter to close the window...")