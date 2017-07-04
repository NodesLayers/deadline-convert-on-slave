import os
import sys
from subprocess import call

### VARS
deadlinecommand_path = "C:\Program Files\Thinkbox\Deadline8\\bin\deadlinecommand.exe"
djv32_path = "Y:\\_nuke_global_setup\\_bin\\djv\\bin\\djv_convert.exe"
djv64_path = ""




print("This tool submits conversion jobs to the farm.")
print("")
print("")


fp = input("File to Convert? ")
fp = fp.replace('"','')

djv_path = '"'+djv32_path+'"'
outFile = fp.replace(".","_converted.")
print(outFile)


cmd = deadlinecommand_path+' \n-SubmitCommandLineJob \n-executable '+djv_path+' \n-arguments "'+fp+' '+outFile+'" \n-frames 1 \n-pool high \n-priority 55 \n-name "Media Conversion"' 
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