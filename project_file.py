import pyttsx3
import os

pyttsx3.speak("Welcome to my tools")


while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	

	if ("run" in p)  and ("chrome" in p):
	  os.system("chrome")

	elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif ("run" in p)  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")

	elif (("run" in p) or  ("open" in p )) and  (("calculator" in p) or ("calc" in p) ) :
	  os.system("calc")

	elif (("run" in p) or  ("open" in p )) and  ("calendar" in p) :
	  os.system("start outlookcal:")		 	
	
	elif (("run" in p) or  ("open" in p )) and  (("clock" in p) or ("Alarm" in p)) :
	  os.system("start ms-clock:")	 	
	
	elif (("run" in p) or  ("open" in p )) and  (("paint" in p) or ("ms paint")) :
	  os.system("mspaint")	
	
	elif (("run" in p) or  ("open" in p )) and  ("task manager" in p) :
	  os.system("taskmgr")	 	
		
	elif (("run" in p) or  ("open" in p )) and  (("file explorer" in p) or ("file manager")) :
	  os.system("explorer")	 	

	elif (("run" in p) or  ("open" in p )) and  ("chracter map" in p) :
	  os.system("charmap")	 	

	elif (("run" in p) or  ("open" in p )) and  ("3d builder " in p) :
	  os.system("start com.microsoft.builder3d:")

	elif (("run" in p) or  ("open" in p )) and  ("camera" in p) :
	  os.system("start microsoft.windows.camera")

	elif (("run" in p) or  ("open" in p )) and  (("help" in p) or ("get help")):
	  os.system("start ms-contact-support:")

	elif (("run" in p) or  ("open" in p )) and  ("mail" in p) :
	  os.system("start outlookmail:")

	elif (("run" in p) or  ("open" in p )) and  ("maps" in p) :
	  os.system("start bingmaps:")		

	elif (("run" in p) or  ("open" in p )) and  ("Microsoft edge" in p) :
	  os.system("start microsoft-edge:") 

	elif (("run" in p) or  ("open" in p )) and  ("Microsoft store" in p):
	  os.system("start ms-windows-store:")

	elif (("run" in p) or  ("open" in p )) and  (("photos" in p) or ("image")):
	  os.system("start ms-photos:")

	elif (("run" in p) or  ("open" in p )) and  ("screen snip" in p):
	  os.system("start ms-screensnip:")	


	elif (("run" in p) or  ("open" in p )) and  ("settings" in p) :
	  os.system("start ms-settings:")

	elif (("run" in p) or  ("open" in p )) and  ("snip & sktech" in p) :
	  os.system("start ms-ScreenSktech:")

	elif (("run" in p) or  ("open" in p )) and  ("Tips" in p) :
	  os.system("start ms-get-started:")

	elif (("run" in p) or  ("open" in p )) and  ("Weather" in p) :
	  os.system("start bingweather:")

	elif (("run" in p) or  ("open" in p )) and  ("windows mixed reality environments" in p) :
	  os.system("start ms-environment-builder:")

	elif (("run" in p) or  ("open" in p )) and  ("parantel controls" in p) :
	  os.system("start ms-wps:")

	elif (("run" in p) or  ("open" in p )) and  ("Xbox" in p) :
	  os.system("start xbox:")

	elif (("run" in p) or  ("open" in p )) and  (("Feedback Hub" in p) or ("feedback")):
	  os.system("start feedback-hub:")
	 		
	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("dont support")

