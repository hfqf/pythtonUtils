
 # coding=UTF-8
 # @Date : 2019/12/24
 # @Author : Points
 # @Description:  自动git clone所有本地pods库,pod install，并自动打开工程
import sys
import os
import subprocess
#from git import Repo
import shutil
import socket

#指定私有库下载目录
localPodsFilePath = "./xx"

#clean local pods document
def cleanLocalPodsFile():
  if os.path.exists(localPodsFilePath):
    print("localPodsFilePath has created!")
    shutil.rmtree(localPodsFilePath)
    print("localPodsFilePath has deleted!")
    os.mkdir(localPodsFilePath)
    print("localPodsFilePath has created once again!")
    os.chdir(localPodsFilePath)
  else:
    os.mkdir(localPodsFilePath)
    print("localPodsFilePath has created once again!")
    os.chdir(localPodsFilePath)
    
# git clone all local pods
# because of limit of network,so put all the localpods into this file.
def gitCloneAllModules():
    print("all local pods module:")
    arrGitUrls = [
    {'git clone -b 0.1.7 http://192.168.xx.xx/xx/xx/xx/xx.git'} #一个示例仓库地址
    ]
    for url in arrGitUrls:
      print ('current url:', url)
      archiveProcessRun = subprocess.Popen(url,shell=True)
      archiveProcessRun.wait()

def podinstall():
    archiveProcessRun = subprocess.Popen('pod install',shell=True)
    archiveProcessRun.wait()

   #auto open .xcworkspace   
def openWorkSpace():
    os.chdir('../')
    archiveProcessRun = subprocess.Popen('open 【自己工程名】.xcworkspace',shell=True)
    archiveProcessRun.wait()

cleanLocalPodsFile()
gitCloneAllModules()
podinstall()
openWorkSpace()

