# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from src.module.parseData.parseDataManager import ParseDataManager
from src.module.readData.readDataManager import ReadDataManager
from src.module.calculate.OperationManager import OperationManager

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getResult(a, b, operation):
    result =  {
        "+": a+b,
        "-": a-b,
        "*": a*b,
        "/": a/b
    }

    return result.get(operation)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    operation = "+"
    nameFile = 'data.txt'

    dataRead = ReadDataManager(nameFile)
    dataRead.doReadData()
    data = dataRead.getReadData()

    parseData = ParseDataManager(data)
    parseData.doParseData()
    data = parseData.getParseData()

    operationManager = OperationManager(operation, float(data[0]), float(data[1]))
    calcul = operationManager.getOperation()

    print(calcul.doOperation())