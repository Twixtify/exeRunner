import os
import subprocess
import threading
import win32api


def file_crawler():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    exe_file = []
    for drive in drives:
        for root, dirs, files in os.walk(drive, topdown=True, onerror=None, followlinks=False):
            for name in files:
                if name.lower().endswith('.exe'):
                    # subprocess.run(os.path.join(root, name))
                    #exe_file.append(os.path.join(root, name))
                    print(os.path.join(root, name))
            #for name in dirs:
            #    print(os.path.join(root, name))


file_crawler()


drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
print(drives[0])

