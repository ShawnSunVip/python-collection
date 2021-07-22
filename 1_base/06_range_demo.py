# 功能描述  range
# by Shawn
# 开发时间: 2021/7/22 16:56

#range(start,stop,step)

r1=range(10) #[0,1,2,3,4,5,6,7,8,9] 从0-10不包括10 步长1

print(list(r1))


r2=range(1,10) #[1, 2, 3, 4, 5, 6, 7, 8, 9]  从1-10不包括10 步长1
print(list(r2))

r3=range(1,10,2) #[1, 3, 5, 7, 9]  从1-10不包括10 步长2
print(list(r3))