class ArrayStack:
    def __init__(self):
        self.item = []
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def get_stack(self):
        return self.item

if __name__ == '__main__':
    print("--------------------------------------LAB 03  TASK 3 -----------------------------------")
    s = ArrayStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.get_stack())
    print(s.pop())
    print(s.pop())
    print(s.pop())


    print("--------------------------------------LAB 03  TASK 4 -----------------------------------")

# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Incorrect"
    if len(stack) == 0:
        return "Correct"
    else:
        return "Incorrect"

string = " [(5+x)-(y+z)]"
print(string, "-", check(string))


