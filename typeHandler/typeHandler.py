from . import dataRange

typeTable : dict = {}
varTable : dict = {}

def VarResolve(var):
    if not str(var)[0].isdigit():
        return varTable[var]
    else : return var

    
class typeHandler :
    
    def dict(self,d:dict):
        pass
    def output(self,d:dict, testNum : int) -> str:
        pass
    def resolve(self,d:dict) -> dataRange:
        pass