if __name__ == "__main__":
    exit()


def _calc(*params, sign):
    result = params[0]
    for i in params[1:]:
        if sign == "+":
            result += i
        elif sign == "-":
            result -= i
        elif sign == "*":
            result *= i
        elif sign == "/":
            if i == 0:
                print("Error, division by zero")
                return 0
            result /= i
    return result


def summ(*params):
    return _calc(*params, sign="+")


def minus(*params):
    return _calc(*params, sign="-")


def mul(*params):
    return _calc(*params, sign="*")


def div(*params):
    return _calc(*params, sign="/")
