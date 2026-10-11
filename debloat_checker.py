import os
import json

# Global UAD debloat reference list
with open("debloat_list/uad_lists.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

app_package_names = []
for line in data:
    if 'removal' in data[line] and data[line]['removal'] == 'Recommended':
        app_package_names.append(line)


def load_package_list(filepath):
    """Load package names from a file, ignoring comments and empty lines."""
    packages = set()
    if not os.path.exists(filepath):
        return packages
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Ignore empty lines and comment lines
            if not line or line.startswith('#'):
                continue
            # Extract package name (handles possible inline comments)
            pkg = line.split('#')[0].strip()
            if pkg:
                packages.add(pkg)
    return packages


donotuninstall = load_package_list("debloat_list/donotuninstall.txt")
safetouninstall = load_package_list("debloat_list/safetouninstall.txt")


def checkDebloat(items):
    uninstall_list = []
    remaining_list = []

    for item in items:
        # Check against the curated safe-to-uninstall list
        if item in safetouninstall:
            uninstall_list.append(item)
        else:
            remaining_list.append(item)

    final_uninstall_list = []
    for item in uninstall_list:
        # Strictly preserve any package in the protected do-not-uninstall list
        if item in donotuninstall:
            remaining_list.append(item)
        else:
            final_uninstall_list.append(item)

    return final_uninstall_list, remaining_list