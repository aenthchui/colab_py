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
    return labels
def inputString():
    import ipywidgets
    children = [ipywidgets.Text(description=name) for name in ['Text:']*len(labels)]
    tab = ipywidgets.Tab()
    tab.children = children
    for i in range(len(labels)):
        tab.set_title(i, labels[i])
    tab
