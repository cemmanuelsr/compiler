class FuncTable:
    def __init__(self):
        self.table = {}

    def get(self, k):
        if k not in self.table.keys():
            raise Exception(f'{k} function never created')
        return self.table[k]

    def create(self, k, v):
        if k in self.table.keys():
            raise Exception(f'{k} already created on currently scope')
        self.table[k] = v
