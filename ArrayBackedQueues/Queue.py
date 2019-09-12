# This is an example of a queue, where items can be inserted and removed in the middle of
# the queue. (As a class example, this is a priority queue. We discussed this after we
# looked at the implementation of a stack.)

class Queue:
    def __init__(self, name):
        self.a = [0]
        self.n = 0
        self.name = name

    # inserting an item into the queue at a particular location
    def insert(self,i,x): #i is index, x is value
        if (self.n + 1 > len(self.a)):
            self.a.append(x)
            for j in range(self.n,i-1,-1):
                self.a[j] = self.a[j-1]
            self.a[i] = x
        else:
            self.a[self.n] = x
        self.n += 1
        print (self.name, self.a)

    # removing an item from the queue at a particular location
    def remove(self,i): #i is index
        for j in range(i,self.n-1):
            print (self.name, self.a)  # printing so we can see what is going on.
            self.a[j] = self.a[j+1]
        self.n -= 1
        self.a[self.n] = " "
        return self.a
