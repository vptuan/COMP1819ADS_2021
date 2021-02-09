

# Exercise 3 and 4


from queue import Empty


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()  # remove last item from list

    def reverse(self):
        if self.is_empty():
            return Empty('Stack is empty')

        items = []
        while self._data:
            items.append(self._data.pop())
        for item in items:
            self._data.append(item)

        print(f"Reverse stack: {self._data}")

    # it will display true if usage of brackets is correct if not False
    def parentheses_valid(self, brackets):
        p_char = {"(": ")", "{": "}", "[": "]"}
        lst = ArrayStack()
        for parentheses in brackets:
            if parentheses in p_char:
                lst.push(parentheses)
            elif len(lst) == 0 or p_char[lst.pop()] != parentheses:
                return False
        return len(lst) == 0


if __name__ == '__main__':
    S = ArrayStack()  # contents: [ ]
    S.push(1)
    S.push(2)
    S.push(3)
    print(S._data)
    print(S.reverse())
    S.push('( )')
    exp = '()(()){([()])}'
    print(exp, S.parentheses_valid(exp))
    exp = '({[])}'
    print(exp, S.parentheses_valid(exp))
    exp = '((()(()){([()])}))'
    print(exp, S.parentheses_valid(exp))    
    exp = ')(()){([()])}'
    print(exp, S.parentheses_valid(exp))    
    exp = '('
    print(exp, S.parentheses_valid(exp))
    exp = ')'
    print(exp, S.parentheses_valid(exp))
    exp = '{)'
    print(exp, S.parentheses_valid(exp))
    exp = '[(5+x)-(y+z)]'
    print(exp, S.parentheses_valid(exp)) 
    
# Exercise 6
class ArrayQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def print_queue(self):
        for i in self.items:
            print(i, end=" ")
        print("")


def reverse_queue(queue):
    # Base case
    if (queue.is_empty()):
        return

    # Dequeue current item (from front)
    data = queue.front()
    queue.pop()

    # Reverse remaining queue
    reverse_queue(queue)

    # Enqueue current item (to rear)
    queue.add(data)


# Driver Code
q = ArrayQueue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
reverse_queue(q)
q.print_queue()

