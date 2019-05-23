from collections import deque

# 큐 생성
q = deque() # q => []
q = deque([10,20]) # q => [10, 20]

# 큐에 원소 추가
q.append(30) # q => [10, 20, 30]
q.append(40) # q => [10, 20, 30, 40]

# 큐에서 원소 제거 및 반환
q.popleft() # return 10, q => [20, 30, 40]
q.popleft() # return 20, q => [30, 40]