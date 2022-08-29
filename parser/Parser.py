from processes.Tokenizer import Tokenizer


class Parser:
    tokenizer: Tokenizer = None

    @staticmethod
    def parse_expression() -> int:
        current_token = Parser.tokenizer.next
        if current_token.type == 'INT':
            result = current_token.value
            Parser.tokenizer.select_next()
            current_token = Parser.tokenizer.next
            while current_token.type in ['PLUS', 'MINUS']:
                if current_token.type == 'PLUS':
                    Parser.tokenizer.select_next()
                    current_token = Parser.tokenizer.next
                    if current_token.type == 'INT':
                        result += current_token.value
                    else:
                        raise Exception('Invalid syntax')
                if current_token.type == 'MINUS':
                    Parser.tokenizer.select_next()
                    current_token = Parser.tokenizer.next
                    if current_token.type == 'INT':
                        result -= current_token.value
                    else:
                        raise Exception('Invalid syntax')

                Parser.tokenizer.select_next()
                current_token = Parser.tokenizer.next

            if current_token.type != 'EOF':
                raise Exception('Invalid syntax')
            return result
        raise Exception('Invalid syntax')

    @staticmethod
    def run(code: str) -> int:
        Parser.tokenizer = Tokenizer(code+'\0')
        Parser.tokenizer.select_next()
        return Parser.parse_expression()
