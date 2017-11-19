from bs4 import BeautifulSoup
data=open('Login.aspx.html')
soup = BeautifulSoup(data,'lxml')
array_inputs=soup.findAll('placeholder')
i=0
while i<len(array_inputs):
    print(array_inputs[i])
    i=i+1
