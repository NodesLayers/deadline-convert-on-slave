import os
import sys
from subprocess import call

### VARS
deadlinecommand_path = "C:\\Program Files\\Thinkbox\\Deadline8\\bin\deadlinecommand.exe"
djv32_path = "C:\\Program Files\\djv-1.1.0-Windows-64\\bin\\djv_convert.exe"
djv64_path = ""



print("")
print("")
print("This tool submits conversion jobs to the farm.")
print("")
print("")

fp = input("File to Convert? ")
fp = fp.replace('"','')

print("")
print("")
print("Choose Codec:")
print("1. ProRes")
print("2. h2.64")
print("3. mjpeg")
print("")
print("")
#opt = input("Option: ")


djv_path = '"'+djv32_path+'"'
outFile = fp.replace(".","_converted.")
print(outFile)
filename=os.path.basename(outFile)
print(filename)


cmd = deadlinecommand_path+' \n-SubmitCommandLineJob \n-executable '+djv_path+' \n-arguments "'+fp+' '+outFile+'" \n-frames 1 \n-pool high \n-priority 55 \n-name "Media Conversion: '+filename+'"' 
print()
print()
print(cmd)
print()
print()

call(cmd)

#deadlinecommand.exe
 #-SubmitCommandLineJob
 #-executable "c:\Program Files\Autodesk\3dsmax8\3dsmaxcmd.exe"
 #-arguments "-start:<STARTFRAME> -end:<ENDFRAME>
 #   -width:480 -height:320 <QUOTE>\\shared\path\scene.max<QUOTE>"
 #-frames 1-10
 #-chunksize 2
 #-group 3dsmax
 #-priority 50
 #-name "3dsmax command line job"
 #-prop MachineLimit=5