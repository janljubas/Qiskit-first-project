'''
promise (promised function):
f(x) = a ⋅ x = (a_1 * x_1) xor (a_2 * x_2) xor ... xor (a_n * x_n) = a * x (mod 2)



    CLASSICAL CASE
We cannot input 111...11 because that way we'll only learn the pairity of the 1s in the dot product!
        (the output doesn't inform us which ones are 1 and which ones are 0)

That is why, classically, we can only calculate a in n steps! We want to know which bit is causing a bit-flip to our input,
hence using these 'disjunctive cases' inputs |000...01⟩, |000...10⟩, ...,|100...00⟩



    QUANTUM CASE
However, the following quantum gate is constructed in a way which offers us the solution (value of 'string' a) in only 1 try!
(meaning, using only one input, x = |000...00⟩ )
Before reading about B-V algorithm, make sure you understand the phase kick-back effect and the Deutsch algorithm.
Deutsch algorithm is similar in nature to the B-V algorithm.

Details at:
    https://learn.qiskit.org/course/ch-algorithms/bernstein-vazirani-algorithm
    https://www.youtube.com/watch?v=60OHCftlqbA&list=PLkespgaZN4gm6tZLD8rnsiENRrg6pXX4q&index=7
    https://en.wikipedia.org/wiki/Bernstein%E2%80%93Vazirani_algorithm

Short version: the classical oracle f_s returns 1 for any input x such that a ⋅ x mod2 = 1, and returns 0 otherwise. If we use the same phase kickback trick
from the Deutsch-Josza algorithm and act on a qubit in the state |-⟩, we get the transformation |x⟩ -> (-1)^(a*x) |x⟩

From there onwards, revealing the hidden bit string follows naturally by querying the quantum oracle f_s with the quantum superposition
obtained from the Hadamard transformation.

'''

import qiskit
from qiskit.visualization import plot_histogram

secretnumber = input("Write down a binary number: ")

circuit = qiskit.QuantumCircuit(len(secretnumber) + 1, len(secretnumber))

# remember, the basic generic architecture of the circuit has:
#   hadamard layer  ->  function evaluation layer  -> hadamard layer  ->  measurement

for i in range (len(secretnumber)): circuit.h(i)    # ili circuit.h(range(len(secretnumber)))

# and setting the output qubit to |-⟩
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))

circuit.barrier()

for i, checker in enumerate(reversed(secretnumber)):
    if checker == '1':
        circuit.cx(i, len(secretnumber))    # adds a CNOT gate from i-th qubit to the bottom qubit

circuit.barrier()

for i in range (len(secretnumber)): circuit.h(i)


circuit.barrier()

circuit.measure([x for x in range (len(secretnumber)) ], [x for x in range (len(secretnumber)) ])

circuit.draw(output = 'mpl').show()

simulator = qiskit.Aer.get_backend('qasm_simulator')
result = qiskit.execute(circuit, backend = simulator, shots = 1).result() # 1 shot to get the number right! :)
counts = result.get_counts()

print(counts)

plot_histogram(counts).show()

input("Press Enter to close the window...")

