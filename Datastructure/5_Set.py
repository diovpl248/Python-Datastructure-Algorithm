# 중복없는 다료를 저장할때 사용하는 집합 자료구조이다.
# C++ STL의 set처럼 정렬되진 않는다.

# 집합 선언
s = set()

# 원소 하나 추가
s.add(20)

# 원소 여러개 추가
s.update([20,5,10])

# 값 제거
s.remove(5)

print(s) # output > {10, 20}

# 리스트로 변환해야 참조가능
l = list(s)

print(l[0], l[1]) # output > 10 20