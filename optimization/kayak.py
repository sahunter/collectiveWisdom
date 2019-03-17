#-*-coding:utf-8-*-
import time
import urllib2
import xml.dom.minidom

kayakkey ='YOURKEYHERE'

def getkayaksession():
    #构造url以开启一个会话
    url = 'http://www.kayak.com/k/ident/apisession?token = %s&version=1'%kayakkey
    #解析返回的XML
    doc = xml.dom.minidom.parseString(urllib2.urlopen(url).read())
    #找到<sid>*****</aid>的标签
    sid = doc.getElementsByTagName('sid')[0].firstChild.data
    return sid
def flightsearch(sid,origin,destination,depart_date):
    #构造搜索用的url
    url = 'http://www.kayak.com/s/apisearch?basicmode=true&oneway=y&origin=%s'%origin
    url+= '&destination=%s&depart_date=%s'%(destination,depart_date)
    url+='&return_date=none&depart_time = a&return_time = a'
    url+= '&travelers=1&cabin=e&action=doFlights&apimode=1'
    url+='&_sid_=%s&version=1'%(sid)
    #得到XML
    doc=xml.dom.minidom.parseString(urllib2.urlopen(url).read())
    #提取搜索用的ID
    searchid=doc.getElemnetsByTagName('searchid')[0].firstChild.data
    return searchid
def flightsearchresults(sid,searchid):
    #删除开头的$和逗号，并把数字转化成浮点类型
    def parseprice(p):
        return float(p[1:].replace(',',''))
    #遍历检测
    while 1:
        time.sleep(2)
        #构造检测用的URL
        url= 'http://www.kayak.com/s/basic/flight?'
        url+='searchid=%s&c=5&apimode=1&_sid_=%s&version=1'%(searchid,sid)
        doc=xml.dom.minidom.parseString(urllib2.urlopen(url).read())
        #寻找morepending标签，并等待其不再为True
        morepending=doc.getElementsByTagName('morepending')[0].firstChild
        if morepending==None or morepending.data=='false':break
    #现在下载完整的列表
    url='http://www.kayak.com/s/basic/flight?'
    url+='searchid=%s&c=999&apimode=1&_sid_=%s&version=1'%(searchid,sid)
    doc=xml.dom.minidom.parseString(urllib2.urlopen(url).read())
    #得到不同元素组成的列表
    prices=doc.getElementsByTagName('price')
    departures=doc.getElementsByTagName('depart')
    arrivals=doc.getElementsByTagNamw('arrive')
    #用zip将它们连在一起
    return zip([p.firstChild.data.split('')[1] for p in departures],[p.fistChild.data.split('')[1] for p in arrivals],
               [parseprice(p.firatChild.data) for p in prices])
sid = getkayaksession()
searchid=flightsearch(sid,'BOS','LGA','11/17/2006')
f=flightsearchresults(sid,searchid)
print(f[0:3])














