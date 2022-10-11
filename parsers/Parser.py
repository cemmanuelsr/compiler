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
    return isinstance(token, (NumericToken, PlusToken, MinusToken, OpenParenthesisToken, IdentifierToken, NotToken))


class Parser:
    tokenizer: Tokenizer = None
    current_token = None

    @staticmethod
    def parse_factor() -> Node:
        Parser.current_token = Parser.tokenizer.next
        if isinstance(Parser.current_token, NumericToken):
            return IntegerNode(Parser.current_token.value)
        if isinstance(Parser.current_token, IdentifierToken):
            return IdentifierNode(Parser.current_token.value)
        if isinstance(Parser.current_token, PlusToken):
            node = UnaryOpNode('+')
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
            return node
        if isinstance(Parser.current_token, MinusToken):
            node = UnaryOpNode('-')
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
            return node
        if isinstance(Parser.current_token, NotToken):
            node = UnaryOpNode('!')
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
            return node
        if isinstance(Parser.current_token, ReadToken):
            node = ReadNode()
            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next
            if isinstance(Parser.current_token, OpenParenthesisToken):
                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next
                if isinstance(Parser.current_token, CloseParenthesisToken):
                    return node
                else:
                    raise Exception("You must close your parenthesis, little man")
            else:
                raise Exception("Invalid syntax")
        if isinstance(Parser.current_token, OpenParenthesisToken):
            result = Parser.parse_rel_expression()
            Parser.current_token = Parser.tokenizer.next
            if isinstance(Parser.current_token, CloseParenthesisToken):
                return result
            raise Exception("You must close your parenthesis, little man")

    @staticmethod
    def parse_term() -> Node:
        Parser.current_token = Parser.tokenizer.next
        if is_a_possible_token(Parser.current_token):
            node = Parser.parse_factor()
            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next
            while isinstance(Parser.current_token, (MultToken, DivToken, AndToken)):
                if isinstance(Parser.current_token, MultToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('*')
                        _node.children.append(node)
                        result = Parser.parse_factor()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, DivToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('/')
                        _node.children.append(node)
                        result = Parser.parse_factor()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, AndToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('&&')
                        _node.children.append(node)
                        result = Parser.parse_factor()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")

                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            return node
        raise Exception("Invalid syntax")

    @staticmethod
    def parse_expression() -> Node:
        Parser.current_token = Parser.tokenizer.next
        if is_a_possible_token(Parser.current_token):
            node = Parser.parse_term()
            Parser.current_token = Parser.tokenizer.next
            while isinstance(Parser.current_token, (PlusToken, MinusToken, OrToken)):
                if isinstance(Parser.current_token, PlusToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('+')
                        _node.children.append(node)
                        result = Parser.parse_term()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, MinusToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('-')
                        _node.children.append(node)
                        result = Parser.parse_term()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, OrToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('||')
                        _node.children.append(node)
                        result = Parser.parse_term()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")

                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            return node
        raise Exception("Invalid syntax")

    @staticmethod
    def parse_rel_expression() -> Node:
        Parser.tokenizer.select_next()
        Parser.current_token = Parser.tokenizer.next

        if is_a_possible_token(Parser.current_token):
            node = Parser.parse_expression()
            Parser.current_token = Parser.tokenizer.next
            while isinstance(Parser.current_token, (EqualToken, GreaterThenToken, LessThenToken)):
                if isinstance(Parser.current_token, EqualToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('==')
                        _node.children.append(node)
                        result = Parser.parse_expression()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, GreaterThenToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('>')
                        _node.children.append(node)
                        result = Parser.parse_expression()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, LessThenToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if is_a_possible_token(Parser.current_token):
                        _node = BinaryOpNode('<')
                        _node.children.append(node)
                        result = Parser.parse_expression()
                        _node.children.append(result)
                        node = _node
                    else:
                        raise Exception("Invalid syntax")

                # Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            return node
        raise Exception("Invalid syntax")

    @staticmethod
    def parse_statement() -> Node:
        Parser.current_token = Parser.tokenizer.next
        node = None

        if isinstance(Parser.current_token, IdentifierToken):
            left_child = IdentifierNode(Parser.current_token.value)

            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next

            if isinstance(Parser.current_token, AssignmentToken):
                node = AssignmentNode()
                node.children.append(left_child)
                right_child = Parser.parse_rel_expression()
                node.children.append(right_child)
            else:
                raise Exception("Incorrect assignment expression")

            Parser.current_token = Parser.tokenizer.next
            if isinstance(Parser.current_token, SemicolonToken):
                return node
            else:
                raise Exception("Missing semicolon marker")

        elif isinstance(Parser.current_token, PrintToken):
            node = PrintNode()

            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next

            if isinstance(Parser.current_token, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                Parser.current_token = Parser.tokenizer.next
                if not isinstance(Parser.current_token, CloseParenthesisToken):
                    raise Exception("You must close your parenthesis, little man")
                node.children.append(result)
                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            Parser.current_token = Parser.tokenizer.next
            if isinstance(Parser.current_token, SemicolonToken):
                return node
            else:
                raise Exception("Missing semicolon marker")

        elif isinstance(Parser.current_token, WhileToken):
            node = WhileNode()

            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next

            if isinstance(Parser.current_token, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                Parser.current_token = Parser.tokenizer.next
                if not isinstance(Parser.current_token, CloseParenthesisToken):
                    raise Exception("You must close your parenthesis, little man")
                node.children.append(result)
                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next
                stmt = Parser.parse_statement()
                node.children.append(stmt)

        elif isinstance(Parser.current_token, IfToken):
            node = ConditionNode('If')

            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next

            if isinstance(Parser.current_token, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                Parser.current_token = Parser.tokenizer.next
                if not isinstance(Parser.current_token, CloseParenthesisToken):
                    raise Exception("You must close your parenthesis, little man")
                node.children.append(result)
                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next
                stmt = Parser.parse_statement()
                node.children.append(stmt)
                Parser.current_token = Parser.tokenizer.next
                if isinstance(Parser.current_token, ElseToken):
                    else_node = ConditionNode('Else')
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    stmt = Parser.parse_statement()
                    else_node.children.append(stmt)
                    node.children.append(else_node)

        else:
            Parser.parse_block()

    @staticmethod
    def parse_block() -> Node:
        node = BlockNode()
        Parser.tokenizer.select_next()
        Parser.current_token = Parser.tokenizer.next

        if isinstance(Parser.current_token, OpenBracketToken):
            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next
            while not isinstance(Parser.current_token, CloseBracketToken):
                result = Parser.parse_statement()
                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next
                node.children.append(result)
                if isinstance(Parser.current_token, EOFToken):
                    raise Exception("You must close your brackets, little man")

        Parser.tokenizer.select_next()
        Parser.current_token = Parser.tokenizer.next
        return node

    @staticmethod
    def run(code: str) -> Node:
        Parser.tokenizer = Tokenizer(code + "\0")
        root = Parser.parse_block()
        if not isinstance(Parser.current_token, EOFToken):
            raise Exception("Invalid syntax")
        return root
