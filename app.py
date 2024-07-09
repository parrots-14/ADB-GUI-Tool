# Generated with tkedit (tkedit.glitch.me)

import tkinter as tk
from tkinter import ttk
from tkinter import * 
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
    
def getstatebootloader():
	call("adb get-state bootloader")
    
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


root = Tk()

root.geometry('890x590')
root.configure(background='#282828')
root.title('ADB GUI Tool')


Label(root, text='Scripting', fg='#FFFFFF', bg='#282828', font=('arial', 12, 'normal')).place(x=20, y=0)


Button(root, text='Reboot', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=reboot).place(x=20, y=30)


Button(root, text='Reboot to Recovery', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=rebootrecovery).place(x=120, y=30)


Button(root, text='Reboot to Fastboot', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=rebootfastboot).place(x=310, y=30)


Button(root, text='Get-State Device', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=getstatedevice).place(x=500, y=30)


Button(root, text='Get-State Bootloader', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=getstatebootloader).place(x=690, y=30)


Button(root, text='Get Serial Number', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=getsn).place(x=20, y=75)


Label(root, text='Debugging', fg='#FFFFFF', bg='#282828', font=('arial', 12, 'normal')).place(x=20, y=110)


Button(root, text='Logcat', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=logcat).place(x=20, y=140)


Button(root, text='Start ADB Server', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=startserver).place(x=120, y=140)


Button(root, text='Kill ADB Server', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=killserver).place(x=290, y=140)


Button(root, text='Reconnect', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=reconnecthost).place(x=440, y=140)


Button(root, text='Reconnect Device', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=reconnectdevice).place(x=555, y=140)


Button(root, text='Reconnect Offline', bg='#181818', fg='#FFFFFF', font=('arial', 12, 'normal'), command=reconnectoffline).place(x=720, y=140)


root.mainloop()