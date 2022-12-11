from processes.Tokenizer import Tokenizer

from tokens.NumericToken import NumericToken
from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken, AndToken, OrToken, NotToken, EqualToken, \
    GreaterThenToken, LessThenToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.BlockToken import OpenBlockToken, CloseBlockToken
from tokens.IdentifierToken import IdentifierToken
from tokens.AssignmentToken import AssignmentToken
from tokens.FunctionToken import WriteToken, ReadToken
from tokens.SemicolonToken import SemicolonToken
from tokens.ConditionalToken import IfToken, ElseToken
from tokens.LoopToken import IterationToken
from tokens.ColonToken import ColonToken
from tokens.CommaToken import CommaToken
from tokens.DotToken import DotToken
from tokens.StringToken import StringToken
from tokens.TypeToken import TypeToken
from tokens.VarDeclarationToken import VarDeclarationToken
from tokens.FnToken import FnToken
from tokens.RightArrowToken import RightArrowToken
from tokens.ReturnToken import ReturnToken
from tokens.EOFToken import EOFToken

from nodes.Node import Node
from nodes.NoOpNode import NoOpNode
from nodes.IntegerNode import IntegerNode
from nodes.UnaryOpNode import UnaryOpNode
from nodes.BinaryOpNode import BinaryOpNode
from nodes.AssignmentNode import AssignmentNode
from nodes.IdentifierNode import IdentifierNode
from nodes.WriteNode import WriteNode
from nodes.ReadNode import ReadNode
from nodes.ConditionNode import ConditionNode
from nodes.IteratorNode import IteratorNode
from nodes.StringNode import StringNode
from nodes.VarDeclarationNode import VarDeclarationNode
from nodes.FuncDecNode import FuncDecNode
from nodes.FuncCallNode import FuncCallNode
from nodes.ReturnNode import ReturnNode
from nodes.BlockNode import BlockNode


def is_a_possible_token(token):
    return isinstance(token,
                      (NumericToken, PlusToken, MinusToken, OpenParenthesisToken, IdentifierToken, NotToken, ReadToken,
                       StringToken, DotToken))


possible_rel_expression_first_token = (
    IdentifierToken, NumericToken, PlusToken, MinusToken, OpenParenthesisToken, NotToken, ReadToken, StringToken)


