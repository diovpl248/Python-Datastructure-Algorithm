# 리스트를 스택으로 활용한다.

stack = []

# 원소 추가
stack.append(10) # stack => [10]
stack.append(20) # stack => [10, 20]

# 원소 제거및 반환
stack.pop() # return 20, stack => [10]
stack.pop() # return 10, stack => []
