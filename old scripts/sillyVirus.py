import os

directory = 0
while directory != 1000:
    os.mkdir(str(directory))
    os.chdir(str(directory))
    directory += 1

open("lmao.txt", "w").writelines("why did you keep going lmao")
