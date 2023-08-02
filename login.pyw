from win10toast import ToastNotifier
import requests
import os
import socket

def get_ip():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == '__main__':

    #以下5个变量，需要根据自己的情况进行修改，
    #与MacroDroid中的几乎保持一致,
    #仅对中文作修改，其他的字符（特别是前后的单引号）均不要修改！
    login_IP = '改为校园网登录IP'
    not_sign_in_title = '改为未登录状态的页面标题'
    result_return = '改为登录成功页面的一些特征字符串'
    sign_parameter = f'改为那一长串的登录参数'
    signed_in_title = '改为已登录状态的页面标题'

    #以下4个变量，可根据自己的需要，决定是否修改
    already_icon = None
    success_icon = None
    false_icon = None
    unknown_icon = None

    try:
        r = requests.get(login_IP,
                        timeout = 1)
        req = r.text
    except:
        req = 'False'

    if signed_in_title in req:
        ToastNotifier().show_toast(title = "该设备已经登录",
                   msg = "校园网状态",
                   icon_path = already_icon,
                   duration = 5,
                   threaded = False)
        os._exit(0)

    elif not_sign_in_title in req:
        r = requests.get(sign_parameter, timeout=1)
        req = r.text
        if result_return in req:
            ToastNotifier().show_toast(title = "登录成功",
                   msg = "校园网状态",
                   icon_path = success_icon,
                   duration = 5,
                   threaded = False)
        else:
            ToastNotifier().show_toast(title = "登录失败",
                   msg = "校园网状态",
                   icon_path = false_icon,
                   duration = 5,
                   threaded = False)

        os._exit(0)

    else:
        ToastNotifier().show_toast(title = "未连接到校园网",
                   msg = "校园网状态",
                   icon_path = unknown_icon,
                   duration = 5,
                   threaded = False)
        os._exit(0)


