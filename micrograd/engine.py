import math

class Value:
    def __init__(self, data, _prev=(), _op=""):
        self.data = data
        self._op = _op
        self.grad = 0.0
        self._prev = set(_prev)
        self._backward = lambda: None

    def __repr__(self):
        return f"Value({self.data}|{self.grad})"

    def __add__(self, other):

        if isinstance(other,(int,float)):
            other = Value(other)

        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return self * -1
    
    def __mul__(self, other):
        
        if isinstance(other,(int,float)):
            other = Value(other)

        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

    def __rmul__(self, other):
        return self * other

    def __truediv__(self,other):
        return self* other**-1

    def __pow__(self,exp):
        assert isinstance(exp, (int,float))
        out = Value(self.data**exp, (self,), f"**{exp}")

        def _backward():
            self.grad += exp * self.data**(exp-1) * out.grad
        
        out._backward = _backward
        return out

    def tanh(self):

        t = math.tanh(self.data)
        out = Value(t, (self,), "tanh()")
        
        def _backward():
            self.grad += (1 - t**2) * out.grad
        
        out._backward = _backward
        return out

    def backward(self):
        visited = set()
        order = []

        def build(node):
            if node in visited:
                return

            visited.add(node)
            for n in node._prev:
                build(n)

            order.append(node)

        build(self)
        self.grad = 1.0

        for r in reversed(order):
            r._backward()


if __name__ == "__main__":
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)

    print(a)
    a = a.tanh()
    print(a)



