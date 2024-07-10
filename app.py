from tkinter import *
import customtkinter
import customtkinter as ctk
import subprocess
from subprocess import call

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

def logcat():
	call("adb logcat")
 
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

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title('ADB GUI Tool')
app.geometry('890x590')


# ADB Scripting Tab
scriptingLabel = ctk.CTkLabel(app, text="Scripting").place(x=20, y=0)
rebootButton = customtkinter.CTkButton(app, text="Reboot", command=reboot).place(x=20, y=30)
rebootRecoveryButton = customtkinter.CTkButton(app, text="Reboot to Recovery", command=rebootrecovery).place(x=200, y=30)
rebootFastbootButton = customtkinter.CTkButton(app, text="Reboot to Fastboot", command=rebootfastboot).place(x=380, y=30)
stateDeviceButton = customtkinter.CTkButton(app, text="Get State", command=getstatedevice).place(x=560, y=30)
getSNButton = customtkinter.CTkButton(app, text="Get Serial Number", command=getsn).place(x=740, y=30)

# ADB Debugging & Internal Debugging Tab
debuggingLabel = ctk.CTkLabel(app, text="Debugging").place(x=20, y=60)
logcatButton = customtkinter.CTkButton(app, text="Logcat", command=logcat).place(x=20, y=90)
startServerButton = customtkinter.CTkButton(app, text="Start ADB Server", command=startserver).place(x=200, y=90)
killServerButton = customtkinter.CTkButton(app, text="Kill ADB Server", command=killserver).place(x=380, y=90)
reconnectHostButton = customtkinter.CTkButton(app, text="Reconnect Host", command=reconnecthost).place(x=560, y=90)
reconnectDeviceButton = customtkinter.CTkButton(app, text="Reconnect Device", command=reconnecthost).place(x=740, y=90)
reconnectOfflineButton = customtkinter.CTkButton(app, text="Reconnect Offline", command=reconnectoffline).place(x=20, y=130)


app.mainloop()