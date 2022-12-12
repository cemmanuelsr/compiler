from .Node import Node
from tables import func_table
from tables.SymbolTable import SymbolTable


class FuncCallNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        function = func_table.get(self.value)
        if len(self.children) != len(function.reference.children[1:-1]):
            raise Exception(
                f'Incorrect number of arguments: expected {len(function.reference.children[1:-1])} got {len(self.children)}')

        func_symbol_table = SymbolTable()
        for passed_arg, expected_arg in zip(self.children, function.reference.children[1:-1]):
            func_symbol_table.set(expected_arg.value, passed_arg.evaluate(symbol_table))

        return function.reference.children[-1].evaluate(func_symbol_table)