class Parser:
    tokenizer: Tokenizer = None
    last_node: Node = None

    @staticmethod
    def parse_factor() -> Node:
        node = None
        if isinstance(Parser.tokenizer.next, NumericToken):
            node = IntegerNode(Parser.tokenizer.next.value)
            Parser.last_node = node
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBlockToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, StringToken):
            node = StringNode(Parser.tokenizer.next.value)
            Parser.last_node = node
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBlockToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, IdentifierToken):
            if isinstance(Parser.tokenizer.see_next()[0], OpenParenthesisToken):
                node = FuncCallNode(Parser.tokenizer.next.value)
                Parser.tokenizer.select_next()

                while isinstance(Parser.tokenizer.next, (CommaToken,) + possible_rel_expression_first_token):
                    node.children.append(Parser.parse_rel_expression())
                    if not isinstance(Parser.tokenizer.next, (CommaToken, CloseParenthesisToken)):
                        raise Exception(f"Expected comma to separate arguments, received {Parser.tokenizer.next.value}")
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(f"Missing closing parenthesis, received {Parser.tokenizer.next.value}")
                if not isinstance(Parser.tokenizer.see_next()[0], OpenBlockToken):
                    Parser.tokenizer.select_next()
            else:
                node = IdentifierNode(Parser.tokenizer.next.value)
                Parser.last_node = node
                if not isinstance(Parser.tokenizer.see_next()[0], OpenBlockToken):
                    Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, PlusToken):
            node = UnaryOpNode('+')
            Parser.last_node = node
            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_factor())
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, MinusToken):
            node = UnaryOpNode('-')
            Parser.last_node = node
            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_factor())
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, NotToken):
            node = UnaryOpNode('!')
            Parser.last_node = node
            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_factor())
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, ReadToken):
            node = ReadNode()
            Parser.last_node = node
            Parser.tokenizer.select_next()
            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                Parser.tokenizer.select_next()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(
                        f"Missing close parenthesis at Read factor, instead receive {Parser.tokenizer.next.value}")
            else:
                raise Exception(
                    f"Missing open parenthesis after Read token, instead receive {Parser.tokenizer.next.value}")
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBlockToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, OpenParenthesisToken):
            node = Parser.parse_rel_expression()
            if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                raise Exception(
                    f"Missing close parenthesis after rel expression, instead receive {Parser.tokenizer.next.value}")
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBlockToken):
                Parser.tokenizer.select_next()

        if node is None:
            raise Exception(f"Parse factor could not resolve for {Parser.tokenizer.next.value}")

        Parser.last_node = node
        return node

    @staticmethod
    def parse_term() -> Node:
        if is_a_possible_token(Parser.tokenizer.next):
            node = Parser.parse_factor()
            while isinstance(Parser.tokenizer.next, (MultToken, DivToken, AndToken)):
                if isinstance(Parser.tokenizer.next, MultToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('*')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_factor())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after *, received {Parser.tokenizer.next.value}")
                elif isinstance(Parser.tokenizer.next, DivToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('/')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_factor())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after /, received {Parser.tokenizer.next.value}")
                elif isinstance(Parser.tokenizer.next, AndToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('&&')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_factor())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after &&, received {Parser.tokenizer.next.value}")

            Parser.last_node = node
            return node
        raise Exception(f"Parse term could not resolve for {Parser.tokenizer.next.value}")

    @staticmethod
    def parse_expression() -> Node:
        if is_a_possible_token(Parser.tokenizer.next):
            node = Parser.parse_term()
            while isinstance(Parser.tokenizer.next, (PlusToken, MinusToken, OrToken)):
                if isinstance(Parser.tokenizer.next, PlusToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('+')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_term())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after +, received {Parser.tokenizer.next.value}")
                elif isinstance(Parser.tokenizer.next, MinusToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('-')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_term())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after -, received {Parser.tokenizer.next.value}")
                elif isinstance(Parser.tokenizer.next, OrToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('||')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_term())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after ||, received {Parser.tokenizer.next.value}")

            return node
        raise Exception(f"Parse expression could not resolve for {Parser.tokenizer.next.value}")

    @staticmethod
    def parse_rel_expression() -> Node:
        Parser.tokenizer.select_next()

        if is_a_possible_token(Parser.tokenizer.next):
            node = Parser.parse_expression()
            while isinstance(Parser.tokenizer.next, (EqualToken, GreaterThenToken, LessThenToken, DotToken)):
                if isinstance(Parser.tokenizer.next, EqualToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('==')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_expression())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after ==, received {Parser.tokenizer.next.value}")
                elif isinstance(Parser.tokenizer.next, GreaterThenToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('>')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_expression())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after >, received {Parser.tokenizer.next.value}")
                elif isinstance(Parser.tokenizer.next, LessThenToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('<')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_expression())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after <, received {Parser.tokenizer.next.value}")
                elif isinstance(Parser.tokenizer.next, DotToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('.')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_expression())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after ., received {Parser.tokenizer.next.value}")

            Parser.last_node = node
            return node
        raise Exception(f"Parse rel expression could not resolve for {Parser.tokenizer.next.value}")

    @staticmethod
    def parse_statement() -> Node:
        node = None

        if isinstance(Parser.tokenizer.next, SemicolonToken):
            node = NoOpNode()
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, VarDeclarationToken):
            node = VarDeclarationNode()
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, IdentifierToken):
                while isinstance(Parser.tokenizer.next, (CommaToken, IdentifierToken)):
                    if isinstance(Parser.tokenizer.next, CommaToken):
                        Parser.tokenizer.select_next()
                        next_expected_token = IdentifierToken
                    if isinstance(Parser.tokenizer.next, IdentifierToken):
                        next_expected_token = (CommaToken, ColonToken)
                    _node = IdentifierNode(Parser.tokenizer.next.value)
                    node.children.append(_node)
                    Parser.tokenizer.select_next()
                    if not isinstance(Parser.tokenizer.next, next_expected_token):
                        raise Exception(
                            f"Expected {next_expected_token().type} token, instead received {Parser.tokenizer.next.value}")

                if isinstance(Parser.tokenizer.next, ColonToken):
                    Parser.tokenizer.select_next()
                    if isinstance(Parser.tokenizer.next, TypeToken):
                        if Parser.tokenizer.next.value == 'String':
                            node.cast_function = str
                        elif Parser.tokenizer.next.value == 'i32':
                            node.cast_function = int
                        Parser.tokenizer.select_next()
                    else:
                        raise Exception(
                            f'Missing type declaration of variable(s) {", ".join([child.value for child in node.children])}')
                else:
                    raise Exception(f"Missing colon token after variables, received {Parser.tokenizer.next.value}")
            else:
                raise Exception(f"Missing identifier token after var, received {Parser.tokenizer.next.value}")

            if not isinstance(Parser.tokenizer.next, SemicolonToken):
                raise Exception(f"Missing semicolon marker after Print, received {Parser.tokenizer.next.value}")

        elif isinstance(Parser.tokenizer.next, IdentifierToken):
            Parser.last_node = node

            if isinstance(Parser.tokenizer.see_next()[0], AssignmentToken):
                left_child = IdentifierNode(Parser.tokenizer.next.value)
                Parser.tokenizer.select_next()
                node = AssignmentNode()
                node.children.append(left_child)
                Parser.last_node = node
                node.children.append(Parser.parse_rel_expression())
                Parser.last_node = node

                if not isinstance(Parser.tokenizer.next, SemicolonToken):
                    raise Exception(
                        f"Missing semicolon marker after identifier, received {Parser.tokenizer.next.value}")

            elif isinstance(Parser.tokenizer.see_next()[0], OpenParenthesisToken):
                node = FuncCallNode(Parser.tokenizer.next.value)
                Parser.last_node = node
                Parser.tokenizer.select_next()

                while isinstance(Parser.tokenizer.next, (CommaToken,) + possible_rel_expression_first_token):
                    node.children.append(Parser.parse_rel_expression())
                    Parser.tokenizer.select_next()
                    if not isinstance(Parser.tokenizer.next, (CommaToken, CloseParenthesisToken)):
                        raise Exception(f"Expected comma to separate arguments, received {Parser.tokenizer.next.value}")
                if isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    Parser.last_node = node
                    Parser.tokenizer.select_next()
                    if not isinstance(Parser.tokenizer.next, SemicolonToken):
                        raise Exception(
                            f"Missing semicolon marker after closing parenthesis, received {Parser.tokenizer.next.value}")
                else:
                    raise Exception(f"Missing closing parenthesis, received {Parser.tokenizer.next.value}")

            else:
                raise Exception(f"Unexpected token after identifier, received {Parser.tokenizer.next.value}")

        elif isinstance(Parser.tokenizer.next, WriteToken):
            node = WriteNode()
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(
                        f"Missing close parenthesis at Print, instead receive {Parser.tokenizer.next.value}")
                Parser.tokenizer.select_next()
                node.children.append(result)
                Parser.last_node = node
            else:
                raise Exception(
                    f"Missing open parenthesis after Print token, instead receive {Parser.tokenizer.next.value}")

            if not isinstance(Parser.tokenizer.next, SemicolonToken):
                raise Exception(f"Missing semicolon marker after Print, received {Parser.tokenizer.next.value}")

        elif isinstance(Parser.tokenizer.next, IterationToken):
            node = IteratorNode()
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(
                        f"Missing close parenthesis at while, instead receive {Parser.tokenizer.next.value}")
                node.children.append(result)
                Parser.last_node = node
            else:
                raise Exception(
                    f"Missing open parenthesis after while token, instead receive {Parser.tokenizer.next.value}")

            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_statement())
            Parser.last_node = node

        elif isinstance(Parser.tokenizer.next, IfToken):
            node = ConditionNode('If')
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(f"Missing close parenthesis at if, instead receive {Parser.tokenizer.next.value}")
                node.children.append(result)
                Parser.last_node = node
            else:
                raise Exception(
                    f"Missing open parenthesis after if token, instead receive {Parser.tokenizer.next.value}")

            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_statement())
            Parser.last_node = node
            if isinstance(Parser.tokenizer.see_next()[0], ElseToken):
                Parser.tokenizer.select_next()
            if isinstance(Parser.tokenizer.next, ElseToken):
                else_node = ConditionNode('Else')
                Parser.last_node = else_node
                Parser.tokenizer.select_next()
                else_node.children.append(Parser.parse_statement())
                node.children.append(else_node)
                Parser.last_node = node

        elif isinstance(Parser.tokenizer.next, ReturnToken):
            node = ReturnNode()
            Parser.last_node = node
            node.children.append(Parser.parse_rel_expression())

        else:
            node = Parser.parse_block()
            Parser.last_node = node

        if node is None:
            raise Exception(f"Parse statement could not resolve for {Parser.tokenizer.next.value}")

        Parser.last_node = node
        return node

    @staticmethod
    def parse_block() -> Node:
        node = BlockNode()
        Parser.last_node = node

        if isinstance(Parser.tokenizer.next, OpenBlockToken):
            Parser.tokenizer.select_next()
            while not isinstance(Parser.tokenizer.next, CloseBlockToken):
                node.children.append(Parser.parse_statement())
                Parser.last_node = node
                Parser.tokenizer.select_next()
                if isinstance(Parser.tokenizer.next, EOFToken):
                    raise Exception("Missing close bracket at parse block")
        else:
            raise Exception(f"Missing open bracket at parse block, received {Parser.tokenizer.next.value}")

        Parser.last_node = node
        return node

    @staticmethod
    def parse_declaration() -> Node:
        Parser.tokenizer.select_next()
        if not isinstance(Parser.tokenizer.next, FnToken):
            raise Exception(f"Invalid syntax, expected fn, received {Parser.tokenizer.next.value}")
        Parser.tokenizer.select_next()
        if not isinstance(Parser.tokenizer.next, IdentifierToken):
            raise Exception(f"Invalid syntax, expected identifier of function, received {Parser.tokenizer.next.value}")

        node = FuncDecNode(Parser.tokenizer.next.value)
        node.children.append(IdentifierNode(Parser.tokenizer.next.value))
        Parser.last_node = node

        Parser.tokenizer.select_next()
        if not isinstance(Parser.tokenizer.next, OpenParenthesisToken):
            raise Exception(f"Invalid syntax, expected open parenthesis, received {Parser.tokenizer.next.value}")

        expect_identifier = False
        while not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, IdentifierToken):
                expect_identifier = False
                child = VarDeclarationNode()
                Parser.last_node = child

                while isinstance(Parser.tokenizer.next, (CommaToken, IdentifierToken)):
                    if isinstance(Parser.tokenizer.next, CommaToken):
                        Parser.tokenizer.select_next()
                        next_expected_token = IdentifierToken
                    if isinstance(Parser.tokenizer.next, IdentifierToken):
                        next_expected_token = (CommaToken, ColonToken)
                    child.children.append(IdentifierNode(Parser.tokenizer.next.value))
                    Parser.tokenizer.select_next()
                    if not isinstance(Parser.tokenizer.next, next_expected_token):
                        raise Exception(
                            f"Expected {next_expected_token().type} token, instead received {Parser.tokenizer.next.value}")

                if isinstance(Parser.tokenizer.next, ColonToken):
                    Parser.tokenizer.select_next()
                    if isinstance(Parser.tokenizer.next, TypeToken):
                        if Parser.tokenizer.next.value == 'String':
                            child.cast_function = str
                        elif Parser.tokenizer.next.value == 'i32':
                            child.cast_function = int
                    else:
                        raise Exception(
                            f'Missing type declaration of variable(s) {", ".join([_child.value for _child in child.children])}')
                else:
                    raise Exception(f"Missing colon token, received {Parser.tokenizer.next.value}")

                Parser.tokenizer.select_next()
                if isinstance(Parser.tokenizer.next, CommaToken):
                    expect_identifier = True

                node.children.append(child)

            elif isinstance(Parser.tokenizer.next, RightArrowToken):
                raise Exception(
                    f"Missing close parenthesis at parse declaration, received {Parser.tokenizer.next.value}")

            elif isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                break

            else:
                raise Exception(f"Invalid token, received {Parser.tokenizer.next.value}")

        if expect_identifier:
            raise Exception(f"Expected identifier after comma")

        Parser.tokenizer.select_next()
        if isinstance(Parser.tokenizer.next, RightArrowToken):
            Parser.tokenizer.select_next()
            if not isinstance(Parser.tokenizer.next, TypeToken):
                raise Exception(f"Expected type declaration of function")

            node.type = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()

        node.children.append(Parser.parse_block())

        return node

    @staticmethod
    def parse_program() -> Node:
        root = BlockNode()
        Parser.last_node = root

        while not isinstance(Parser.tokenizer.next, EOFToken):
            root.children.append(Parser.parse_declaration())
            Parser.last_node = root
            if isinstance(Parser.tokenizer.see_next()[0], EOFToken):
                Parser.tokenizer.select_next()

        return root

    @staticmethod
    def run(code: str) -> Node:
        Parser.tokenizer = Tokenizer(code + "\0")
        root = Parser.parse_program()
        root.value = 'Root'
        root.children.append(FuncCallNode('Main'))
        if not isinstance(Parser.tokenizer.next, EOFToken):
            raise Exception(f"Invalid syntax, instead of EOF ends with {Parser.tokenizer.next.value}")
        return root
