from abc import ABC
from numpy import double
from abc import ABC,abstractmethod

class Expression(ABC):
    @abstractmethod
    def calc(self)->double:
        pass

# Implementing the classes here
class Num(Expression):
    def __init__(self, value):
        self.value = value
    def calc(self) -> double:
        return double(self.value)

class BinExp(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Plus(BinExp):
    def calc(self) -> double:
        return self.left.calc() + self.right.calc()

class Minus(BinExp):
    def calc(self) -> double:
        return self.left.calc() - self.right.calc()

class Mul(BinExp):
    def calc(self) -> double:
        return self.left.calc() * self.right.calc()
    
class Div(BinExp):
    def calc(self) -> double:
        return self.left.calc() / self.right.calc()


# Implementing the parser function here
def parser(expression)->double:
    priority = {'+':1, '-':1, '*':2, '/':2}
    operators = []
    operands = []

    def calc_latest_exp():
        # Get latest "mini exp" out (only: num operator num)
        operator = operators.pop()
        right = operands.pop()
        left = operands.pop()
        # Calculate the "mini exp" and place the calculated num as the last operand
        if operator == '+':
            operands.append(Plus(left, right))
        elif operator == '-':
            operands.append(Minus(left, right))
        elif operator == '*':
            operands.append(Mul(left, right))
        elif operator == '/':
            operands.append(Div(left, right))

    def is_negative_num(i):
        is_negative = False
        chr = expression[i]
        # If current char is minus
        if(chr == '-'):
            # If this is the first char in exp. or the char before was a math sign
            if(i == 0 or expression[i-1] in '+-*/('):
                # This means this is a minus sign that belongs to a number
                is_negative = True
        return is_negative 

    def is_part_of_num(j, i):
        chr = expression[j]
        belongs_to_num = False
        # Decimal or digit
        if(chr in '0123456789.'):
            belongs_to_num = True
        # Minus of negative number
        elif(j == i and chr == '-'):
            belongs_to_num = True
        elif(j > 0 and expression[j-1] == '-'):
            belongs_to_num = True
        return belongs_to_num

    i = 0
    # While there are tokens to be read
    while i < len(expression):
        token = expression[i]
        # If empty move on
        if token == ' ':
            i += 1
        # If the token is a number (including negatives)
        elif token in '0123456789' or is_negative_num(i):
            j = i
            # Get whole number (ex: 2, (-2), 10.122...)
            while j < len(expression) and is_part_of_num(j, i):
                j += 1
            # Handle negative numbers
            if j > 0 and expression[j-1] == '-': 
                if j == i + 1:
                    # If there is only a minus sign, this is an operator
                    operators.append('-')
                else:
                    # If this is a negative number, add to operands
                    operands.append(Num(expression[i:j]))
            else:
                # Add the poisitive number to operands
                operands.append(Num(expression[i:j]))
            # Move the index forward, and continue reading exp. after the index of saved num
            i = j
        # If the token is an operator
        elif token in '+-*/':
            # While there is a recent operator with greater (or same) priority, calculate it first 
            while (operators and operators[-1] != '(' and (priority[operators[-1]] >= priority[token])):
                # (ex: a * b + --> First calc a*b(=c) and later on calc c+... )
                calc_latest_exp()
            # (ex: a - b + --> No need to calc for now, the order is from start to end of exp
            operators.append(token)
            i += 1
        # If the token is "(" add to operators
        elif token == '(':
            operators.append(token)
            i += 1
        # If the token is ")" 
        elif token == ')':
            # Calculate exp inside "()" because this has higher priority
            while operators[-1] != '(':
                calc_latest_exp()
            operators.pop()  # Discard the (
            i += 1

    # There aren't any tokens left
    while operators:
        calc_latest_exp()

    # The exp. is calculated by now, while operands[0] has res as Num. 
    # calc() to return val of Num
    return operands[0].calc()

