# Find a power of two numbers using divide and conquer

def DAC_power(a,n):
    if n == 1:
        return a
    else:
        mid = n // 2
        b = DAC_power(a, mid)
        c = b * b

        if n % 2 == 0:
            return c
        else:
            return c*a
    
    

results = DAC_power(2,7)
print(results)