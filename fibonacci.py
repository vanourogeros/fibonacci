import time

#def fib_recursive(target, initial, in_value):

def fib_memoization(n, dictionary):
  if n in dictionary.keys():
      return dictionary[n]
  else:
      dictionary[n] = fib_memoization(n - 1, dictionary) + fib_memoization(n - 2, dictionary)
      return dictionary[n]

def fib_iterative(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = b
        b = a + b
        a = c
    return b

def matrix_pow(A, n):
    #for 2x2 matrices
    R = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            a = R[0][0] * A[0][0] + R[0][1] * A[1][0]
            b = R[0][0] * A[0][1] + R[0][1] * A[1][1]
            c = R[1][0] * A[0][0] + R[1][1] * A[1][0]
            d = R[1][0] * A[0][1] + R[1][1] * A[1][1]
            R = [[a, b], [c, d]]
        n //= 2    
        a = A[0][0] * A[0][0] + A[0][1] * A[1][0]
        b = A[0][0] * A[0][1] + A[0][1] * A[1][1]
        c = A[1][0] * A[0][0] + A[1][1] * A[1][0]
        d = A[1][0] * A[0][1] + A[1][1] * A[1][1]
        A[0][0] = a
        A[0][1] = b
        A[1][0] = c
        A[1][1] = d
    return R    


def fib_matrix(n):
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    M = matrix_pow(F, n - 2)
    return M[0][0] + M[0][1]

def fib_GoldenRatio(n):
    phi = (1 + 5**0.5)/2
    F = (phi**n - (1 - phi)**n)/(5**0.5)
    return F

d = {0 : 0, 1 : 1}
n = 0
while n != -1:
    time_report = ""
    n = int(input("Give the number of the nth term of the Fibonacci Sequence you want to find (input -1 to exit): "))
    if n < 0:
        break
    time_a = time.time()
    print("Calculation with iterative method: {}".format(fib_iterative(n)))
    time_b = time.time()
    time_report += "Calculation time with iterative method was {} seconds\n".format(time_b - time_a)
    print("Calculation with matrix method: {}".format(fib_matrix(n)))
    time_c = time.time()
    time_report += "Calculation time with matrix method was {} seconds\n".format(time_c - time_b)
    try:        
        print("Calculation with memoization method: {}".format(fib_memoization(n, d)))
        time_d = time.time()
        time_report += "Calculation time with memoization method was {} seconds\n".format(time_d - time_c)
    except:
        print("Number too large to use recursive method")  
    try:
        time_e = time.time()
        print("Approximation with Golden Ratio relationship: {}".format(fib_GoldenRatio(n)))
        time_f = time.time()
        time_report += "Calculation time with Golden Ratio method was {} seconds\n".format(time_f - time_e)
    except:
        print("Golden Ratio Method resulted in overflow")    

    print(time_report)    
    
