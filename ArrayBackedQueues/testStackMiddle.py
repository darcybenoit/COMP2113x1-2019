# This is an example of being able to use multiple stacks in the same program.
# We test the push/pop for each Stack, making sure to interleave them so that we can see that they are independent.
import StackFileMiddle

stackA = StackFileMiddle.StackMiddle()

print("StackA.insert(0,25)")
stackA.insert(0,25)
print("StackA.insert(1,442)")
stackA.insert(1,442)
print("StackA.insert(2,20)")
stackA.insert(2,20)
print("StackA.insert(1,300)")
stackA.insert(1,300)


print("\nstackA.pop() ", stackA.pop())
print("stackA.pop() ", stackA.pop())
print("stackA.pop() ", stackA.pop())
print("stackA.pop() ", stackA.pop())


print("StackA.insert(0,25)")
stackA.insert(0,25)
print("StackA.insert(1,442)")
stackA.insert(1,442)
print("StackA.insert(2,20)")
stackA.insert(2,20)
print("StackA.insert(1,300)")
stackA.insert(1,300)

print("Here is the list: ", stackA.showList())

#include the array position of the item you want to remove.
#what happens when you try and remove an item that doesn't exist?
print("stackA.remove() ", stackA.remove(1))
print("stackA.remove() ", stackA.remove(1))

