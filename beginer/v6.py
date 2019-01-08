def counting_numbers():
    i = 1
    while True:
       yield i
       i += 1
def check_power(N, k):
    if N <= 0 or k <= 0:
        raise ValueError("N and k should be greater than 0")
    if k == 1:  
         return N == 1 
    for i in counting_numbers():
        x = k ** i
        if x == N :
           return True
        elif x > N:
           return False
