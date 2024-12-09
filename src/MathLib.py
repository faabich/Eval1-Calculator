import math

class MathLib:

    @classmethod
    def execute(self, mathRequest):
        match mathRequest.get_oper():
            case "add":
                mathRequest.set_res(mathRequest.get_ope1() + mathRequest.get_ope2())
            case "sub":
                mathRequest.set_res(mathRequest.get_ope1() - mathRequest.get_ope2())
            case "mul":
                mathRequest.set_res(mathRequest.get_ope1() * mathRequest.get_ope2())
            case "div":
                if mathRequest.get_ope2() == 0:
                    print("Ne peut pas diviser par 0")
                    return None
                else:
                    mathRequest.set_res(mathRequest.get_ope1() / mathRequest.get_ope2())
            case "pow":
                mathRequest.set_res(mathRequest.get_ope1() ** mathRequest.get_ope2())
            case "root":
                mathRequest.set_res(mathRequest.get_ope1() ** (1/mathRequest.get_ope2()))
            case _:
                print("Invalid operator")
                return None