from abc import ABC
from numpy import double
from abc import ABC,abstractmethod

class Expression(ABC):
    @abstractmethod
    def calc(self)->double:
        pass

# implement the classes here
class Num(Expression):
    pass
class BinExp(Expression):
    pass
class Plus(BinExp):
    pass
class Minus(BinExp):
    pass
class Mul(BinExp):
    pass
class Div(BinExp):
    pass


#implement the parser function here
def parser(expression)->double:
    return 0.0

