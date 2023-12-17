import os
import platform

print("len methods os : " + str(len(dir(os)))) # in window = 156 / in linux > 300
os.uname()
# information windows
print(platform.uname())

# information linux
# os.uname()

""" Return a unicode string representing the current working directory. """
print("dir: " + os.getcwd())

"""Return a list containing the names of the files in the directory."""
print("list dir : " + str(os.listdir()))

#  create dir
# os.mkdir(name)

# delete dir
# os.remove(name)

# change name dir
# os.rename()


