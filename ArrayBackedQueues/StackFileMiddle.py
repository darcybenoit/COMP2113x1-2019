# This is an exmaple of an array-backed stack as done in class. 

class StackMiddle:
    def __init__(self):
        self.a = [0]
        self.n = 0

    # Here we insert the item into the stack. We extend the list by 1, and then shuffle as needed to get the
    # item in place. 
    def insert(self,i,x):
        if (self.n + 1 > len(self.a)):
            self.a.append(x)
            for j in range(self.n,i-1, -1):
                self.a[j] = self.a[j-1]
            self.a[i] = x
        else:
            self.a[self.n] = x
        self.n += 1

    # Remove the item from the list from the appropriate location
    def remove(self,i): #i is index
        print ("Removing from the list: ", self.a[i])
        for j in range(i,self.n-1):
            self.a[j] = self.a[j+1]
        self.n -= 1
        self.a[self.n] = " "
        return self.a

    # Here we pop the end item off of the stack. We modify the value of n, and will overwrite this data later.
    def pop(self):
        x = self.a[self.n-1]
        self.n -= 1
        return x


    # This simply returns the list as-is, so that we can print it.
    def showList(self):
        return self.a
