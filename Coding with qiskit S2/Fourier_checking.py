import qiskit
from qiskit.circuit.library import FourierChecking
from qiskit.visualization import plot_histogram

'''
The FourierChecking circuit will calculate a correlation between the 2 mappings, f and g using a Fourier transform
If the FT is > 0,05, then we say they are correlated

'''

f = [1, -1, -1, -1]
g = [1, 1, -1, 1]

circuit = FourierChecking(f=f, g=g)
print(circuit.draw())
circuit.draw(output = 'mpl').show()     # the visualization fell off, but initially the internal layers were visible


zero_zero = qiskit.quantum_info.Statevector.from_label('00')
statevector = zero_zero.evolve(circuit)      # this executes the circuit with the statevector simulator

probabilities = statevector.probabilities_dict()    # outputs

# plot_histogram(probabilities).show()
print(probabilities.get('00').round(2))


input("Press Enter to close the window...")
