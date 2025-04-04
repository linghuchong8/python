"""
计算n的阶乘

5 * 4 * 3 * 2 * 1 == 5! == 5 * 4!
    4 * 3 * 2 * 1 == 4! == 4 * 3!
        3 * 2 * 1 == 3! == 3 * 2!
        
                1 == 1! == 1
"""

def calc(n):
    if n == 1:
        return 1
    
    return n * calc(n - 1)
    

print(calc(5))