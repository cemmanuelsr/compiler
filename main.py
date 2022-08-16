class Node:
    def __init__(self, type_of_node, value, priority):
        self.left = None
        self.right = None
        self.type = type_of_node
        self.value = value
        self.priority = priority

    def evaluate(self):
        try:
            if self.type == '+':
                return self.left.evaluate() + self.right.evaluate()
            elif self.type == '-':
                return self.left.evaluate() - self.right.evaluate()
            elif self.type == '*':
                return self.left.evaluate() * self.right.evaluate()
            elif self.type == '/':
                if self.right.evaluate() == 0:
                    raise Exception('Division by zero')
                return self.left.evaluate() / self.right.evaluate()
            elif self.type == 'num' and self.right is None and self.left is None:
                return self.value
            else:
                raise Exception('Invalid syntax')
        except Exception:
            raise Exception('Invalid syntax')


def tokenize(input_str):
    tokens = []
    str_size = len(input_str)
    i = 0
    while i < str_size:
        c = input_str[i]
        if c == '+':
            tokens.append(Node('+', None, 2))
        elif c == '-':
            tokens.append(Node('-', None, 2))
        elif c == '*':
            tokens.append(Node('*', None, 1))
        elif c == '/':
            tokens.append(Node('/', None, 1))
        elif c.isdigit():
            n = ''
            j = i
            while j < str_size and c.isdigit():
                n += c
                j += 1
                if j <= str_size - 1:
                    c = input_str[j]

            tokens.append(Node('num', int(n), 0))
            i = j - 1
        elif c.isspace():
            pass
        else:
            raise Exception('Invalid token')

        i += 1

    return tokens


def swap_right(node):
    previous_left = node.right.left
    previous_right = node.right
    node.right.left = node
    node.right = previous_left
    return previous_right


def swap_left(node):
    previous_right = node.left.right
    previous_left = node.left
    node.left.right = node
    node.left = previous_right
    return previous_left


def balance_tree(node):
    while node.left.priority > node.priority or node.right.priority > node.priority:
        if node.left.priority > node.priority:
            node = swap_left(node)
        elif node.right.priority > node.priority:
            node = swap_right(node)

    return node


def create_tree(tokens):
    if len(tokens) == 0:
        raise Exception('Incorrect number of arguments')
    elif len(tokens) == 1:
        if tokens[0].type == 'num':
            return tokens[0]
        else:
            raise Exception('Invalid syntax')
    elif len(tokens) == 2:
        raise Exception('Invalid syntax')
    else:
        root = tokens[1]
        root.left = tokens[0]
        token_right = create_tree(tokens[2:])
        root.right = token_right
        root = balance_tree(root)
        return root


if __name__ == "__main__":
    import sys

    input_string = sys.argv[1]
    nodes = tokenize(input_string)
    tree_root = create_tree(nodes)
    print(tree_root.evaluate())
