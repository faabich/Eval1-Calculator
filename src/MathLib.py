from src.MathRequest  import MathRequest

class MathLib:

    def __init__ (self, res):
        self.res = res

    match MathRequest.get_oper():
        case '+':
            res = MathRequest.get_ope1() + MathRequest.get_ope2()
        case '-':
            res = MathRequest.get_ope1() - MathRequest.get_ope2()
        case '*':
            res = MathRequest.get_ope1() * MathRequest.get_ope2()
        case '/':
            if MathRequest.get_ope2() == 0:
                print("Error: Division by zero is undefined.")
            else:
                res = MathRequest.get_ope1() / MathRequest.get_ope2()
        case '^':
            res = MathRequest.get_ope1() ** MathRequest.get_ope2()
        case _:
            print("Invalid operator.")
    MathRequest.set_res(res)