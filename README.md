# ADB GUI Tool
This app is still being developed, so expect more content.
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

### Debugging
Logcat - Gives you a constant log of what's happening in the phone. Note that from my experience, there's no way to stop this except for unplugging the phone or closing the app.

Start Server - Starts the ADB server.

Kill Server - Kills the ADB server. This could help to fix some issues when running commands.

Reconnect - Kicks the host, forcing it to reconnect

Reconnect device - Kicks the device, forcing it to reconnect

Reconnect offline - Resets offline devices, forcing it to reconnect

## What commands will be added?

ADB Install - Command implemented, working on adding arguments to get the path to APK, coming in 1.2

ADB Uninstall - Not implemented, coming in 1.2

ADB Sideload - Not implemented, coming in 1.2

ADB Push - Not implemented

ADB Pull - Not implemented

I plan on adding more, but those are the ones that are going to be added soon.

## How can I see the output?
When you open the .py file, you should get py.exe, or something resembling Command Prompt. From there, you will be able to see the output.

## Troubleshooting
Waiting for device / Device not found - Ensure you have the device plugged in, and USB Debugging enabled. To enable this, go to Settings > About Phone > Build Number (Tap 7 times) > Go back to Settings Menu > Developer Options. From there, enable USB debugging. The process may be different for different phones, but it typically involves this process. You'll have to trust the device too when you plug it in.

Killing the server with the 'Kill Server' button then starting it can fix issues with running commands sometimes.
