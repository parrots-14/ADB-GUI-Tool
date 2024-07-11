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
    
def rebootbootloader():
    call("adb reboot bootloader")
    
def devices():
    call("adb devices")

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
    
# Fastboot button commands
def fastboot_devices():
    call("fastboot devices")
    
def fastboot_reboot():
    call("fastboot reboot")
    
def fastboot_reboot_recovery():
    call("fastboot reboot recovery")
    
def fastboot_unlock():
    call("fastboot flashing unlock")
    
def fastboot_lock():
    call("fastboot flashing lock")
    
def fastboot_critical_unlock():
    call("fastboot flashing unlock_critical")
    
def fastboot_critical_lock():
    call("fastboot flashing lock_critical")

# Setting appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title('ADB GUI Tool')
app.geometry('890x590')

# Arguments
argument = StringVar()
argument2 = StringVar()
argument3 = StringVar()
argument4 = StringVar()

# Tabview
my_tab = ctk.CTkTabview(app, width=885, height=585)
my_tab.pack(pady=10)

# Actual tabs
tab_1 = my_tab.add("ADB")
tab_2 = my_tab.add("Fastboot")

# ADB Scripting
scriptingLabel = ctk.CTkLabel(tab_1, text="Scripting").place(x=10, y=0)
rebootButton = ctk.CTkButton(tab_1, text="Reboot", command=reboot).place(x=10, y=30)
rebootRecoveryButton = ctk.CTkButton(tab_1, text="Reboot to Recovery", command=rebootrecovery).place(x=190, y=30)
rebootFastbootButton = ctk.CTkButton(tab_1, text="Reboot to Fastboot", command=rebootfastboot).place(x=370, y=30)
rebootBootloaderButton = ctk.CTkButton(tab_1, text="Reboot to Bootloader", command=rebootbootloader).place(x=550, y=30)
stateDeviceButton = ctk.CTkButton(tab_1, text="Get State", command=getstatedevice).place(x=730, y=30)
getSNButton = ctk.CTkButton(tab_1, text="Get Serial Number", command=getsn).place(x=10, y=70)
rootButton = ctk.CTkButton(tab_1, text="ADB Root", command=root).place(x=190, y=70)

# ADB Debugging & Internal Debugging
debuggingLabel = ctk.CTkLabel(tab_1, text="Debugging").place(x=10, y=100)
logcatButton = ctk.CTkButton(tab_1, text="Logcat", command=logcat).place(x=10, y=130)
startServerButton = ctk.CTkButton(tab_1, text="Start ADB Server", command=startserver).place(x=190, y=130)
killServerButton = ctk.CTkButton(tab_1, text="Kill ADB Server", command=killserver).place(x=370, y=130)
reconnectHostButton = ctk.CTkButton(tab_1, text="Reconnect Host", command=reconnecthost).place(x=550, y=130)
reconnectDeviceButton = ctk.CTkButton(tab_1, text="Reconnect Device", command=reconnectdevice).place(x=730, y=130)
reconnectOfflineButton = ctk.CTkButton(tab_1, text="Reconnect Offline", command=reconnectoffline).place(x=10, y=170)
devicesButton = ctk.CTkButton(tab_1, text="View Devices", command=devices).place(x=190, y=170)

# App Installation & File Transfer
installationLabel = ctk.CTkLabel(tab_1, text="File Transfer").place(x=10, y=200)
installButton = ctk.CTkButton(tab_1, text="Install APK", command=install).place(x=10, y=230)
pushButton = ctk.CTkButton(tab_1, text="Push", command=push).place(x=190, y=230)
pullButton = ctk.CTkButton(tab_1, text="Pull", command=pull).place(x=370, y=230)
remountButton = ctk.CTkButton(tab_1, text="Remount", command=remount).place(x=550, y=230)
sideloadButton = ctk.CTkButton(tab_1, text="Sideload", command=sideload).place(x=730, y=230)

# Arguments in UI for Tab 1
argumentLabel1 = ctk.CTkLabel(tab_1, text="Arguments").place(x=10, y=460)
argumentEntry1 = ctk.CTkEntry(tab_1, textvariable=argument, placeholder_text="Argument 1").place(x=10, y=490)
argumentEntry2 = ctk.CTkEntry(tab_1, textvariable=argument2, placeholder_text="Argument 2").place(x=190, y=490)

# Arguments in UI for Tab 2
argumentLabel2 = ctk.CTkLabel(tab_2, text="Arguments").place(x=10, y=460)
argumentEntry3 = ctk.CTkEntry(tab_2, textvariable=argument3, placeholder_text="Argument 1").place(x=10, y=490)
argumentEntry4 = ctk.CTkEntry(tab_2, textvariable=argument4, placeholder_text="Argument 2").place(x=190, y=490)

# Fastboot section
fastbootWarningLabel = ctk.CTkLabel(tab_2, text="Warning! These commands can brick your device if you don't know what you're doing.").place(x=10, y=0)
fastbootBasicsLabel = ctk.CTkLabel(tab_2, text="Basics").place(x=10, y=30)
fastbootDevicesButton = ctk.CTkButton(tab_2, text="Devices", command=fastboot_devices).place(x=10, y=60)
fastbootRebootButton = ctk.CTkButton(tab_2, text="Reboot", command=fastboot_reboot).place(x=190, y=60)
fastbootRebootRecoveryButton = ctk.CTkButton(tab_2, text="Reboot to Recovery", command=fastboot_reboot_recovery).place(x=370, y=60)
fastbootBasicsLabel = ctk.CTkLabel(tab_2, text="Locking / Unlocking Bootloader -  Do not touch unless you know what you're doing!").place(x=10, y=90)
fastbootUnlockButton = ctk.CTkButton(tab_2, text="Unlock Bootloader", command=fastboot_unlock).place(x=10, y=120)
fastbootLockButton = ctk.CTkButton(tab_2, text="Lock Bootloader", command=fastboot_lock).place(x=190, y=120)
fastbootCriticalUnlockButton = ctk.CTkButton(tab_2, text="Critical Unlock Bootloader", command=fastboot_critical_unlock).place(x=370, y=120)
fastbootCriticalLockButton = ctk.CTkButton(tab_2, text="Critical Lock Bootloader", command=fastboot_critical_lock).place(x=550, y=120)

app.mainloop()
