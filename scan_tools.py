import socket,os,time,sys
from whois import whois



#域名查IP
def ip_check(url):
    ip=socket.gethostbyname(url)
    print(ip)

#判断是否存在cdn
def cdn_check(url):
#cdn_date=os.system('nslookup')
#os.system 只能输出不能进行后面的解析
    cdn_data=os.popen('nslookup '+url)
    cdn_datas=cdn_data.read()
    dot = cdn_datas.count('.')
    if dot > 10:
        print("cdn exist")
    else:
        print("cdn no exist")


#扫描端口
def port_check(url):
    ports={'21','22','80','135','443','1433','3389','3306','8000'}
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #申请一个socket变量
    for port in ports:
        result=server.connect_ex(('220.181.38.148',int(port)))
        if result==0:
            print(port + '|open')
        else:
            print(port + '|close')

# #域名反查IP
def whois_check(url):
    data=whois(url)
    print(data)
def zym_check(url):
    urls=url.replace('www','')
    #将www替换为空
    for zym_data in open('dic.txt'):
        zym_data=zym_data.replace('\n','')
        url=zym_data+urls
        try:
            ip=socket.gethostbyname(url)
            print(url+'->'+ip)
            time.sleep(0.1)
        except Exception as  e:
           pass

if __name__ == '__main__':
    check=sys.argv[1]
    urls=sys.argv[2]
    if check=='-u':
        ip_check(urls)
    if check == '-c':
        cdn_check(urls)
    if check=='-p':
        port_check(urls)
    if check=='-w':
        whois_check(urls)
    if check=='-d':
        zym_check(urls)
    if check=='-A':
        ip_check(urls)
        cdn_check(urls)
        port_check(urls)
        whois_check(urls)
        zym_check(urls)



