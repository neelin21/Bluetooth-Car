import os
import pyAIML
from Bot_Predicates import setBotProperties
import sys

# Create the kernel and learn AIML files
kernel = pyAIML.Kernel()

sys.setrecursionlimit(100000) # 10000 is an example, try with different values

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "AIML_Files/startup.xml")
    kernel.learn("AIML_Files/*.aiml")
    kernel.saveBrain("bot_brain.brn")

#sets bot properties
setBotProperties(kernel)

# Press CTRL-C to break this loop
while True:
             
    message = raw_input(">>>")
    
    if message == "learn":
        print "Learning in progess..."
        kernel.learn("AIML_Files/*.aiml")
        kernel.saveBrain("bot_brain.brn")
    elif message == "save":
        print "Saving..."
        kernel.saveBrain("bot_brain.brn")
    elif message == "erase":
        print "Deleting..."
        os.remove("bot_brain.brn")
    elif message == "goodbye":
        print kernel.respond(message)
        exit()
    else:
        print kernel.respond(message)

#Fix what do you want to talk about scenerio
