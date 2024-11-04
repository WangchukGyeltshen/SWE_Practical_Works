def fib_itr(n) :
    if n < 0 :
        return []
    elif n == 0 :
        return [0]
    elif n == 1 :
        [0 , 1]
        
    fib_sequence = [0, 1] 
    for _ in range(2, n + 1):
        next_fib = fib_sequence[-1] + fib_sequence[-2] 
        fib_sequence.append(next_fib) 
    return fib_sequence
n = 10 
print(f"Fibonacci sequence up to {n}: {fib_itr(n)}")


def index_of_first_fib_exceeding(value):
    if value < 0:
        return 0 

    a, b = 0, 1  
    index = 1  

    while b <= value:
        a, b = b, a + b  
        index += 1  
    return index
print(index_of_first_fib_exceeding(13))



def is_fibonacci_number(x):
    if x < 0:
        return False  
    a, b = 0, 1  
    
    while b < x:
        a, b = b, a + b   


    return b == x


print(is_fibonacci_number(13)) 



def fibonacci_ratios(n):
    a, b = 0, 1  
    for _ in range(n):
        if a != 0 :  
            ratio = b / a
            print(f"Ratio of {b} / {a} = {ratio}")
        a, b = b, a + b 

fibonacci_ratios(100)