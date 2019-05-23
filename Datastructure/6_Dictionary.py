# 딕셔너리 변수 생성
dic = {} # or dict()

# 딕셔너리 쌍 추가
dic = {1: 999, 2: 888}
dic[10] = "안녕하세요"
dic["33"] = "반갑습니다"

# 요소 제거
del dic[1]
del dic[2]

# 딕셔너리 안에 요소가 있는지 검사
if 1 in dic:
    print("있을리가 없을탠데!")

# 출력
print(dic[10], dic["33"]) # output > 안녕하세요 반갑습니다