"""with open('my_list_.py','r+') as my_file:
	read_data = my_file.read()
	
#display the contents of the file
print(read_data)

#check if file is closed
print(my_file.closed)"""
my_file=open('song.mp3','r+b')
my_file.seek(-128,2)
trial_read=my_file.read()
checking=trial_read.decode()
print(type(checking), checking)
if not checking.find('TAG'):
	print('Name of song:',checking[3:33])
	print('Artist:',checking[33:63])
	print('Album:',checking[63:93])
else:
	print('No TAG',checking.find('TAG'))
"""for line in my_file:
	print(line)"""



