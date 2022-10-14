from processes.Tokenizer import Tokenizer

from tokens.NumericToken import NumericToken
from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken, AndToken, OrToken, NotToken, EqualToken, \
    GreaterThenToken, LessThenToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.BracketToken import OpenBracketToken, CloseBracketToken
from tokens.IdentifierToken import IdentifierToken
from tokens.AssignmentToken import AssignmentToken
from tokens.FunctionToken import PrintToken, ReadToken
from tokens.SemicolonToken import SemicolonToken
from tokens.ConditionalToken import IfToken, ElseToken
from tokens.LoopToken import WhileToken
from tokens.EOFToken import EOFToken

from nodes.Node import Node
from nodes.NoOpNode import NoOpNode
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


def is_a_possible_token(token):
    return isinstance(token, (NumericToken, PlusToken, MinusToken, OpenParenthesisToken, IdentifierToken, NotToken, ReadToken))


class Parser:
    tokenizer: Tokenizer = None

    @staticmethod
    def parse_factor() -> Node:
        node = None
        if isinstance(Parser.tokenizer.next, NumericToken):
            node = IntegerNode(Parser.tokenizer.next.value)
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, IdentifierToken):
            node = IdentifierNode(Parser.tokenizer.next.value)
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, PlusToken):
            node = UnaryOpNode('+')
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
        elif isinstance(Parser.tokenizer.next, MinusToken):
            node = UnaryOpNode('-')
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
        elif isinstance(Parser.tokenizer.next, NotToken):
            node = UnaryOpNode('!')
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
        elif isinstance(Parser.tokenizer.next, ReadToken):
            node = ReadNode()
            Parser.tokenizer.select_next()
            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                Parser.tokenizer.select_next()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception("You must close your parenthesis, little man")
            else:
                raise Exception("Missing open parenthesis")
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, OpenParenthesisToken):
            node = Parser.parse_rel_expression()
            if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                raise Exception("You must close your parenthesis, little man")
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
                Parser.tokenizer.select_next()

        if node is None:
            raise Exception("Unexpected error")
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
                        result = Parser.parse_factor()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                elif isinstance(Parser.tokenizer.next, DivToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('/')
                        _node.children.append(node)
                        result = Parser.parse_factor()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                elif isinstance(Parser.tokenizer.next, AndToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('&&')
                        _node.children.append(node)
                        result = Parser.parse_factor()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")

            return node
        raise Exception("Invalid syntax")

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
                        result = Parser.parse_term()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                elif isinstance(Parser.tokenizer.next, MinusToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('-')
                        _node.children.append(node)
                        result = Parser.parse_term()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                elif isinstance(Parser.tokenizer.next, OrToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('||')
                        _node.children.append(node)
                        result = Parser.parse_term()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")

            return node
        raise Exception("Invalid syntax")

    @staticmethod
    def parse_rel_expression() -> Node:
        Parser.tokenizer.select_next()

        if is_a_possible_token(Parser.tokenizer.next):
            node = Parser.parse_expression()
            while isinstance(Parser.tokenizer.next, (EqualToken, GreaterThenToken, LessThenToken)):
                if isinstance(Parser.tokenizer.next, EqualToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('==')
                        _node.children.append(node)
                        result = Parser.parse_expression()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                elif isinstance(Parser.tokenizer.next, GreaterThenToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('>')
                        _node.children.append(node)
                        result = Parser.parse_expression()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                elif isinstance(Parser.tokenizer.next, LessThenToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('<')
                        _node.children.append(node)
                        result = Parser.parse_expression()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")

            return node
        raise Exception("Invalid syntax")

    @staticmethod
    def parse_statement() -> Node:
        node = None

        if isinstance(Parser.tokenizer.next, SemicolonToken):
            node = NoOpNode()
        elif isinstance(Parser.tokenizer.next, IdentifierToken):
            left_child = IdentifierNode(Parser.tokenizer.next.value)

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, AssignmentToken):
                node = AssignmentNode()
                node.children.append(left_child)
                right_child = Parser.parse_rel_expression()
                node.children.append(right_child)
            else:
                raise Exception("Incorrect assignment expression")

            if not isinstance(Parser.tokenizer.next, SemicolonToken):
                raise Exception("Missing semicolon marker")

        elif isinstance(Parser.tokenizer.next, PrintToken):
            node = PrintNode()

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception("You must close your parenthesis, little man")
                Parser.tokenizer.select_next()
                node.children.append(result)
            else:
                raise Exception("Missing open parenthesis")

            if not isinstance(Parser.tokenizer.next, SemicolonToken):
                raise Exception("Missing semicolon marker")

        elif isinstance(Parser.tokenizer.next, WhileToken):
            node = WhileNode()

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception("You must close your parenthesis, little man")
                node.children.append(result)
            else:
                raise Exception("Missing open parenthesis")

            Parser.tokenizer.select_next()
            stmt = Parser.parse_statement()
            node.children.append(stmt)

        elif isinstance(Parser.tokenizer.next, IfToken):
            node = ConditionNode('If')

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception("You must close your parenthesis, little man")
                node.children.append(result)
            else:
                raise Exception("Missing open parenthesis")

            Parser.tokenizer.select_next()
            stmt = Parser.parse_statement()
            node.children.append(stmt)
            if isinstance(Parser.tokenizer.see_next()[0], ElseToken):
                Parser.tokenizer.select_next()
            if isinstance(Parser.tokenizer.next, ElseToken):
                else_node = ConditionNode('Else')
                Parser.tokenizer.select_next()
                stmt = Parser.parse_statement()
                else_node.children.append(stmt)
                node.children.append(else_node)

        else:
            node = Parser.parse_block()

        if node is None:
            raise Exception("Unexpected error")
        return node

    @staticmethod
    def parse_block() -> Node:
        node = BlockNode()

        if isinstance(Parser.tokenizer.next, OpenBracketToken):
            Parser.tokenizer.select_next()
            while not isinstance(Parser.tokenizer.next, CloseBracketToken):
                result = Parser.parse_statement()
                node.children.append(result)
                Parser.tokenizer.select_next()
                if isinstance(Parser.tokenizer.next, EOFToken):
                    raise Exception("You must close your brackets, little man")
        else:
            raise Exception("Missing open bracket")

        return node

    @staticmethod
    def run(code: str) -> Node:
        Parser.tokenizer = Tokenizer(code + "\0")
        Parser.tokenizer.select_next()
        root = Parser.parse_block()
        Parser.tokenizer.select_next()
        if not isinstance(Parser.tokenizer.next, EOFToken):
            raise Exception("Invalid syntax")
        return root
