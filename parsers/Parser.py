from processes.PrePro import PrePro
from processes.Tokenizer import Tokenizer

from tokens.NumericToken import NumericToken
from tokens.OperatorToken import PlusToken, MinusToken, MultToken, DivToken
from tokens.ParenthesisToken import OpenParenthesisToken, CloseParenthesisToken
from tokens.EOFToken import EOFToken


class Parser:
    tokenizer: Tokenizer = None
    current_token = None

    @staticmethod
    def parse_factor() -> int:
        Parser.current_token = Parser.tokenizer.next
        if isinstance(Parser.current_token, NumericToken):
            return Parser.current_token.value
        if isinstance(Parser.current_token, PlusToken):
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            return result
        if isinstance(Parser.current_token, MinusToken):
            Parser.tokenizer.select_next()
            result = Parser.parse_factor()
            return -result
        if isinstance(Parser.current_token, OpenParenthesisToken):
            result = Parser.parse_expression()
            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next
            if isinstance(Parser.current_token, CloseParenthesisToken):
                return result
            raise Exception("Invalid syntax")

    @staticmethod
    def parse_term() -> int:
        Parser.current_token = Parser.tokenizer.next
        if isinstance(Parser.current_token, (NumericToken, PlusToken, MinusToken)):
            result = Parser.parse_factor()
            Parser.tokenizer.select_next()
            Parser.current_token = Parser.tokenizer.next
            while isinstance(Parser.current_token, (MultToken, DivToken)):
                if isinstance(Parser.current_token, MultToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if isinstance(Parser.current_token, NumericToken):
                        result *= Parser.parse_factor()
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, DivToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if isinstance(Parser.current_token, NumericToken):
                        result //= Parser.parse_factor()
                    else:
                        raise Exception("Invalid syntax")

                Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            return result
        raise Exception("Invalid syntax")

    @staticmethod
    def parse_expression() -> int:
        Parser.tokenizer.select_next()
        Parser.current_token = Parser.tokenizer.next

        if isinstance(Parser.current_token, (NumericToken, PlusToken, MinusToken)):
            result = Parser.parse_term()
            Parser.current_token = Parser.tokenizer.next
            while isinstance(Parser.current_token, (PlusToken, MinusToken)):
                if isinstance(Parser.current_token, PlusToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if isinstance(Parser.current_token, NumericToken):
                        result += Parser.parse_term()
                    else:
                        raise Exception("Invalid syntax")
                if isinstance(Parser.current_token, MinusToken):
                    Parser.tokenizer.select_next()
                    Parser.current_token = Parser.tokenizer.next
                    if isinstance(Parser.current_token, NumericToken):
                        result -= Parser.parse_term()
                    else:
                        raise Exception("Invalid syntax")

                # Parser.tokenizer.select_next()
                Parser.current_token = Parser.tokenizer.next

            return result
        raise Exception("Invalid syntax")

    @staticmethod
    def run(code: str) -> int:
        code = PrePro.pre_process(code)
        Parser.tokenizer = Tokenizer(code+"\0")
        result = Parser.parse_expression()
        if not isinstance(Parser.current_token, EOFToken):
            raise Exception("Invalid syntax")
        return result
