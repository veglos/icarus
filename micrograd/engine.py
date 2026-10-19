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

        print(order)

        for r in reversed(order):
            r._backward()


if __name__ == "__main__":
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)

    e = a * b
    d = e + c
    f = d * e

    f.backward()

    print(a,b,c)



