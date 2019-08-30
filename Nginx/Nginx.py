#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Nginx.NginxDirectoryTraversalVulnerability
import Nginx.NginxCRLFInjectionVulnerability
import ClassCongregation

def Main(Url,FileName,Values):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=Nginx.NginxDirectoryTraversalVulnerability.NginxDirectoryTraversalVulnerability(Url,RandomAgent)
        WriteFile.Write(Medusa)
    except:
        print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Nginx.NginxCRLFInjectionVulnerability.NginxCRLFInjectionVulnerability(Url,RandomAgent)
        WriteFile.Write(Medusa)
    except:
        print("[-]NginxCRLFInjectionVulnerability Scan error")

    #最后该类扫描结束输出结果语句
    SanOver="Nginx Scan completed"
    WriteFile.Write(SanOver)
