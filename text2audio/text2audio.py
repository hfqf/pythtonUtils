# coding=UTF-8
# @Date : 2020/03/26
# @Author : Points
# @Description:  自动生成iOS离线语音包文件(500以内的语音播报)
# @Company: com.huiyinxun
#!coding=utf-8
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
import os
import shutil
import urllib
import urllib2
import json
print os.getcwd()
mp3Path = "./mp3"

MAX = 4
#检测mp3文件夹
def checkMp3Path():
    if os.path.exists(mp3Path):
        print("mp3Path has existed!")
#        shutil.rmtree(mp3Path)
#        print("mp3Path has deleted!")
#        os.mkdir(mp3Path)
#        print("mp3Path has created once again!")
    else:
        os.mkdir(mp3Path)
        print("mp3Path has created!")

#获取百度text2Audio的token,所需的client_id和client_secret去百度语音官网注册即可
def getBaiduToken():
    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=gleXhGxXDtLTVYE6pza08hFA&client_secret=DzbPFSuTXBrOcyFI12WIMHZazYWkNS3D'
    rq = urllib2.Request(url)
    rs = json.loads(urllib2.urlopen(rq).read())
    return rs['access_token']

#下载mp3文件
def text2Audio(input,token):
    url = 'http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=abcdxxx&tok='+token+'&tex=蓝知收款'+input+'元&vol=9&per=0&spd=5&pit=5&aue=3'
    print url
    response=urllib2.Request(url)
    rs=urllib2.urlopen(response)
    f=open(mp3Path+'/'+input+'-s.mp3','wb')
    f.write(rs.read())
    f.close()

#根据最大收款金额自动下载所需的音频文件
def startGenerate(start,max):
    token = getBaiduToken()

    arr = []
    if(start==1):
        i=1
        while(i<10):
          num1 =  "0.0%d" % i
          num2 =  "0.%d" % i
          arr.append(num1)
          arr.append(num2)
          i = i + 1

    i=start
    while(i<=max):
      j=1
      num1 =  "%d" % i
      arr.append(num1)
      while(j<10):
          num2 =  "%d.%d" % (i, j)
          arr.append(num2)
          j=j+1
      i = i + 1
    for value in arr:
        text2Audio(value,token)

checkMp3Path()
#实际情况中发现会发生连接中断的情况，可能是连接数过多导致，然后需要重新执行脚本，根据上次的最大数值，作为下次启动的start值,第一次从1开始
startGenerate(1,MAX)
