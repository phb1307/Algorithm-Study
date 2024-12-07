def solution(players, callings):
    answer = []
    
    dictionary = {string : i for i, string in enumerate(players)}
    
    for calling in callings: 
        rank = dictionary[calling] # 추월한 선수의 현재 랭킹 
        loserPlayer = players[rank - 1] # 추월당한 선수
        winnerPlayer = players[rank] # 추월한 선수
        
        # 리스트 랭킹 변경
        players[rank - 1], players[rank] = players[rank], players[rank - 1] # swap
        
        # 딕셔너리도 랭킹 변경 
        dictionary[loserPlayer] += 1
        dictionary[winnerPlayer] -= 1
        
    answer = players 
    
    return answer