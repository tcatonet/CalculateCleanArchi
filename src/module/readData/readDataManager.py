class ReadDataManager:

    def __init__(self, nameDataFile):
        self.nameDataFile = nameDataFile
        self.readData = ""

    def doReadData(self):
        fichier = open(self.nameDataFile, "r")
        self.readData = fichier.readlines()

    def getReadData(self):
        return self.readData