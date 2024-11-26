def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        result = 0 # 약수 개수 
        
        for j in range(1, int(i**0.5) + 1): # range(a,b) a ~ b-1 까지 반복하므로 +1해야 약수에 자기자신 포함 가능
            if(j * j == i):
                result += 1 # 제곱근이면 짝이 없으므로 +=1
            elif(i % j == 0): # i를 1~제곱근 근사치 까지 나눌 때 나눠지면 약수  
                result += 2 # 제곱근까지 구하면 이후 약수들은 구한 약수들과 짝이 되므로 +=2 
        
        if(result % 2 == 0):
            answer += i
        else: 
            answer -= i
            
    return answer