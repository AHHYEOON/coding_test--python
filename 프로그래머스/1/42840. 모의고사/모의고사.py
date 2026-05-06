def solution(answers):
    answer = []
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for i, ans in enumerate(answers):
        if pattern1[i % len(pattern1)] == ans:
            score[0] += 1
        if pattern2[i % len(pattern2)] == ans:
            score[1] += 1
        if pattern3[i % len(pattern3)] == ans:
            score[2] += 1
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)
    return answer