import shutil
global labels
labels=[]
lines=[]
fileRead = False

def unzipFiles():
    shutil.unpack_archive("converted_keras.zip", "converted_keras")
    with open('./converted_keras/labels.txt') as f:
        lines = f.readlines()
    f.close()
    for x in lines:
            labels.append(x[x.find(' ')+1:len(x)-1])
