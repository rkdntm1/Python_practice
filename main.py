# 과제) 목록에 어떤 알파벳이 있는지 소스 짜오기

# ('hong', 'kim', 'lee','park','kim') -> 알파벳 만

# 중복 없는 리스트 형태로 변경
def make_list(*arr):
    irum = []
    for item in arr:
        if item not in irum:  # 중복 없애주기
            irum.append(item)
    return irum


# 리스트안의 내용을 합쳐서 str 형태로 변경해주기
def strchanger(lst):
    k = ''
    for i in range(len(t1)):
        k += t1[i]
    return k


# str 형에서 중복 없이 알파벳 단위로 뽑아 내는 함수
def alpha(str):
    mas = []
    for j in range(len(str)):
        if str[j] not in mas:  # 중복 없애주기
            mas += str[j]
    return mas


t1 = make_list('hong', 'kim', 'lee', 'park', 'kim')  # make_list 함수 호출
p = strchanger(t1)  # strchanger 함수 호출
f = alpha(p)  # aplpha 함수 호출
f.sort()
print(f)  # 결과 출력



