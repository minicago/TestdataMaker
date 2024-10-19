import json
from typeHandler import dataRange

class jsonHandler :
    name : str
    testNum : int
    testContext : str
    dR : dict
    def __init__(self):
        self.name = 'untitled'
        self.testNum = 10
        self.testContext = '$n$\n$a$'
        self.dR = {"n" : dataRange.resolve("n", {}), "a" : dataRange.resolve("a",{"type":"array", "length":"n"})}
        pass
    def dict(self):
        drtmp = self.dR
        for k in drtmp:
            drtmp[k] = drtmp[k].dict()
        return {
            "name" : self.name,
            "testNum" : self.testNum,
            "testContext" : self.testContext,
            "dataRange" : drtmp
        }

def readJson(path : str) -> jsonHandler:
    f = open(path, "r")
    j : jsonHandler
    j.data = json.load(f.read())
    f.close()
    return j

