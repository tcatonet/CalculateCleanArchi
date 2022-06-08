class ParseDataManager:

    def __init__(self, lignes):
        self.lignes = lignes
        self.parseData = ""

    def doParseData(self):
        for ligne in self.lignes:
            tabData = ligne.split(",")
            self.parseData = tabData

    def getParseData(self):
        return self.parseData