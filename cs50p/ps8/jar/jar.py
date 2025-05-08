class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Not enough space in the jar!!")
        else:
            self.size = self.size + n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Not enough cookies to withdraw")
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        self._size = size

def main():
    jar = Jar(9)
    jar.deposit(7)
    jar.withdraw(4)
    print(jar.size)
    print(jar)


if __name__== "__main__":
    main()
