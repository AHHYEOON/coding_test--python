def solution(array, commands):
    answer = []
    p = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        p = array[i-1:j]
        p.sort()
        answer.append(p[k-1])
    return answer