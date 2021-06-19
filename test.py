from win32api import ShellExecute
def openword(text):
    ShellExecute(0, 'open', text, '', '', 1)
text="file:///C:/Users/13162/Desktop/读书报告.docx"
openword(text)