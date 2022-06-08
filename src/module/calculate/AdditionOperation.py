from src.module.calculate.AbsOperation import AbsOperation


class AdditionOperation(AbsOperation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def doOperation(self):
        return self.a + self.b
