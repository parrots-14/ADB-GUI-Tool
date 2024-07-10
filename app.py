from tkinter import *
import customtkinter as ctk
from subprocess import call

# Made by parrots-14 on Github

# Commands with no arguments

def reboot():
    call("adb reboot")

def rebootrecovery():
    call("adb reboot recovery")

def rebootfastboot():
    call("adb reboot fastboot")

def logcat():
    call("adb logcat")

def getstatedevice():
    call("adb get-state device")

def getsn():
    call("adb get-serialno")

def startserver():
    call("adb start-server")

def killserver():
    call("adb kill-server")

def reconnecthost():
    call("adb reconnect")

def reconnectdevice():
    call("adb reconnect device")

def reconnectoffline():
    call("adb reconnect offline")
    
def remount():
    call("adb remount")
    
def root():
    call("adb root")

## Commands that have arguments

def install():
    arg = argument.get()
    call(f"adb install {arg}")
    
def pull():
    arg = argument.get()
    call(f"adb pull {arg}")
    
def push():
    arg = argument.get()
    arg2 = argument2.get()
    call(f"adb push {arg} {arg2}")
    
def sideload():
    arg = argument.get()
    call(f"adb sideload {arg}")

# Setting appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title('ADB GUI Tool')
app.geometry('890x590')

# Arguments
argument = StringVar()
argument2 = StringVar()

# ADB Scripting Tab
scriptingLabel = ctk.CTkLabel(app, text="Scripting").place(x=20, y=0)
rebootButton = ctk.CTkButton(app, text="Reboot", command=reboot).place(x=20, y=30)
rebootRecoveryButton = ctk.CTkButton(app, text="Reboot to Recovery", command=rebootrecovery).place(x=200, y=30)
rebootFastbootButton = ctk.CTkButton(app, text="Reboot to Fastboot", command=rebootfastboot).place(x=380, y=30)
stateDeviceButton = ctk.CTkButton(app, text="Get State", command=getstatedevice).place(x=560, y=30)
getSNButton = ctk.CTkButton(app, text="Get Serial Number", command=getsn).place(x=740, y=30)
rootButton = ctk.CTkButton(app, text="ADB Root", command=root).place(x=20, y=70)

# ADB Debugging & Internal Debugging Tab
debuggingLabel = ctk.CTkLabel(app, text="Debugging").place(x=20, y=100)
logcatButton = ctk.CTkButton(app, text="Logcat", command=logcat).place(x=20, y=130)
startServerButton = ctk.CTkButton(app, text="Start ADB Server", command=startserver).place(x=200, y=130)
killServerButton = ctk.CTkButton(app, text="Kill ADB Server", command=killserver).place(x=380, y=130)
reconnectHostButton = ctk.CTkButton(app, text="Reconnect Host", command=reconnecthost).place(x=560, y=130)
reconnectDeviceButton = ctk.CTkButton(app, text="Reconnect Device", command=reconnectdevice).place(x=740, y=130)
reconnectOfflineButton = ctk.CTkButton(app, text="Reconnect Offline", command=reconnectoffline).place(x=20, y=170)

# App Installation & File Transfer Tab
installationLabel = ctk.CTkLabel(app, text="File Transfer").place(x=20, y=200)
installButton = ctk.CTkButton(app, text="Install APK", command=install).place(x=20, y=230)
pushButton = ctk.CTkButton(app, text="Push", command=push).place(x=200, y=230)
pullButton = ctk.CTkButton(app, text="Pull", command=pull).place(x=380, y=230)
remountButton = ctk.CTkButton(app, text="Remount", command=remount).place(x=560, y=230)
sideloadButton = ctk.CTkButton(app, text="Sideload", command=sideload).place(x=740, y=230)

# Arguments in UI
argumentLabel = ctk.CTkLabel(app, text="Arguments").place(x=20, y=520)
argumentEntry = ctk.CTkEntry(app, textvariable=argument, placeholder_text="Argument 1").place(x=20, y=550)
argumentEntry2 = ctk.CTkEntry(app, textvariable=argument2, placeholder_text="Argument 2").place(x=200, y=550)


app.mainloop()