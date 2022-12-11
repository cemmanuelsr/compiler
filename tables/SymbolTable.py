class SymbolTable:
    def __init__(self):
        self.table = {}

    def get(self, k):
        if k not in self.table.keys():
            raise Exception(f'{k} variable never created')
        return self.table[k]

    def set(self, k, v):
        self.table[k] = v
