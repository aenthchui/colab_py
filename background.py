import shutil
fileRead = False
def unzipFiles():
    global lines
    lines = []
    shutil.unpack_archive("converted_keras.zip", "converted_keras")
    with open('./converted_keras/labels.txt') as f:
        lines = f.readlines()
    f.close()
    global labels
    labels = []
    for x in lines:
            labels.append(x[x.find(' ')+1:len(x)-1])
