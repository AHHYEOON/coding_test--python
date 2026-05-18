from itertools import product

def solution(numbers, target):
    count = 0 
    
    for signs in product([1, -1], repeat = len(numbers)):
        total = 0 
        for i in range(len(numbers)):
            total += signs[i] * numbers[i]
        if total == target:
            count += 1
            
    return count