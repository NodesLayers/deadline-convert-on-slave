import os
import sys
from subprocess import call

### VARS
deadlinecommand_path = "C:\\Program Files\\Thinkbox\\Deadline8\\bin\deadlinecommand.exe"

print("")
print("")
print("This tool submits copy jobs to the farm.")
print("")
print("")

file_in = input("Path to copy from? ")
end_path = os.path.split(file_in)[1]
print("")
print("")
print("")
file_out = input("Path to copy to? ")
file_out = os.path.join(file_out, end_path)
print("")
print("")
print("")


cmd = deadlinecommand_path+' \n-SubmitCommandLineJob \n-executable robocopy.exe \n-arguments "'+file_in+' '+file_out+' /MIR /MT" \n-frames 1 \n-pool high \n-priority 55 \n-name "File Copy: '+end_path+'"' 
print()
print()
print(cmd)
print()
print()

call(cmd)