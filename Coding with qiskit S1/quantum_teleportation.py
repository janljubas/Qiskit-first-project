import qiskit
from qiskit.visualization import plot_histogram

def extract_q2(original_dict):

    result_dict = {str(int(k[0])): v for k, v in original_dict.items()}

    result_dict = {key: 0 for key in result_dict}

    for key, value in original_dict.items():
        result_dict[key[0]] += value
    
    return result_dict

'''   THEORY

We want to `teleport` the qubit q0 to the qubit 1 - copy the value of one and paste it to the other.

However, we cannot copy directly (No cloning theorem); we need a smart way to transmit the information.

That is why we are using the q1 as a resource qubit to complete this teleportation protocol.

A qubit can be perfectly transmitted using 3 qubits and 2 classical bits.
Teleportation needs: 
    × 2 qubits that are entangled -> each party (say, Alice and Bob) has one half of the entangled pair
    × a 'message' qubit that is to be transported from one qubit to another
    × a classical communication line between both parties for the transmission od 2 classical bits!

Note that q0 ( |φ⟩ ) and q1 are Alice's qubits, while q2 is Bob's qubit


-> more details in Umesh Vazirani video lectures or my notes

'''

circuit = qiskit.QuantumCircuit(3, 3)
# circuit.draw(output = 'mpl').show()


# step 0: setting a value of |φ⟩ to |1⟩ , but it could be any value
circuit.x(0)        
circuit.barrier()   # now (after the barrier) |φ⟩ = |1⟩ and we want to copy it to the q2
# circuit.draw(output='mpl').show()



# step 1: creating entanglement between q1 and q2   (Hadamard plus the CNOT gates)
circuit.h(1)  
circuit.cx(1, 2)
circuit.barrier()
circuit.draw(output='mpl').show()
# from now q1 and q2 are ENTANGLED  -> two-qubit state is now a |Ψ+⟩ Bell state:  1/√2 (|00⟩ + |11⟩ )



# step 2: Distributing the entangled qubits to Alice and Bob => total quantum state is |Ψ⟩ ⊗ [two-qubit state]
circuit.cx(0, 1)
circuit.h(0)
circuit.draw(output='mpl').show()



# step 3: Alice measures her qubits
circuit.barrier()
circuit.measure([0, 1], [0, 1])
circuit.draw(output='mpl').show()


# step 4: classical bit conditioning the bit-flip of q2 and phase-flip of q2, respectively
circuit.barrier()
circuit.cx(1, 2)
circuit.cz(0, 2)
circuit.draw(output='mpl').show()
print("The whole quantum circuit for Quantum Teleportation: \n")
print(circuit.draw())
# now q2 contains the exact state of the q0 in the beginning!

# checking the results: measuring q2

circuit.measure([2], [2])

simulator = qiskit.Aer.get_backend('qasm_simulator')
result = qiskit.execute(circuit, backend = simulator, shots = 10000).result()
counts = result.get_counts()

plot_histogram(counts).show()

print("Measurements:", extract_q2(counts))   # notice that all q2 measurements are equal to 1!


input("Press Enter to close the window...")

