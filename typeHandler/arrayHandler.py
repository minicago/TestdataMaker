from . import typeHandler
from . import dataRange
import random

class arrayHandler(typeHandler.typeHandler):
    def dict(self, d:dict):
        tmp = d
        tmp["context"] = d["context"].dict()
        return d
        pass
    def output(self, d:dict, testNum : int) -> str:
        length = typeHandler.VarResolve(d.get("length", "n"))
        a = []
        for i in range(0, length):
            a.append(d.get("context").output())
        typeHandler.varTable[d.get("name","")] = a
        return d.get("join"," ").join(a)
        pass
    def resolve(self, d:dict) -> dataRange:
        context = dataRange.resolve("untitled" ,d.get("context", {}))
        d["context"] = context
        dr = dataRange.dataRange()
        dr.d = d
        return dr
        pass

typeHandler.typeTable["array"] = arrayHandler()