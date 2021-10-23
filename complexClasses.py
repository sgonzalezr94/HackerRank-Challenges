class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, n):
        addition = complex(self.real, self.imaginary) + \
            complex(n.real, n.imaginary)
        return Complex(addition.real, addition.imag).__str__()

    def __sub__(self, n):
        substraction = complex(self.real, self.imaginary) - \
            complex(n.real, n.imaginary)
        return Complex(substraction.real, substraction.imag).__str__()

    def __mul__(self, n):
        multiplication = complex(
            self.real, self.imaginary)*complex(n.real, n.imaginary)
        return Complex(multiplication.real, multiplication.imag).__str__()

    def __truediv__(self, n):
        division = complex(self.real, self.imaginary) / complex(n.real, n.imaginary)
        return Complex(division.real, division.imag).__str__()

    def mod(self):
        return Complex(abs(complex(self.real, self.imaginary)), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


n1 = Complex(2, 1)
n2 = Complex(5, 6)



