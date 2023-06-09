
def main():
    print("abc")
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.size)
    print(jar)

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Negative number")
        self._capacity=capacity
        self._size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size + n > self._capacity:
            raise ValueError("Over capacity")
        self._size+=n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("not enough cookies!")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



if __name__ == "__main__":
    main()

