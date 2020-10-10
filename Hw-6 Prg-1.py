import os
import sys

number_of_command_line_arguments = len(sys.argv)

print(number_of_command_line_arguments)

print(os.path.abspath(sys.argv[0]))

while os.path.exists(str(sys.argv[0])):
	os.path.exists(str(sys.argv[0]))
	continue
	print("True")
else:
	print("Alert")
