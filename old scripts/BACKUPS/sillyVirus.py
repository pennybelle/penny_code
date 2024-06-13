import os


def cd(): os.system('cd')


directory = 0
while directory != 10:
    os.mkdir(str(directory))
    cd()
    directory += 1
