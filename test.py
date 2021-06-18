from win32api import ShellExecute
def openword(text):
    ShellExecute(0, 'open', text, '', '', 1)