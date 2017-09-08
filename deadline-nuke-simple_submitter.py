import os
import sys
from subprocess import call

## Settings
title = "Deadline - Simple Farm Submitter"
my_version = "v0.1"
nuke_script_name = os.path.basename(nuke.root().name())
nuke_script_folder = os.path.dirname(nuke.root().name())
nuke_script_path = os.path.normpath(os.path.join(nuke_script_folder,nuke_script_name))
prio_message = "Request Priority"

deadline_path = os.environ['DEADLINE_PATH']
deadline_command_path = os.path.join(deadline_path, "deadlinecommand.exe")
print "Deadline Slave Path: "+deadline_command_path

nuke_exe_path = "C:\Program Files\Nuke10.5v4\Nuke10.5.exe"


pool = "poola"
secondary_pool = "workstation"
group = "nk1004"
priority = "33"


## Parameters
first_frame = int(nuke.root()["first_frame"].getValue())
last_frame = int(nuke.root()["last_frame"].getValue())



## START
print ""
print title+" "+my_version


## PANEL
p = nuke.Panel('Simple Deadline Submitter '+my_version)    
p.addSingleLineInput('Framerange:', str(first_frame)+"-"+str(last_frame))
p.addEnumerationPulldown('Complexity:', "Simple Medium Heavy")
p.addBooleanCheckBox('Render slate', True)
p.addBooleanCheckBox('Ask for priority', False)
p.addBooleanCheckBox('Do not re-arrange frames', False)
ret = p.show()



## PROCESSING

## Framerange
framerange = p.value("Framerange:")
framerange = framerange.split("-")
first_frame = int(framerange[0])
last_frame = int(framerange[1])
framerange = str(first_frame)+"-"+str(last_frame)
middle_frame = ((last_frame-first_frame)/2+1)+first_frame
print "Framerange: "+str(first_frame)+"-"+str(last_frame)


## Complexity
complexity = p.value("Complexity:")
if complexity == "Simple":
    concurrent_tasks = str(3)
    frames_per_task = str(15)
if complexity == "Medium":
    concurrent_tasks = str(2)
    frames_per_task = str(5)
if complexity == "Heavy":
    concurrent_tasks = str(1)
    frames_per_task = str(1)
print "Concurrent tasks: "+str(concurrent_tasks)
print "Frames per task: "+str(frames_per_task)



## Command Deadline
#deadline_command_path
 #-SubmitCommandLineJob
 #-executable nuke_exe_path
 #-arguments "-start:<STARTFRAME> -end:<ENDFRAME>
  #  -width:480 -height:320 <QUOTE>\\shared\path\scene.max<QUOTE>"
 #-frames 1-10
 #-chunksize 2
 #-group 3dsmax
 #-priority 50
 #-name "3dsmax command line job"
 #-prop MachineLimit=5



cmd = '"'+deadline_command_path+'"'
cmd = cmd+' \n-SubmitCommandLineJob'
cmd = cmd+' \n-executable '+'"'+nuke_exe_path+'"'
cmd = cmd+' \n-arguments '+"t-start:<STARTFRAME> -end:<ENDFRAME> <QUOTE>"+nuke_script_path+"<QUOTE>"
cmd = cmd+' \n-frames '+framerange
cmd = cmd+' \n-name test'
cmd = cmd+' \n-chunksize '+frames_per_task
cmd = cmd+' \n-priority '+priority
cmd = cmd+' \n-pool '+pool
cmd = cmd+' \n-group '+group




print ""
print ""
print(cmd)
print ""
print ""

call(cmd)
























