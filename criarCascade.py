import os
def criarCascade():
    for file_type in ['negativas']:
        for img in os.listdir(file_type):
            if file_type == 'positivas':
                line = file_type + '/'+img+'1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'negativas':
                line = file_type +'/'+img+'\n'
                with open('bg.txt' , 'a') as f:
                    f.write(line)
criarCascade()