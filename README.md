# ADB GUI Tool
Note that this tool has a very minimal chance to brick your phone if you don't know what you're doing. Additionally, if you're on an operating system other than Windows, check the "How do I set this up?" area.
## What is this?
This is a tool utilizing Python to run ADB commands in a standalone app, instead of the terminal. This is meant for beginners to ADB, but can be used by anyone.
## How do I set this up?
The setup is probably gonna be different for operating systems other than Windows. However, what does apply globally is that you MUST have Python installed.

### Windows
1. Unzip
2. Run 'setup.bat' so that it installs a dependency needed for the program
3. Open CMD and get into the directory that the app is in
4. Run 'python app.py'

### Linux, MacOS (hopefully), etc.
1. Unzip
2. Delete EVERYTHING in the app except for 'app.py.' The setup script is only for Windows, and installs a dependency which can be manually installed. The rest of the files are the ADB dependencies for Windows.
3. Open up your terminal and run 'pip install customtkinter'
4. Install ADB onto your computer.
5. Run the python script, and it should launch.

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

### Fastboot Basics

View Devices - Shows devices currently connected in fastboot

Reboot - Reboots to system

Reboot to Recovery - Reboots to recovery

### Fastboot unlocking / locking bootloader

Unlock Bootloader - Unlocks the bootloader, allowing unsigned firmware to be flashed

Lock Bootloader - Locks the bootloader, checking if the firmware is signed. MAKE SURE YOU ARE COMPLETELY BACK TO STOCK BEFORE RUNNING THIS

Critical Unlock Bootloader - Unlocks critical bootloader partitions

Critical Lock Bootloader - Locks critical bootloader partitions.

## What commands could come soon?
### Tentative
None at the moment
### Likely
None at the moment

## How can I see the output?
When you use CMD to open the .py file, the CMD will display the output.

## Troubleshooting
### Waiting for device / Device not found
Ensure you have the device plugged in, and USB Debugging enabled. To enable this, go to Settings > About Phone > Build Number (Tap 7 times) > Go back to Settings Menu > Developer Options. From there, enable USB debugging. The process may be different for different phones, but it typically involves this process. You'll have to trust the device too when you plug it in.
### ADB server error
This indicates that your ADB server is outdated. For Windows, delete everything in the directory except for the tool script itself, and then paste the platform tools ZIP into the directory and unzip it. For Linux, just run 'sudo apt-get install android-sdk-platform-tools' if on a Debian based distribution, or 'sudo dnf install android-tools' for Fedora based distributions.

Killing the server with the 'Kill Server' button then starting it can fix issues with running commands sometimes.

Fastboot is currently very unstable, but if the app crashes the commands should still run.
