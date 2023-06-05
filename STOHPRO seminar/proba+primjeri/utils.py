from qiskit import QuantumCircuit

class OneStepCircuit:
    
    def __init__(self) -> None:
        self.one_step_circuit = QuantumCircuit(6, name='ONE STEP')

    # Coin operator
    def coin_operator(self):
        self.one_step_circuit.h([4,5])
        self.one_step_circuit.z([4,5])
        self.one_step_circuit.cz(4,5)
        self.one_step_circuit.h([4,5])
        # self.one_step_circuit.barrier()
        # print(self.one_step_circuit.draw())
    
# ''' If we were to define the shift operator in a separate class, the QuantumCircuit operators would be out of the scope!'''
    
    # # X gate
    # def x(self, qubit):
    #     self.one_step_circuit.x(qubit)
    
    # # CCX gate
    # def ccx(self, qubit1, qubit2, qubit3):
    #     self.one_step_circuit.ccx(qubit1, qubit2, qubit3)

    # Shift operator function for 4d-hypercube
    def shift_operator(self, print_var = None):
        for i in range(0,4):
            self.one_step_circuit.x(4)
            if i%2==0:
                self.one_step_circuit.x(5)
            self.one_step_circuit.ccx(4,5,i)
        if print_var:
            print(self.one_step_circuit.draw())
    
    # Convert to instruction (usually defined "internally", but now we have to implement it manually)
    def to_instruction(self):
        return self.one_step_circuit.to_instruction()

    def inverse(self):
        return self.one_step_circuit.inverse()

