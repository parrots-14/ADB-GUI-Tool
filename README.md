# ADB GUI Tool
Note that this tool may be unstable, and I am not responsible if you brick your device.
## What is this?
This is a tool utilizing Python to run ADB commands in a standalone app, instead of the terminal. This is meant for beginners to ADB, but can be used by anyone.
## How do I set this up?
For starters, you'll need to install ADB and Python.

From there, you need to open Command Prompt in the directory that you have the .py file opened in, and run 'python app.py.' The command prompt also serves as a way to view the output, so don't close it.

## What commands are currently implemented, and what do they do?
### Scripting
Reboot - Just reboots the phone.

Reboot Recovery - Reboots the phone into recovery.

Reboot Fastboot - Reboots the phone into fastboot.

Get State Device - Prints the state that the phone is in. (recovery, device, etc.)

Get Serial Number - Prints the device's serial number.

Root - Gives ADB root access.

### Debugging
Logcat - Gives you a constant log of what's happening in the phone. Note that from my experience, there's no way to stop this except for unplugging the phone or closing the app.

Start Server - Starts the ADB server.

Kill Server - Kills the ADB server. This could help to fix some issues when running commands.

Reconnect - Kicks the host, forcing it to reconnect

Reconnect device - Kicks the device, forcing it to reconnect

Reconnect offline - Resets offline devices, forcing it to reconnect

### File Transfer

Install APK - Installs the APK. Use the first argument entry box for the path.

Push - Pushes a file to a directory in the device. Use the first argument for the path to the file on the PC, then the second argument for the path on the android device.

Pull - Pulls a file from the device to the computer. Use the first argument for the path to the file on the device.

Remount - Remounts the device.

Sideload - Sideloads ZIP files on the device. Make sure your device is on sideload mode. If you wanna check, use getstate.

## What commands could come soon?
### Tentative
ADB Shell and other commands that rely on it - I'm unsure if I'm going to add this, because everytime that I add this and run the command, it ends up crashing.
### Likely
Reboot Bootloader - Reboots into bootloader, sometimes works for other devices that just reboot to system when you run reboot to fastboot. Coming in 1.3

Devices - Easy to implement, coming in 1.3

Fastboot tab - Likely coming in 1.3

## How can I see the output?
When you use CMD to open the .py file, the CMD will display the output.

## Troubleshooting
Waiting for device / Device not found - Ensure you have the device plugged in, and USB Debugging enabled. To enable this, go to Settings > About Phone > Build Number (Tap 7 times) > Go back to Settings Menu > Developer Options. From there, enable USB debugging. The process may be different for different phones, but it typically involves this process. You'll have to trust the device too when you plug it in.

Killing the server with the 'Kill Server' button then starting it can fix issues with running commands sometimes.
