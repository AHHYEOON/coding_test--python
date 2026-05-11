def solution(n):
    answer = list(str(n))
    k = answer[::-1]
    int_list = [int(x) for x in k]
    return int_list