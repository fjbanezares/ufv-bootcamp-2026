import os
import platform

def get_home_directory():
    if platform.system() == 'Windows':
        # Windows-specific code to get the home directory
        return os.environ['USERPROFILE']
    else:
        # POSIX-specific code to get the home directory
        print(platform.system()) # Darwin in my Mac
        return os.environ['HOME']

print("Home directory:", get_home_directory())
