import ctypes
import os
import shutil
import sys
import time

# Set the window title
ctypes.windll.kernel32.SetConsoleTitleW('PyMove 1.0')

# Set the destiny folder
DESTINATIONFOLDER = str('.\\pp')

# Check if a file has been dropped on the script
if len(sys.argv) == 1:
	print('No arguments or dropped files received, exiting...')
	time.sleep(2.5)
	sys.exit()

# If there is at least one file or folder, proceed to move to the set destiny folder
elif len(sys.argv) > 1:
	
	# Loop the arguments array and move each element to the desired destiny
	for i in range(1, len(sys.argv)):
		argsElement = sys.argv[i]
		shutil.move(argsElement, DESTINATIONFOLDER)

		# Check if the element is a folder or a file
		if os.path.isfile(argsElement):
			print('The file ' + argsElement + ' has been moved to ' + DESTINATIONFOLDER + '!')
		elif os.path.isdir(argsElement):
			print('The folder ' + argsElement + ' has been moved to ' + DESTINATIONFOLDER + '!')
		else:
			print('The element ' + argsElement + ' has been moved to ' + DESTINATIONFOLDER + '!')

	print('\n\nAll elements have been moved successfully!\n\n')

	# Ask to open a Windows Explorer window to the destination folder
	userInput = str(input('Do you wish to open the destination folder? Y/N \n'))

	if userInput == 'Y' or userInput == 'y':
		os.system('explorer.exe ' + DESTINATIONFOLDER)
		sys.exit()
		
	elif userInput == 'N' or userInput == 'n':
		print('\nAlright then! Ending script...')
		time.sleep(1.5)
		sys.exit()

	else:
		print('\nAll set. Ending script...')
		time.sleep(1.5)
		sys.exit()

else:
	print('\nUndefined error.')
	os.system('pause')

