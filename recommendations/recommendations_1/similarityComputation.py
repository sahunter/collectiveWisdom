from math import sqrt
#计算图上Toby和LaSalle之间的距离
t1 = sqrt(pow(4.5-4,2)+pow(1-2,2))
print(t1)
#t2表示偏好越相近越大，为防止分母为0，在分母加1
t2 = 1/(1+sqrt(pow(4.5-4,2)+pow(1-2,2)))
print(t2)

