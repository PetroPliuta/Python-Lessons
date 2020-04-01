import sys
print("Hello world")

# print(sys.version)
# print(sys.version_info)


class Class:
    def class_meth(self, arg):
        print(arg)


# def a = new Class

def f(x): return 2*x


print(f(123))

complex_zero = [0.0, 0.0]


def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)

    """
    if imag == 0.0 and real == 0.0:
        return complex_zero


print(complex())
