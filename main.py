import os
from debloat_checker import *

file_path = 'app.txt'

# Open the file with the correct encoding (UTF-8, which will work for US-ASCII as well)
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

items = [line.replace('package:', '', 1).strip() for line in lines]

uninstall_list, remaining_list = checkDebloat(items)
uninstall_list.sort()

# Create directory if the directory does not exist
if not os.path.exists("output"):
    os.makedirs("output")

# Open the output file to write
with open("output/uninstall_list.txt", 'w') as f_out:
    # Write each item to the output file
    for item in uninstall_list:
        # Reference the adb in the correct folder
        f_out.write('~/Documents/adb/adb shell pm uninstall --user 0 ' + item + '\n')

remaining_list.sort()

# Open the output file to write
with open("output/remaining_list.txt", 'w') as f_out:
    # Write each item to the output file
    for item in remaining_list:
        f_out.write(item + '\n')

