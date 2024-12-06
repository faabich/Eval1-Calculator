from src.MathLib import MathLib

class MathRequest:

    def __init__ (self, ope1, oper, ope2, res):
        self.ope1 = ope1
        self.oper = oper
        self.ope2 = ope2
        self.res = res

    def get_ope1(self):
        return self.ope1

    def get_oper(self):
        return self.oper

    def get_ope2(self):
        return self.ope2

    def get_res(self):
        return MathLib.res

    def set_res(self, value):
        raise NotImplementedError

    def to_string(self):
        raise NotImplementedError