#Program to open and read a mp3 file for TAG
try:
	my_file=open('song.mp3','r+b')
	my_file.seek(-128,2)
	trial_read=my_file.read()
	checking=trial_read.decode()
	if not checking.find('TAG'):
		print('Name of song:',checking[3:33])
		print('Artist:',checking[33:63])
		print('Album:',checking[63:93])
	else:
		print('No TAG',checking.find('TAG'))
except BaseException as err:
	print('Check file again')