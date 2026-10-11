# Xiaomi MIUI 14 Global 14.0.9 Debloat List (DEC 2024)
If you're frustrated with the pre-installed applications on your new phone, you're not alone. Many of these apps can be redundant or intrusive, often causing issues such as push notifications and excessive battery drain.

By using ADB (Android Debug Bridge), you can safely remove these unwanted applications without the need for rooting. This method is less risky than manual removal and ensures that system variables remain intact, allowing you to continue receiving OTA updates without issues.

This script is designed to help Xiaomi phone users remove unnecessary pre-installed applications and bloatware from their devices. 
By running this script, you can declutter your phone, improve performance, and free up storage space.

**DISCLAIMER: Use at your own risk. I am not responsible for anything that could happen to your phone. It is highly recommended to use it on a new phone or on a clean state after your phone is reset.**

## Debloat List
This list is curated for **MIUI 14**
- Xiaomi Redmi Note 10 Pro (sweet)

The two list files drive everything:
- `debloat_list/safetouninstall.txt` - packages that WILL be removed
- `debloat_list/donotuninstall.txt` - packages that will NEVER be removed
  (this file wins if a package ever appears in both)

# Setting Up
## Download Python
Install python on your computer from https://www.python.org/downloads/
```
python --version
```
```
sudo apt install python-is-python3
```

## Download ADB (Android Debug Bridge)
Download the platform-tools for ADB
https://developer.android.com/tools/releases/platform-tools

## Steps to Enable Developer Mode on MIUI 14 OS
Steps are to be done on your phone.

1. Open Settings.
2. Tap on About phone.
3. Tap on OS version multiple times until Developer Mode is enabled.
4. Go back to Settings, then select Additional settings.
5. Tap on Developer options and toggle it on.
6. Scroll down and find USB debugging, then toggle it on to enable USB Debugging.
7. Check the instructions and click OK.

If unsure, please follow some youtube video.

## Verify Device Is Connected
Use a compatible USB cable to connect your phone to a USB port on your computer. If this is the first time connecting your phone to this computer, you may see a prompt on your phone asking you to authorize the connection. Tap Allow or OK to grant permission.

To verify if your device is properly connected and recognized by ADB (Android Debug Bridge), open Command Prompt or Terminal on your computer,
enter the following and you should be able to see a similar output:
```
./platform-tools/adb devices

List of devices attached
12345abc        device
```

# Debloating
## Generate a list of packages on the phone
Run the command to get the list of apps on your phone
```
./adb shell pm list packages > app.txt
```

## Custom Debloat List
To customize what gets removed, edit the two files in `debloat_list/`:
- add a package to `safetouninstall.txt` to REMOVE it
- add a package to `donotuninstall.txt` to KEEP it (this file always wins)


## Generate List of App to Uninstall
Run the script to get the list of app to uninstall
```
python main.py
```

Three files will be generated in the 'output' folder:
- `uninstall_list.sh` - executable script with the `adb shell pm uninstall --user 0` commands
- `restore_list.sh` - executable rollback script (`adb shell cmd package install-existing`) for the same packages
- `remaining_list.txt` - the packages that will remain untouched

Always review `output/uninstall_list.sh` before running it.

## Uninstalling of Apps

Run the generated script (it is already executable):
```
./output/uninstall_list.sh
```
or
```
bash output/uninstall_list.sh
```

If anything breaks, roll everything back with:
```
./output/restore_list.sh
```
then reboot the phone. (`pm uninstall --user 0` never touches the system
partition, so a factory reset also restores everything.)

# Reference
The debloat list is taken from \
https://github.com/0x192/universal-android-debloater/blob/main/resources/assets/uad_lists.json
