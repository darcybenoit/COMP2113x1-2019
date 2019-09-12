# This is an example of being able to use multiple stacks in the same program.
# We test the push/pop for each Stack, making sure to interleave them so that we can see that they are independent.
import Stack

stackA = Stack.Stack()
stackB = Stack.Stack()

print("StackA.push(25)")
stackA.push(25)
print("StackA.push(442)")
stackA.push(442)
print("StackA.push(20)")
stackA.push(20)


print("\nStackB.push(100)")
stackB.push(100)

print("\nstackA.pop() ", stackA.pop())
print("stackA.pop() ", stackA.pop())
print("stackA.pop() ", stackA.pop())


print("\nstackB.pop() ", stackB.pop())
