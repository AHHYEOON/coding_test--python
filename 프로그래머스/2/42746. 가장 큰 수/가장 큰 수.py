def solution(numbers):
    numbers_str = list(map(str,numbers))
    
    numbers_str.sort(key=lambda x : x*3, reverse=True)
    
    result = ("".join(numbers_str))
    
    if result[0] == '0':
        return '0'
    return result