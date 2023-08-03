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

    login_IP = '100.64.4.10'
    not_sign_in_title = '上网登录页'
    result_return = 'result":1'
    sign_parameter = f'改为那一长串的登录参数'
    signed_in_title = '用户信息页'

    #以下4个变量，为链接提示的图头，可根据自己的需要，决定是否修改
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


