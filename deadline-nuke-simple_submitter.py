## Settings
title = "Deadline: Simple Farm Submitter"
my_version = "v0.1"
deadline_command_path = "C:\\Program Files\\Thinkbox\\Deadline8\\bin\\deadlinecommand.exe"
nuke_script_name = os.path.basename(nuke.root().name())
prio_message = "Request Priority"


## Parameters
first_frame = int(nuke.root()["first_frame"].getValue())
last_frame = int(nuke.root()["last_frame"].getValue())



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



middle_frame = ((last_frame-first_frame)/2+1)+first_frame
#print middle_frame

