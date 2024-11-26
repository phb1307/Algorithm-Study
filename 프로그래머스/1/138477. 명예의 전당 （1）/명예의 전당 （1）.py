def solution(k, score):
    answer = []
    
    arr = [] # 명예의 전당 배열
    
    for scoreIdx, scoreItem in enumerate(score):
        if len(arr) >= k: # 명예의 전당 길이 k 넘을 경우
            for arrIdx, arrItem in enumerate(arr): 
                if arrItem <= scoreItem: # 점수가 내림차순 정렬된 명예의 전당 배열 값보다 큰지 차례대로 확인  
                    arr.append(scoreItem)
                    arr.sort(reverse=True)
                    del arr[-1]
                    answer.append(arr[-1])
                    break
                else: 
                    if arrIdx + 1 == k: # 내림차순 정렬된 명예의 전당 마지막 배열 값보다 점수가 작다면  
                        answer.append(arr[-1])
        
        else: # 명예의 전당 길이 k까지는 무조건 추가 
            arr.append(scoreItem)
            arr.sort(reverse=True)
            answer.append(arr[-1])

    return answer