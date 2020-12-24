import os

if os.path.exists('demo.txt'):
    os.remove("demo.txt")
else:
    print("File is noe exist!")

# osrmdir is used to remove a folder
# systax is os.rmdir("folder name")
