from processes.Tokenizer import Tokenizer

from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken, AndToken, OrToken, NotToken, EqualToken, \
    GreaterThenToken, LessThenToken, CupToken
from tokens.NumericToken import NumericToken
from tokens.EOFToken import EOFToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.BracketToken import OpenBracketToken, CloseBracketToken
from tokens.AssignmentToken import AssignmentToken
from tokens.IdentifierToken import IdentifierToken
from tokens.FunctionToken import WriteToken, ReadToken
from tokens.BlockToken import OpenBlockToken, CloseBlockToken
from tokens.ConditionalToken import IfToken, ElseToken
from tokens.LoopToken import IterationToken
from tokens.ColonToken import ColonToken
from tokens.CommaToken import CommaToken
from tokens.HatToken import HatToken
from tokens.StringToken import StringToken
from tokens.ReturnToken import ReturnToken
from tokens.ToToken import ToToken

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
from nodes.FuncDecNode import FuncDecNode
from nodes.FuncCallNode import FuncCallNode
from nodes.ReturnNode import ReturnNode
from nodes.BlockNode import BlockNode


def is_a_possible_token(token):
    return isinstance(token,
                      (NumericToken, PlusToken, MinusToken, OpenParenthesisToken, IdentifierToken, NotToken, ReadToken,
                       StringToken, CupToken))


possible_rel_expression_first_token = (
    IdentifierToken, NumericToken, PlusToken, MinusToken, OpenParenthesisToken, NotToken, ReadToken, StringToken,
    DivToken)


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
            while isinstance(Parser.tokenizer.next, (MultToken, AndToken)):
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
                elif isinstance(Parser.tokenizer.next, AndToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('&')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_factor())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after &, received {Parser.tokenizer.next.value}")

            Parser.last_node = node
            return node

        elif isinstance(Parser.tokenizer.next, DivToken):
            node = BinaryOpNode('/')
            Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, OpenBracketToken):
                raise Exception(f"Expected open bracket after fraction, received {Parser.tokenizer.next.value}")
            Parser.tokenizer.select_next()

            if is_a_possible_token(Parser.tokenizer.next):
                node.children.append(Parser.parse_factor())
                Parser.last_node = node
            else:
                raise Exception(f"Invalid token after /, received {Parser.tokenizer.next.value}")

            if not isinstance(Parser.tokenizer.next, CloseBracketToken):
                raise Exception(f"Expected close bracket, received {Parser.tokenizer.next.value}")
            Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, OpenBracketToken):
                raise Exception(f"Expected open bracket after fraction, received {Parser.tokenizer.next.value}")
            Parser.tokenizer.select_next()

            if is_a_possible_token(Parser.tokenizer.next):
                node.children.append(Parser.parse_factor())
                Parser.last_node = node
            else:
                raise Exception(f"Invalid token after /, received {Parser.tokenizer.next.value}")

            if not isinstance(Parser.tokenizer.next, CloseBracketToken):
                raise Exception(f"Expected close bracket, received {Parser.tokenizer.next.value}")
            Parser.tokenizer.select_next()

            return node

        else:
            raise Exception(f"Parse term could not resolve for {Parser.tokenizer.next.value}")

    @staticmethod
    def parse_expression() -> Node:
        if is_a_possible_token(Parser.tokenizer.next) or isinstance(Parser.tokenizer.next, DivToken):
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
                        _node = BinaryOpNode('|')
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

        if is_a_possible_token(Parser.tokenizer.next) or isinstance(Parser.tokenizer.next, DivToken):
            node = Parser.parse_expression()
            while isinstance(Parser.tokenizer.next, (EqualToken, GreaterThenToken, LessThenToken, CupToken)):
                if isinstance(Parser.tokenizer.next, EqualToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('=')
                        _node.children.append(node)
                        Parser.last_node = _node
                        _node.children.append(Parser.parse_expression())
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after =, received {Parser.tokenizer.next.value}")
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
                elif isinstance(Parser.tokenizer.next, CupToken):
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

        if isinstance(Parser.tokenizer.next, IdentifierToken):
            left_child = IdentifierNode(Parser.tokenizer.next.value)
            Parser.last_node = left_child
            Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, AssignmentToken):
                raise Exception(f"Missing assignment token, instead received {Parser.tokenizer.next.value}")

            node = AssignmentNode()
            node.children.append(left_child)
            Parser.last_node = node
            node.children.append(Parser.parse_rel_expression())
            Parser.last_node = node

        elif isinstance(Parser.tokenizer.next, WriteToken):
            node = WriteNode()
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(
                        f"Missing close parenthesis at Write, instead receive {Parser.tokenizer.next.value}")
                Parser.tokenizer.select_next()
                node.children.append(result)
                Parser.last_node = node
            else:
                raise Exception(
                    f"Missing open parenthesis after Write token, instead receive {Parser.tokenizer.next.value}")

        elif isinstance(Parser.tokenizer.next, IterationToken):
            node = IteratorNode()
            Parser.last_node = node
            Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, HatToken):
                raise Exception(f"Missing hat token after sum, instead received {Parser.tokenizer.next.value}")
            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenBracketToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseBracketToken):
                    raise Exception(
                        f"Missing close parenthesis at iterator, instead receive {Parser.tokenizer.next.value}")
                node.children.append(result)
                Parser.last_node = node
            else:
                raise Exception(
                    f"Missing open bracket after iterator token, instead receive {Parser.tokenizer.next.value}")

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
                if isinstance(Parser.tokenizer.next, CloseBlockToken):
                    Parser.tokenizer.select_next()
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
                if isinstance(Parser.tokenizer.next, EOFToken):
                    raise Exception(f"Missing close block token at parse block, received EOF")
        else:
            raise Exception(f"Missing open block token at parse block, received {Parser.tokenizer.next.value}")

        Parser.last_node = node
        return node

    @staticmethod
    def parse_declaration() -> Node:
        Parser.tokenizer.select_next()
        node = FuncDecNode(Parser.tokenizer.next.value)
        node.children.append(IdentifierNode(Parser.tokenizer.next.value))
        Parser.last_node = node

        if isinstance(Parser.tokenizer.see_next()[0], ColonToken):
            Parser.tokenizer.select_next()
            Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, IdentifierToken):
                raise Exception(f"Expected argument to be an identifier, got {Parser.tokenizer.next.value}")

            while isinstance(Parser.tokenizer.next, (MultToken, IdentifierToken)):
                if isinstance(Parser.tokenizer.next, MultToken):
                    Parser.tokenizer.select_next()
                    next_expected_token = IdentifierToken
                if isinstance(Parser.tokenizer.next, IdentifierToken):
                    next_expected_token = (MultToken, OpenBlockToken)
                node.children.append(IdentifierNode(Parser.tokenizer.next.value))
                Parser.tokenizer.select_next()
                if not isinstance(Parser.tokenizer.next, next_expected_token):
                    raise Exception(
                        f"Expected {next_expected_token} token, instead received {Parser.tokenizer.next.value}")

        else:
            Parser.tokenizer.select_next()

        if not isinstance(Parser.tokenizer.next, EOFToken):
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
