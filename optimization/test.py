import time
def getminutes(t):
    x = time.strptime(t,'%H:%M')
    return x[3]*60 + x[4]

print(getminutes('7:39'))

r = [3,6,8,9]
s = r[3:3]
print(s)
domain = [(0,9)]*12
