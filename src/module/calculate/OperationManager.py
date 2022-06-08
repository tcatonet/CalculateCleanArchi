from src.module.calculate.SubsOperation import SubsOperation
from src.module.calculate.AdditionOperation import AdditionOperation

class OperationManager():
    def __init__(self, signeOperation, a, b):
        self.signeOperation = signeOperation
        self.a = a
        self.b = b

    def getOperation(self):
        result = {
            "+": AdditionOperation(self.a, self.b),
            "-": SubsOperation(self.a, self.b)
        }
        return result.get(self.signeOperation)