from . import typeHandler
class dataRange :
    d : dict
    def dict(self):
        ret = typeHandler.typeTable[self.d.get("type", "int")].dict(self.d)
        ret.pop("name")
        return ret
    def output(self, testNum : int) -> str:
        return typeHandler.typeTable[self.d.get("type", "int")].output(self.d,testNum)

def resolve(name : str, d: dict) -> dataRange:
    ret = typeHandler.typeTable[d.get("type", "int")].resolve(d)
    ret.d["name"] = name
    return ret