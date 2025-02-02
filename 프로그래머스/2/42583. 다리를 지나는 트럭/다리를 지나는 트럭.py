from collections import deque
def solution(bridge_length, weight, truck_weights):

    # 다리 지나는 트럭 무게 합
    tmp_weights_sum = 0;
    
    # 다리 길이 배열
    # bridge = [0] * bridge_length;
    bridge = [0 for i in range(bridge_length)]
    
    # 다리 큐 생성
    bridge_queue = deque();
    
    # 다리 큐 삽입
    for i in bridge:
        bridge_queue.append(i);
    
    # 트럭 무게 큐 생성 
    truck_weights_queue = deque(); 
    
    # 트럭 무게 큐 삽입
    for truck_weight in truck_weights:
        truck_weights_queue.append(truck_weight);
        
    # 최소 시간
    second = 0;
    
    # 큐 빌 때까지 반복
    while truck_weights_queue:
        # 한 번 움직일 때마다 1초 경과
        second += 1;
        
        # 다리 큐 반환
        tmp_weights_sum -= bridge_queue.popleft()
        
        # 다리 위 트럭 무게와 진입할 트럭의 무게 합이 다리가 견딜 수 있는 무게보다 적다면 
        if tmp_weights_sum + truck_weights_queue[0] <= weight:
            tmp_weights_sum += truck_weights_queue[0]
            bridge_queue.append(truck_weights_queue.popleft())
        else:
            bridge_queue.append(0)
        
    second += bridge_length
        
    return second