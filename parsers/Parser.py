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
    last_node: Node = None

    @staticmethod
    def parse_factor() -> Node:
        node = None
        if isinstance(Parser.tokenizer.next, NumericToken):
            node = IntegerNode(Parser.tokenizer.next.value)
            Parser.last_node = node
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, IdentifierToken):
            node = IdentifierNode(Parser.tokenizer.next.value)
            Parser.last_node = node
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, PlusToken):
            node = UnaryOpNode('+')
            Parser.last_node = node
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, MinusToken):
            node = UnaryOpNode('-')
            Parser.last_node = node
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, NotToken):
            node = UnaryOpNode('!')
            Parser.last_node = node
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            node.children.append(result)
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, ReadToken):
            node = ReadNode()
            Parser.last_node = node
            Parser.tokenizer.select_next()
            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                Parser.tokenizer.select_next()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(f"Missing close parenthesis at Read factor, instead receive {Parser.tokenizer.next.value}")
            else:
                raise Exception(f"Missing open parenthesis after Read token, instead receive {Parser.tokenizer.next.value}")
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
                Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, OpenParenthesisToken):
            node = Parser.parse_rel_expression()
            if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                raise Exception(f"Missing close parenthesis after rel expression, instead receive {Parser.tokenizer.next.value}")
            if not isinstance(Parser.tokenizer.see_next()[0], OpenBracketToken):
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
                        result = Parser.parse_factor()
                        _node.children.append(result)
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
                        result = Parser.parse_factor()
                        _node.children.append(result)
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
                        result = Parser.parse_factor()
                        _node.children.append(result)
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
                        result = Parser.parse_term()
                        _node.children.append(result)
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
                        result = Parser.parse_term()
                        _node.children.append(result)
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
                        result = Parser.parse_term()
                        _node.children.append(result)
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
            while isinstance(Parser.tokenizer.next, (EqualToken, GreaterThenToken, LessThenToken)):
                if isinstance(Parser.tokenizer.next, EqualToken):
                    Parser.tokenizer.select_next()
                    if is_a_possible_token(Parser.tokenizer.next):
                        _node = BinaryOpNode('==')
                        _node.children.append(node)
                        Parser.last_node = _node
                        result = Parser.parse_expression()
                        _node.children.append(result)
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
                        result = Parser.parse_expression()
                        _node.children.append(result)
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
                        result = Parser.parse_expression()
                        _node.children.append(result)
                        node = _node
                        Parser.last_node = node
                    else:
                        raise Exception(f"Invalid token after <, received {Parser.tokenizer.next.value}")

            Parser.last_node = node
            return node
        raise Exception(f"Parse rel expression could not resolve for {Parser.tokenizer.next.value}")

    @staticmethod
    def parse_statement() -> Node:
        node = None

        if isinstance(Parser.tokenizer.next, SemicolonToken):
            node = NoOpNode()
            Parser.last_node = node
        elif isinstance(Parser.tokenizer.next, IdentifierToken):
            left_child = IdentifierNode(Parser.tokenizer.next.value)
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, AssignmentToken):
                node = AssignmentNode()
                node.children.append(left_child)
                Parser.last_node = node
                right_child = Parser.parse_rel_expression()
                node.children.append(right_child)
                Parser.last_node = node
            else:
                raise Exception(f"Missing assignment token after identifier, received {Parser.tokenizer.next.value}")

            if not isinstance(Parser.tokenizer.next, SemicolonToken):
                raise Exception(f"Missing semicolon marker after identifier, received {Parser.tokenizer.next.value}")

        elif isinstance(Parser.tokenizer.next, PrintToken):
            node = PrintNode()
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(f"Missing close parenthesis at Print, instead receive {Parser.tokenizer.next.value}")
                Parser.tokenizer.select_next()
                node.children.append(result)
                Parser.last_node = node
            else:
                raise Exception(f"Missing open parenthesis after Print token, instead receive {Parser.tokenizer.next.value}")

            if not isinstance(Parser.tokenizer.next, SemicolonToken):
                raise Exception(f"Missing semicolon marker after Print, received {Parser.tokenizer.next.value}")

        elif isinstance(Parser.tokenizer.next, WhileToken):
            node = WhileNode()
            Parser.last_node = node

            Parser.tokenizer.select_next()

            if isinstance(Parser.tokenizer.next, OpenParenthesisToken):
                result = Parser.parse_rel_expression()
                if not isinstance(Parser.tokenizer.next, CloseParenthesisToken):
                    raise Exception(f"Missing close parenthesis at while, instead receive {Parser.tokenizer.next.value}")
                node.children.append(result)
                Parser.last_node = node
            else:
                raise Exception(f"Missing open parenthesis after while token, instead receive {Parser.tokenizer.next.value}")

            Parser.tokenizer.select_next()
            stmt = Parser.parse_statement()
            node.children.append(stmt)
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
                raise Exception(f"Missing open parenthesis after if token, instead receive {Parser.tokenizer.next.value}")

            Parser.tokenizer.select_next()
            stmt = Parser.parse_statement()
            node.children.append(stmt)
            Parser.last_node = node
            if isinstance(Parser.tokenizer.see_next()[0], ElseToken):
                Parser.tokenizer.select_next()
            if isinstance(Parser.tokenizer.next, ElseToken):
                else_node = ConditionNode('Else')
                Parser.last_node = else_node
                Parser.tokenizer.select_next()
                stmt = Parser.parse_statement()
                else_node.children.append(stmt)
                node.children.append(else_node)
                Parser.last_node = node

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

        if isinstance(Parser.tokenizer.next, OpenBracketToken):
            Parser.tokenizer.select_next()
            while not isinstance(Parser.tokenizer.next, CloseBracketToken):
                result = Parser.parse_statement()
                node.children.append(result)
                Parser.last_node = node
                Parser.tokenizer.select_next()
                if isinstance(Parser.tokenizer.next, EOFToken):
                    raise Exception("Missing close bracket at parse block")
        else:
            raise Exception(f"Missing open bracket at parse block, received {Parser.tokenizer.next.value}")

        Parser.last_node = node
        return node

    @staticmethod
    def run(code: str) -> Node:
        Parser.tokenizer = Tokenizer(code + "\0")
        Parser.tokenizer.select_next()
        root = Parser.parse_block()
        Parser.tokenizer.select_next()
        if not isinstance(Parser.tokenizer.next, EOFToken):
            raise Exception(f"Invalid syntax, instead of EOF ends with {Parser.tokenizer.next.value}")
        return root
