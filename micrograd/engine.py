class Value:
    def __init__(self, data, _prev=(), _op=""):
        self.data = data
        self._op = _op
        self.grad = 0.0
        self._prev = set(_prev)

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        out = self.data + other.data
        return Value(out, (self, other), "+")
    
    def __mul__(self, other):
        out = self.data * other.data
        return Value(out, (self, other), "*")

if __name__ == "__main__":
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    d = a*b + c

    print(d, d._prev, d._op)
    print(a)  # should still be 2.0

