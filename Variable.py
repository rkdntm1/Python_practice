#변수
#애완동물을 소개해주세요.
animal = "고양이"
name = "냥냥이" #문자형 자료
age = 4 #정수형 자료
hobby = "간식을"
is_adult = age >= 3 #boolean

print("우리집 " + animal + "의 이름은 "+ name + "이에요")
hobby = "공놀이" #밑에 바로 적용
#print(name + "는 " +str(age)+ "살이며,"+ hobby +" 아주 좋아해요") #str->정수형을 문자형으로 출력
print(name, "는 " ,age, "살이며,", hobby ," 아주 좋아해요") # ','로도 가능하지만 띄어쓰기가 포함됨
print(name + "는 어른일까요?" + str(is_adult)) #boolean형도 똑같이 str로