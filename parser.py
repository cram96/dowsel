array=[]
datafile= open('Login.aspx.html')
for line in datafile.readlines():
    if 'input' in line:
        array.insert(0,line)

