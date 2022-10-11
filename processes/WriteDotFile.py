from nodes.Node import Node
from nodes.IntegerNode import IntegerNode
from nodes.UnaryOpNode import UnaryOpNode
from nodes.BinaryOpNode import BinaryOpNode
from nodes.AssignmentNode import AssignmentNode
from nodes.IdentifierNode import IdentifierNode
from nodes.PrintNode import PrintNode
from nodes.ReadNode import ReadNode
from nodes.ConditionNode import ConditionNode
from nodes.WhileNode import WhileNode
from nodes.BlockNode import BlockNode


box_shaped = (BlockNode, WhileNode, ConditionNode, ReadNode, PrintNode)
diamond_shaped = (AssignmentNode, BinaryOpNode, UnaryOpNode)
circle_shaped = (IntegerNode, IdentifierNode)


class Writer:
    node_name_map = {}
    dof_file_header = ''
    index = 0

    @staticmethod
    def create_node_with_children(node: Node):
        if node not in Writer.node_name_map:
            Writer.node_name_map[node] = f'n{Writer.index}'
            if isinstance(node, box_shaped):
                Writer.dof_file_header += f'{Writer.node_name_map[node]} [label = "{node.value}", shape="square"]\n'
            if isinstance(node, circle_shaped):
                Writer.dof_file_header += f'{Writer.node_name_map[node]} [label = "{node.value}", shape="circle"]\n'
            if isinstance(node, diamond_shaped):
                Writer.dof_file_header += f'{Writer.node_name_map[node]} [label = "{node.value}", shape="diamond"]\n'
            Writer.index += 1
        if len(node.children) == 0:
            return f'"{Writer.node_name_map[node]}"'

        node_text = ''
        for child in node.children:
            node_text += f'"{Writer.node_name_map[node]}" -- {Writer.create_node_with_children(child)}'

        return node_text

    @staticmethod
    def write(root: Node, filename: str, path: str = 'graphs/dot') -> None:
        body = '"\n"'.join(Writer.create_node_with_children(root).split('""'))
        dot_file_content = 'graph g {\n'
        dot_file_content += (Writer.dof_file_header + '\n')
        dot_file_content += (body + '\n')
        dot_file_content += '}\n'
        with open(f'{path}/{filename}.dot', 'w+') as file:
            file.write(dot_file_content)
