import queue
from sys import stdin


class Stack:

    def __init__(self):
        self.__q1 = queue.Queue()
        self.__q2 = queue.Queue()

    def push(self, data):
        self.__q1.put(data)

    def pop(self):
        if self.isEmpty():
            return -1
        while self.__q1.qsize() > 1:
            self.__q2.put(self.__q1.get())
        ans = self.__q1.get()
        self.__q1,self.__q2=self.__q2,self.__q1
        return ans

    def top(self):
        if self.isEmpty():
            return -1

        while self.__q1.qsize() > 1:
            self.__q2.put(self.__q1.get())

        ans = self.__q1.get()
        self.__q2.put(ans)

        self.__q1,self.__q2=self.__q2,self.__q1

        return ans

    def getSize(self):
        return self.__q1.qsize()

    def isEmpty(self):
        return self.__q1.qsize() == 0


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
