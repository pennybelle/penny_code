from os import path

log = 'HighScore.log'

def file_check():
    if path.exists(log): return True
    else: return False
print(file_check())
if not file_check():
    record = open(log, 'w+')
    record.writelines([str(0), '\n', str(0)])
    record.close()

record = open(log, 'r')
score = int(record.readlines()[1])
print(score)