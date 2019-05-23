import heapq

# 힙으로 사용할 리스트
heap = []

# 원소 삽입 (힙의 리스트, 튜플(우선순위, 데이터))
# O(logN)
heapq.heappush(heap, (3, "파일닫기"))
heapq.heappush(heap, (1, "파일열기"))
heapq.heappush(heap, (2, "파일작성"))

# 원소 반환 및 제거
# O(logN)
for i in range(len(heap)):
    print(i+1, heapq.heappop(heap))
    # output
    # > 1 (1, '파일열기')
    # > 2 (2, '파일작성')
    # > 3 (3, '파일닫기')

# 기본적으로 최소힙만 지원하고, 최대힙을 만드려면 우선순위를 음수값으로 줘서 한다.