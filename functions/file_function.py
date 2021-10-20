def reader(filepath):
    file = open(filepath)
    c = file.read()
    file.close()
    return c

def writer(filepath, data):
    file = open(filepath,'w')
    file.write(data)
    file.close()
    return True

def updater(filepath, data):
    file = open(filepath,'a')
    file.write(data)
    file.close()
    return True


