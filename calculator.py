from enum import Enum
#this math operation interpreter only supports +-/*() and INT
#classes to make a tree of operations
class Operand:
    def __init__(self, value):
       self.value = value 

class Operator:
    def __init__(self, operator, left_operand, right_operand):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand


class Lexer:


    def __init__(self, input:str):
        self.input = input.replace(" ", "")
        print("self.input after replace: ", self.input)
        self.position, self.read_position = 0, 0
        self.read_char()


    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = ""
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1


    def next_token(self):
        token =dict()
        if self.ch == "+":
            token["type"] = "PLUS"
            token["literal"] = self.ch
        elif self.ch == "-":
            token["type"] = "MINUS"
            token["literal"] = self.ch
        elif self.ch == "*":
            token["type"] = "MULTIPLY"
            token["literal"] = self.ch
        elif self.ch == "/":
            token["type"] = "DIVIDE"
            token["literal"] = self.ch
        elif self.ch == "(":
            token["type"] = "LPAREN"
            token["literal"] = self.ch
        elif self.ch == ")":
            token["type"] = "RPAREN"
            token["literal"] = self.ch
        elif self.ch == "":
            token["type"] = "END"
            token["literal"] = self.ch
        else:
            if self.ch.isdigit():
                initial_position = self.position
                while self.ch.isdigit():
                    self.read_char()
                token["type"] = "INT"
                token["literal"] = self.input[initial_position:self.position]
                return token
        self.read_char()
        return token
    
    def retrieve_tokens(self):
        tokens = list()
        for _ in range(len(self.input)):
            tokens.append(self.next_token())
        return tokens


# def evaluate_expression(expression:str):
#     tokens = expression.split();
#     print(tokens)

# evaluate_expression("3 + 5 * (7 + 8)");
lexer = Lexer("3 + 5 * (7 + 8)")
print(lexer.retrieve_tokens())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
# print(lexer.next_token())
