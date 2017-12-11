WinActivate("打开");
;识别windows窗口
ControlFocus("打开","","Edit1")
;窗口等待10秒
WinWait("[Class:#32770]","",10)
;向输入框输入需要上传的文件的地址
ControlSetText("打开","","Edit1","C:\Users\admin\Desktop\loadrunner _HTTP.docx")
Sleep(2000)
;点击打开按钮
ControlClick("打开","","Button1");
Sleep(2000)