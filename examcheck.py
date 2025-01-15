# import examCalculator

# print('과목점수입력>>')

# s1 = int(input('첫번째과목 점수입력>>'))
# s2 = int(input('두번째과목 점수입력>>'))
# s3 = int(input('세번째과목 점수입력>>'))

# print(f'과목점수 평균은 {averageScore}입니다.')

#너무길어서줄여쓰기as
# import examCalculator as exC
from examCalculator import *
#이안에있는 함수다쓸거야 from file as nickname

x = int(input('과목1>>'))
y = int(input('과목2>>'))
z = int(input('과목3>>'))
# tot = examCalculator.totalScore(x,y,z)
print(totalScore(x,y,z))
print(averageScore(x,y,z))
