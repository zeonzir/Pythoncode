#Program to read and edit a text file based on certain criterion
try:
	f=open('PlainTextFile.txt','r+b')
	Data=f.read()
	StringData=Data.decode()
	f.seek(StringData.find('word'),0) #Find function supported for string
	STR=f.read() #Reading the contents of the file from the word 'word' would force the pointer to EOF
	f.seek(StringData.find('word'),0)
	STR=STR.decode()
	STR='inserted '+STR
	STR=STR.encode()
	f.write(STR)
	f.close() #f.close() in finally would result in an extra error if our except case is triggered.
except BaseException as err:
	print('Check file again')



