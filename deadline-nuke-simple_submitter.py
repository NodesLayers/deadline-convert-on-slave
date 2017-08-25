## Settings
title = "Deadline: Simple Farm Submitter"
deadline_command_path = ""C:\\Program Files\\Thinkbox\\Deadline8\\bin\\deadlinecommand.exe""
nuke_script_name = os.path.basename(nuke.root().name())




first_frame = int("1")
last_frame = int("100")
middle_frame = (last_frame-first_frame)/2+1
print middle_frame










## PANEL
p = nuke.Panel('MAELSTROM WRITER '+myVersion)    
p.addEnumerationPulldown('Show:', "DNG02_MAE")
p.addEnumerationPulldown('Context:', sequence+"_"+shot)
p.addEnumerationPulldown('Render type:', 'comp precomp element')
p.addEnumerationPulldown('Format:', 'movie exr-sequence')
p.addSingleLineInput('(optional) Identifier:', '')


ret = p.show()




## Set User Variables
render_type = p.value("Render type:")
format = p.value("Format:")
ident = p.value("(optional) Identifier:")