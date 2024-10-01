a = 0
max_a = 0 
psg = 0 # 열차 내 현재 승객 수를 저장할 변수 초기화

for i in range(10):
    out_a, in_a = map(int, input().split()) # 하차 승객, 승차 승객 수 입력받기
    psg += (in_a - out_a) # 현재 승객 수 업데이트
    max_a = max(psg, max_a) # 퇴대 승객 수 업데이트
print(max_a)
