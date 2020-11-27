# arr =[10,20,30,40]
#for index in arr:
    #print(index)

#name = 'hong gil dong'
#print(len(name)) #길이

# data ='hello python'
# print(len(data))
#
# for index in data:
#     print(index, end =" ")
#
# print('\n=================================')
# for i in range(len(data)):
#     print(data[i], end = ' ')
#
# print('\n=================================')
# #capitalize #첫문자를 대문자로 나머지 소문자
# # a='hello python'
# # #b='hello python'
# # b=a.capitalize()
# # print(a)
# # print(b)
# # print(a==b)
# # print(a is b) #'Hello python'이라는 새로운 메모리가 만들어지므로 False
#
# print('\n=================================')
# #count #어떤 문자를 해당 객체에서 찾을때
# #찾을 문자, 시작위치, 끝위치(끝위치는 포함이 안됨)
# a='hello python'
# b=a.count('o') #o 가 몇번 나왔는가?
# c=a.count('o', 4) # o 가 4번째부터 몇번 나왔는가?
# d=a.count('o', 7, 10)  # o 가 7번째부터 10직전까지 몇번이 나왔는가?
# print(a)
# print(b)
# print(c)
# print(d)
#
# print('\n=================================')
# #endswith   #끝나는거 찾을때 보통 확장자 찾을때 주로 쓰일듯
# file_name ='hello.txt'
# result = file_name.endswith('txt')
# print(result)
#
# #help() #help(함수이름)
# help(str.count)

# #find #위치정보 #값이 없을경우 -1 로 값이 나옴
# fruit= 'banana'
# print(fruit.find('n'))
# print(fruit.find('n', 3))
# print(fruit.find('m', 3, 4))

#index #find와 비슷하지만 값이 없을경우 ValueError를 발생시킴

# data = 'hong gil dong'
# print(data.index('g')) #3
# print(data.index('g',4)) #5
# print(data.index('g', 6, 13)) #12
# print(data.index('g', 6, 12)) #12번째를 포함 하지않으므로 값 x - > 오류발생


# #replace  #일부자료들을 대체할때 사용
#
# name = 'hong gil dong'
# new_name = name.replace('g', '##')
# print(name)
# print(new_name)
# new_name2 = name.replace('g', '!!', 2)#앞의 2번만 바꿈
# print(new_name2)

# #strip lstrip rstrip
# #공백제거
# a ="          aaaaaaabbbbbbbaaaaaaa          "
# print('*******{0}******'.format(a))
# print(("********{0}*****".format(a.strip()))) #공백 다제거
# print('*********{0}******'.format(a.lstrip()))# 왼쪽 공백 제거
# print('********{0}******'.format(a.rstrip()))# 오른쪽 공백 제거
# print('===============================================')
# print('********{0}******'.format(a.strip().strip('a')))#공백시키고 그 메모리에 다시 밖에서 'a'라는 값을 제거
# print('********{0}******'.format(a.strip('a')))#밖에서 'a'라는 값을 제거해야하는데 없어서 제거가 안됨

# #join
# #literable이 있을떄 해당 데이터들을 연결시킬때 쓰임
# t1 = ':'.join(['a1', 'a2', 'a3', 'a4'])
# print(t1)
# print(type(t1))

# #split
# #문자열을 나누어주고 리스트 타입으로 변경
# t1 = 'aaa bbb ccc ddd'
# print(type(t1))
# result = t1.split() #공백을 기준으로 split - > 리스트 타입으로 변경
# print(result)
# print(type(result))
#
# print("=============================")
# t2 = 'aaa,bbb,ccc,ddd'
# result2 = t2.split(',') #,를 기준으로 split -> 리스트타입으로 변경
# print(result2)
# print(type(result2))
#
# t3='aaa;bbb;ccc;ddd'
# test = t3.split(';', maxsplit=2) #두번을 기준으로 짜름 maxsplit = 2
# print(test)
