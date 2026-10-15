class Value:
    def __init__(self, data, _prev=(), _op=""):
        self.data = data
        self._op = _op
        self.grad = 0.0
        self._prev = set(_prev)
        self._backward = lambda: None

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad


        out._backward = _backward
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

if __name__ == "__main__":
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    e = a * b
    d = e + c
    
    d.grad = 1.0
    d._backward()
    #e._backward()
    print(a,b,c)

