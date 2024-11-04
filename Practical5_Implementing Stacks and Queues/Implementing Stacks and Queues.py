class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  
print(stack.peek())  
print(stack.size())  

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.front())  
print(queue.size())  

def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

print(is_balanced("((()))"))  
print(is_balanced("(()"))

def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

print(reverse_string("Hello, World!"))  

def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  

class Stack:
    def _init_(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(int(operand1 / operand2))
    return stack.pop()

class QueueUsingStacks:
    def _init_(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

from collections import deque

class TaskScheduler:
    def _init_(self):
        self.task_queue = deque()

    def add_task(self, task_name):
        self.task_queue.append(task_name)
        print(f"Task '{task_name}' added to the scheduler.")

    def process_tasks(self):
        print("\nStarting task processing...")
        while self.task_queue:
            current_task = self.task_queue.popleft()
            print(f"Processing task: {current_task}")
        print("All tasks have been processed.")

print(evaluate_postfix("2 3 +")) 
print(evaluate_postfix("5 1 2 + 4 * + 3 -")) 

queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) 
print(queue.dequeue())  

scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.process_tasks()


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = Stack()
    postfix = []
    
    for token in expression.split():
        if token.isdigit():  
            postfix.append(token)
        elif token == '(':  
            stack.push(token)
        elif token == ')': 
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else: 
            while (not stack.is_empty()) and (precedence[stack.items[-1]] >= precedence[token]):
                postfix.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return ' '.join(postfix)

print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  
print(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"))