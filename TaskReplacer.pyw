import asyncio
import subprocess
from os import startfile as fstart
import time

import sys

application = 'WindowsCamera.exe'
ftoexecute = ''
apps = {}
apps["-camera"] = 'WindowsCamera.exe'
apps["-calc"] = 'Calculator.exe'
apps["-chrome"] = 'chrome.exe'
apps["-paint"] = 'mspaint.exe'
apps["-notepad"] = 'notepad.exe'
apps["-discord"] = 'discord.exe'
apps["-edge"] = 'msedge.exe'
apps["-word"] = 'WINWORD.EXE'

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist', shell=True))
    if process_name in progs:
        return True
    else:
        return False

async def execute():
    while not process_exists(application):
        time.sleep(0.500)
    fstart(f"{ftoexecute}")
    subprocess.call(f"taskkill /IM {application} /F")
    

def applicationasexe( app ):
    if app in apps.keys():
        return apps[app]
    if not app.endswith(".exe"):
        return app + ".exe"
    else:
        return app

def instructions():
    print(f"usage: python {sys.argv[0]} ... [-a app | -fs file ]")
    print("Options and arguments (and corresponding environment variables):")
    print("-a\t\t : define the application to be used after this topic")
    print("-a app\t\t : name of the application to be replaced (with the .exe or without the .exe)")
    print("-a -camera\t : use as app the camera application")
    print("-a -calc\t : use as app the calculator application")
    print("-a -chrome\t : use as app the chrome application")
    print("-a -paint\t : use as app the paint application")
    print("-a -notepad\t : use as app the notepad application")
    print("-a -edge\t : use as app the microsoft edge application")
    print("-a -word\t : use as app the microsoft word application")
    print("-fs\t\t : define the file to start one app get invoked")
    print("-fs file\t : name of the file to be started when the application get invoked")

if __name__=='__main__':  
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "-help":
            instructions()
            exit()
        elif sys.argv[1] == "-a":
            application = applicationasexe( sys.argv[2] )
            if sys.argv[3] == "-fs":
                ftoexecute = sys.argv[4]
                loop = asyncio.get_event_loop()
                loop.run_until_complete(execute())
                loop.close()
        elif sys.argv[1] == "-fs":
            ftoexecute = sys.argv[2]
            if sys.argv[3] == "-a":
                application = applicationasexe( sys.argv[4] )
                loop = asyncio.get_event_loop()
                loop.run_until_complete(execute())
                loop.close()
        else:
            instructions()
            exit()