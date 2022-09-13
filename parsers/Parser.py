from processes.PrePro import PrePro
from processes.Tokenizer import Tokenizer

from tokens.NumericToken import NumericToken
from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.EOFToken import EOFToken

from nodes.Node import Node
from nodes.IntegerNode import IntegerNode
from nodes.UnaryOpNode import UnaryOpNode
from nodes.BinaryOpNode import BinaryOpNode


def is_a_possible_token(token):
    return isinstance(token, (NumericToken, PlusToken, MinusToken, OpenParenthesisToken))


class Parser:
    tokenizer: Tokenizer = None
    current_token = None

    @staticmethod
    def parse_factor() -> Node:
        Parser.current_token = Parser.tokenizer.next
        if isinstance(Parser.current_token, NumericToken):
            return IntegerNode(Parser.current_token.value)
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
        if isinstance(Parser.current_token, OpenParenthesisToken):
            result = Parser.parse_expression()
            Parser.current_token = Parser.tokenizer.next
            if isinstance(Parser.current_token, CloseParenthesisToken):
                return result
            raise Exception("Invalid syntax")

    @staticmethod
    def parse_term() -> Node:
        Parser.current_token = Parser.tokenizer.next
        if is_a_possible_token(Parser.current_token):
            node = Parser.parse_factor()
            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next
            while isinstance(Parser.current_token, (MultToken, DivToken)):
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

                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            return node
        raise Exception("Invalid syntax")

    @staticmethod
    def parse_expression() -> Node:
        Parser.tokenizer.select_next()
        Parser.current_token = Parser.tokenizer.next

        if isinstance(Parser.current_token, (NumericToken, PlusToken, MinusToken, OpenParenthesisToken)):
            node = Parser.parse_term()
            Parser.current_token = Parser.tokenizer.next
            while isinstance(Parser.current_token, (PlusToken, MinusToken)):
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

                # Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            return node
        raise Exception("Invalid syntax")

    @staticmethod
    def run(code: str) -> Node:
        code = PrePro.pre_process(code)
        Parser.tokenizer = Tokenizer(code + "\0")
        root = Parser.parse_expression()
        if not isinstance(Parser.current_token, EOFToken):
            raise Exception("Invalid syntax")
        return root
