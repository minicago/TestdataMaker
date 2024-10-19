from . import typeHandler 
from . import dataRange
import random

class intHandler(typeHandler.typeHandler):
    def dict(self,d:dict):
        return d
        pass
    def output(self, d:dict, testNum : int) -> str:
        L = typeHandler.VarResolve( d.get("range")[testNum][0])
        R = typeHandler.VarResolve( d.get("range")[testNum][1])
        res = random.randint(L, R)
        typeHandler.varTable[d.get("name","")] = res
        return str(res)
        pass
    def resolve(self,d:dict) -> typeHandler.dataRange:
        dr = dataRange.dataRange()
        dr.d = d
        return dr
        pass

typeHandler.typeTable["int"] = intHandler()