# Uyga vazifa 7 
# 1 - masala

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(1))  
print(is_prime(7)) 



# 2 - masala

def digit_sum(k):
    summa = 0
    for raqam in str(k):
        summa += int(raqam)
    return summa


print(digit_sum(24))   
print(digit_sum(502))  


# 3 - masala

def power_of_two(N):
    k = 1
    while 2**k <= N:
        print(2**k, end=" ")
        k += 1


power_of_two(10)
