WinActivate("��");
;ʶ��windows����
ControlFocus("��","","Edit1")
;���ڵȴ�10��
WinWait("[Class:#32770]","",10)
;�������������Ҫ�ϴ����ļ��ĵ�ַ
ControlSetText("��","","Edit1","C:\Users\admin\Desktop\loadrunner _HTTP.docx")
Sleep(2000)
;����򿪰�ť
ControlClick("��","","Button1");
Sleep(2000)