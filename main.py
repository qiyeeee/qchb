import requests
import requests.utils
from bs4 import BeautifulSoup
import random


def show_exit(content):
    """
    输出错误原因，辅助退出
    """
    input(content)
    exit()


def get_openid():
    count = 0;
    st = "oADCC6"  # 设定前缀
    s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
         'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5',
         '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z'];  # 'a','b','c','d','e','f','g','h','c'
    while (count < 22):
        i = random.randint(0, len(s))
        if (i >= 0 and i < len(s)):
            st += s[i];
            count += 1;
    return st


def get_image(s, code, course):
    headers = {
        "Host": "h5.cyol.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; PACM00 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3164 MMWEBSDK/20211001 Mobile Safari/537.36 MMWEBID/556 MicroMessenger/8.0.16.2040(0x28001056) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/tpg,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "com.tencent.mm",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    url = 'https://h5.cyol.com/special/daxuexi/' + code + '/images/end.jpg'
    resp = s.get(url, headers=headers)
    img_path = course + '.jpg'
    f = 0;
    with open(img_path, 'wb') as fp:
        fp.write(resp.content)
        f = 1
    if (f == 1):
        print("图片获取成功")
    else:
        print("图片获取失败")


def get_code(s):
    """
    调用API获取最新一期青春学习的CODE
    :return:
    """
    url = "https://h5.cyol.com/special/weixin/sign.json"
    headers = {
        "Host": "h5.cyol.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; PACM00 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3164 MMWEBSDK/20211001 Mobile Safari/537.36 MMWEBID/556 MicroMessenger/8.0.16.2040(0x28001056) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Origin": "http://h5.cyol.com",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    resp = s.get(url, headers=headers).json()
    return list(resp)[-1]


def get_course(s, code):
    headers = {
        "Host": "h5.cyol.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; PACM00 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3164 MMWEBSDK/20211001 Mobile Safari/537.36 MMWEBID/556 MicroMessenger/8.0.16.2040(0x28001056) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/tpg,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "com.tencent.mm",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    url = 'https://h5.cyol.com/special/daxuexi/' + code + '/m.html'
    resp = s.get(url, headers=headers)
    soup = BeautifulSoup(resp.content.decode("utf8"), "lxml")
    course = soup.title.string[7:]
    return course


def save_door(course, s, school, name, clas, dept):
    """
    调用API提交用户进入页面信息至青春湖北数据库
    :param info:
    :return:
    """
    headers = {
        "Host": "cp.fjg360.cn",
        "Connection": "keep-alive",
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; PACM00 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3164 MMWEBSDK/20211001 Mobile Safari/537.36 MMWEBID/556 MicroMessenger/8.0.16.2040(0x28001056) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    url = "https://cp.fjg360.cn/index.php?m=vote&c=index&a=save_door&sessionId=&imgTextId=&ip="
    # url += get_ip()
    url += "&username=" + name
    url += "&phone=" + "未知"
    url += "&city=" + school  # info["danwei1"]湖北经济学院法商学院
    url += "&danwei2=" + clas  # info["danwei3"]班级
    url += "&danwei=" + dept  # info["danwei2"]系部
    url += "&openid=" + get_openid()  # 随机的openid
    url += "&num=10"
    url += "&lesson_name=" + course  # 大学习第几期
    resp = s.get(url, headers=headers).json()
    if resp.get("code") == 1:
        print("%s %s %s True" % (name, clas, dept))
        return True
    else:
        show_exit("您的用户信息有误，请检查后重试")


def run():
    s = requests.session()
    code = get_code(s)
    course = get_course(s, code)
    name = input("请输入你的名字:")
    school = input("请输入你的一级单位:")
    clas = input("请输入你的二级单位:")
    dept = input("请输入你的三级单位:")
    save_door(course, s, school, name, clas, dept)
    get_image(s, code, course)


def show():
    print("本程序仅供交流和学习使用！！！！！！！！！")
    print("请勿将本程序用于任何盈利和违法方面！！！！")
    print("使用本程序给您带来的任何后果,您需自己承担。均于本程序作者无关");
    print("如果您\n同意:请输入 yes 运行本程序\n不同意:输入 no 关闭本程序")


if __name__ == '__main__':
    show()
    a = input("您是否同意:")
    if a == "yes":
        run()
    else:
        show_exit("退出本程序")
    show_exit("运行完成")
