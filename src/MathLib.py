from src.MathRequest  import MathRequest

class MathLib:

    def __init__ (self, res):
        self.res = res

    def calculate(MathRequest):
        ope1 = MathRequest.get_ope1()
        oper = MathRequest.get_oper()
        ope2 = MathRequest.get_ope2()

        match oper:
            case '+':
                res = ope1 + ope2
            case '-':
                res = ope1 - ope2
            case '*':
                res = ope1 * ope2
            case '/':
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                else:
                    res = ope1 / ope2
            case '^':
                res = ope1 ** ope2
            case _:
                print("Invalid operator.")
        MathRequest.set_res(res)