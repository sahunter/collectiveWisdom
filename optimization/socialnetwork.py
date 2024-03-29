import math
import Image
import ImageDraw
import optimization
people=['Charlie','Augustus','Veruca','Violet','Mike','Joe','Willy','Miranda']
links=[('Augustus','Willy'),
       ('Mike','Joe'),
       ('Miranda','Mike'),
       ('Violet','Augustus'),
       ('Miranda','Willy'),
       ('Charlie','Mike'),
       ('Veruca','Joe'),
       ('Miranda','Augustus'),
       ('Willy','Augustus'),
       ('Joe','Charlie'),
       ('Veruca','Augustus'),
       ('Miranda','Joe')]
def crosscount(v):
    #将数字序列转换成一个person:(x,y)的字典
    loc = dict([(people([i],(v[i*2],v[i*2+1])))for i in range(0,len(people))])
    total = 0
    #遍历每一对连线
    for i in range(len(links)):
           for j in range(i+1,len(links)):
                  #获取坐标位置
                  (x1,y1),(x2,y2)= loc[links[i][0],loc[links[i]][1]]
                  (x3,y3), (x4, y4) = loc[links[j][0], loc[links[j]][1]]
                  den = (y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)



def drawnetwork(sol):
    #建立image对象
    img = Image.new('RGB',(400,400),(255,255,255))
    draw = ImageDraw.Draw(img)

    #建立标示位置信息的字典
    pos = dict([(people(i),(sol[i*2],sol[i*2+1])) for i in range(0,len(people))])
    #绘制连线
    for (a,b) in links:
           draw.line((pos[a],pos[b]),fill=(255,0,0))
    #绘制代表人的结点
    for n,p in pos.items():
           draw.text(p,n,(0,0,0))
    img.show()
sol = optimization.randomoptimize(domain)



























