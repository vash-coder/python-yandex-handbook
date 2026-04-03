number_1 = int(input())
number_2 = int(input())

a_1 = number_1 // 100
a_2 = number_1 // 10 % 10
a_3 = number_1 % 10

b_1 = number_2 // 100
b_2 = number_2 // 10 % 10
b_3 = number_2 % 10

c_1 = (a_1 + b_1) % 10
c_2 = (a_2 + b_2) % 10
c_3 = (a_3 + b_3) % 10

answer = c_1 * 100 + c_2 * 10 + c_3
print(answer)