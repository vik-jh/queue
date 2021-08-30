
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

class StackUsingQueue:
    def __init__(self,s1):
        self.s1=[]

def reverseQueue(inputQueue) :
    if inputQueue.qsize()<=1:
        return 
    ans=inputQueue.get()
    reverseQueue(inputQueue)
    inputQueue.put(ans)
    
    
    
  
    # Your code goes here



'''-------------- Utility Functions --------------'''



def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1