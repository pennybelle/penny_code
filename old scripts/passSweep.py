class passSweep():
    alp = 'abcdefghijklmnopqrstuvwxyz'
    indx = ''
    output = ''
    step = int(0)

    def sweep():
        while True:
            for char in passSweep.alp:
                passSweep.output = passSweep.indx + char
                print(passSweep.output)
            passSweep.indx += passSweep.alp[passSweep.step % 26]
            passSweep.step += 1
        
passSweep.sweep()