#list

# a = [10,20,['a','b','c'],30,40] #리스트
# print(a)
# print(type(a)) # list

# list1 =[10,20,30,40] #[0],[1],[2],[3]
# list2 =['a','b','c','d']
# print(list1 + list2)
# result1= list1[0:2] # 0부터 2직전까지
# result2= list1[:2] # 처음부터 2직전까지
# result3= list1[1:] # 1번째부터 ~
# print(result1)
# print(result2)
# print(result3)

# list =[10,20,30,40]
# a=list[0]
# print(list)
# print(a)
# print(list[1])
#
# list[1] = 100 # list[1] 값을 100으로 변경
# print("======================")
# print(list)

# #+,* 연산
# #+ : list간 연결
# #*(숫자) : 숫자만큼 반복
#
# list1=[10, 20, 30, 40]
# list2=[1, 2, 3, 4]
# print(list1+list2)
# result = list1 + list2
# print(result)
# print(list1*2)

# #len, min, max, append
# lst = [10,20,30,50,40]
#
# print(len(lst)) #길이
# print(min(lst)) #가장 작은 값
# print(max(lst)) #가장 큰 값
# print("======================")
# lst2 = lst.append(100)
# print(lst2)
# print(lst)
#
# help(list)

# #clear extend
# a=[10,20,30,40,50,60,70]
# print(a.count(10))
# #a.clear()
# t1 = 'abc' # t1[0] = 'a' t1[1] = 'b' t1[2] = 'c'
# a.extend(t1) #글자 하나하나의 요소가 extend 됨 -> t1을 배열로 인식
# print(a)
#
# a =[10,20,30]
# b=[100,200,300]
# a.extend(b)
# print(a)

#index
#그 위치를 찾는것
# fruit =['사과', '배', '복숭아', '포도', '딸기', '포도']
# value = fruit.index('포도') # 제일먼저 만나는 포도의 위치
# value2 = fruit.index('포도', 4)
# print(value)
# print(value2)

#insert

# fruit =['사과', '배', '복숭아', '포도', '딸기', '포도']
# fruit.insert(1,'밤') #1번자리에 '밤'을 추가하고 나머지는 뒤로 밀림
# print(fruit)

#pop -pop()
# fruit =['사과', '배', '복숭아', '포도', '딸기', '포도']
# print(fruit)
# print('-------------------')
# a=fruit.pop()
# print(a)
# print('-------------------')
# print(fruit)
#
# fruit.pop()
# fruit.pop()
# fruit.pop()
# fruit.pop()
# fruit.pop()
# print(fruit)
# print('===================')
# print(fruit.pop())

#pop --- pop(index)
# fruit =['사과', '배', '복숭아', '포도', '딸기', '포도']
# t= fruit.pop(1) #1번 위치에 있는 값을 빼옴
# print(t)
# print(fruit)
#
# t2= fruit.pop(30) #오류) pop index out of range
# print(t2)
# print(fruit)


#remove
# fruit =['사과', '배', '복숭아', '포도', '딸기', '포도']
#
# fruit.remove('포도')
# print(fruit)
# #fruit.remove('옥수수') #list.remove(x): x not in list
# #help(list.remove)

#del
# a=[10,20,30,40,50]
# del a[:2] #a[2]직전까지
# print(a)

#reverse
# list=[10,40,20,60,50]
# print(list)
# list.reverse()
# print(list)
'''
cf
for index in reversed(range(5)):
    print(index)
'''

#sort
'''
fruit =['사과','바나나', '배', '파인애플', '복숭아', '포도', '딸기', '포도']

print(fruit)
fruit.sort()
print("=-===============가나다 정렬=================")
print(fruit)

print('=====================리버스 트루 설정(내림차순)=======')
fruit.sort(reverse=True)
print(fruit)

print("=======================길이로 정렬/내림차순=========================")
fruit.sort(key=len, reverse=True)
print(fruit)
'''
# data =[10,20,30,50,-10,-5,-2,-200]
# print(data)
# print('=========================')
# data.sort(key=abs) #절댓값으로 정렬
# print(data)

data =[10,20,30,50,-10,-5,-2,-200]
def fn(x):
    return x**2

data.sort(key=fn)
print(data)

