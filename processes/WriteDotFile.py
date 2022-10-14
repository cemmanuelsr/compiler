box_shaped = ['Block', 'While', 'If', 'Else', 'Read', 'Print']
diamond_shaped = ['=', '+', '-', '*', '/', '||', '&&', '==', '<', '>']


class Writer:
    node_name_map = {}
    dof_file_header = ''
    dot_file_body = ''
    index = 0

    @staticmethod
    def create_node_name(node):
        Writer.node_name_map[node] = f'n{Writer.index}'
        if node.value in box_shaped:
            Writer.dof_file_header += f'{Writer.node_name_map[node]} [label = "{node.value}", shape="square"]\n'
        elif node.value in diamond_shaped:
            Writer.dof_file_header += f'{Writer.node_name_map[node]} [label = "{node.value}", shape="diamond"]\n'
        else:
            Writer.dof_file_header += f'{Writer.node_name_map[node]} [label = "{node.value}", shape="circle"]\n'
        Writer.index += 1

    @staticmethod
    def link_parent_and_child(node, parent):
        Writer.dot_file_body += f'"{Writer.node_name_map[parent]}" -- "{Writer.node_name_map[node]}"\n'

    @staticmethod
    def write_exception(error, node):
        # Writer.dof_file_header = Writer.dof_file_header[:-2] + ', color="red", style="filled", fontcolor="white"]\n'
        Writer.dof_file_header += f'error [label = "{error}", color="white", style="filled", fontcolor="red"]\n'
        Writer.dot_file_body += f'"{Writer.node_name_map[node]}" -- "error"\n'

    @staticmethod
    def _restart():
        Writer.node_name_map = {}
        Writer.dof_file_header = ''
        Writer.dot_file_body = ''
        Writer.index = 0

    @staticmethod
    def write(filename: str, path: str = 'graphs/dot'):
        dot_file_content = 'graph g {\n' + Writer.dof_file_header + '\n' + Writer.dot_file_body + '}'
        with open(f'{path}/{filename}.dot', 'w+') as file:
            file.write(dot_file_content)
        Writer._restart()
