import qiskit
from qiskit.visualization import plot_histogram
from qiskit_ibm_provider import IBMProvider
from qiskit import compiler

circuit = qiskit.QuantumCircuit(2,2)
circuit.cx(0,1)
circuit.h(1)
circuit.measure([0, 1], [0, 1])
print(circuit.draw())

# IBMProvider.save_account(token='9b9eea23e2d44e1947f8965ab2e670692e4d469957becc89bc9af31f2231b44bca4631686017c00c18d5d0bf4f1e454a215cacc770168e1cfe35e0679cc9f5b3')

# IBM-ov provider za simuliranje sustava
provider = IBMProvider()

# print(f"Currently available devices/simulators:")
# for backend in provider.backends():
#     try:
#         qubit_count = len(backend.properties().qubits)
#     except:
#         qubit_count = "simulated"
#     print(f"{backend.name} has {backend.status().pending_jobs} queued and {qubit_count} qubits.")


# na temelju toga biramo svoj backend
backend = provider.get_backend('ibmq_qasm_simulator')


mapped_circuit = compiler.transpile(circuit, backend=backend)
job = backend.run(mapped_circuit, shots=1024)   # definiramo posao koji taj backend izvodi za nas
result = job.result()
counts = result.get_counts()

plot_histogram([counts])

print("Kraj")
