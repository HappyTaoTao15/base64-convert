import PySimpleGUI as sg
import base64
import pyperclip

sg.theme("LightBlue2")
# stop = 0时变量为禁止状态 stop = 1时为开启状态 当stop = 1 条件状语会判断 然后停止程序
stop = 0
# begin 是触发条件状语变量没有什么实际作用， begin = 1时为第一个窗口 begin = 2时为第二个窗口 begin = 3时为第三个窗口（help）
begin = 1

def main():
    global begin, stop
    while True:

        # 此处为第一个窗口 --- 选择文件窗口
        if begin == 1:
            layout = [
                [sg.T("请选择文件：")],
                [sg.FileBrowse(button_text="选择文件", target="-IN-"), sg.In(key="-IN-")],
                [sg.B("开始转换", key="star"), sg.B("帮助", key="help")]
            ]
            window = sg.Window("base64编码器", layout)
            while True:
                event, values = window.read()
                if event == "help":
                    help()
                if event == "star":
                    begin = 2
                    with open(values["选择文件"], 'rb') as f:
                        ibase64 = base64.b64encode(f.read())
                        window.close()
                if event == None:
                    stop = 1
                    window.close()
                    break

        # 此处为第二个窗口---base64编码展示处
        if begin == 2:
            tbase64 = str(ibase64)
            sbase64 = tbase64[0:42]
            textsee = "点击复制即可获取完整编码"

            layout = [
                [sg.T("此文件base64编码如下：")],
                [sg.T("点击复制即可获取完整编码")],
                [sg.InputText(sbase64, tooltip=textsee)],
                [sg.B("复制", key="copy", font=("黑体", 12)), sg.B("返回", key="return", font=("黑体", 12))]
            ]
            window = sg.Window("base64编码器", layout)
            while True:
                event, values = window.read()
                if event == "copy":
                    pyperclip.copy(tbase64)
                    sg.popup_auto_close("复制成功！！！")
                if event == "return":
                    ibase64 = ""
                    begin = 1
                    stop = 0
                    window.close()
                    break
                if event == None:
                    stop = 1
                    break
        # 此处为关闭循环结束触发条件 stop == 1时便触发
        if stop == 1:
            break



# 此处为第三个窗口---帮助
def help():
    begin = 3
    ihelp = """ 
                软件使用帮助:
                1,按下按钮(请选择文件)
                2,选择您所需转换的文件
                3,按下(打开)
                4,按下按钮(开始转换)
                5,按下(复制)获取完整编码
                6,如需再次转换请点击(返回)，如果不用按右上角(x)退出软件
           """
    while True:
        stop1 = 0
        if begin == 3:
            layout = [
                [sg.ML(default_text=ihelp, disabled=True, size=(80, 10))],
            ]
            window = sg.Window("帮助", layout)
            while True:
                event, values = window.read()
                if event is None:
                    window.close()
                    stop1 = 1
                    window.close()
                    break
        if stop1 == 1:
            break


main()
