# TaskReplacer

A script capable of starting another application or file upon execution of a specified program.

# Usage

Starting the script with 
`pythonw` the script will run in the background while if it is started with `python` the script will exhibit a terminal

By running python ``.\TaskReplacer.pyw -h`` you can view aids on the arguments that you can/must pass for execution.


| Command  | Description               |             
|:---------|:--------------------------|
|`-a`      |define the application to be used after this topic |
|`-a app`  |name of the application to be replaced (with the .exe or without the .exe) |
|`-a -camera` |use as app the camera application |
|`-a -calc` |use as app the calculator application |
|`-a -chrome` |use as app the chrome application |
|`-a -paint` |use as app the paint application |
|`-a -notepad` |use as app the notepad application |
|`-a -edge` |use as app the microsoft edge application |
|`-a -word` |use as app the microsoft word application |
|`-fs` |define the file to start one app get invoked |
|`-fs file` |name of the file to be started when the application get invoked |

``pythonw .\TaskReplacer.pyw -a <app> -fs <file to run>``

Exemples: 

``pythonw .\TaskReplacer.pyw -a -calc -fs "C:\Users\Utente\Videos\1.mp4"``

``pythonw .\TaskReplacer.pyw -a Calculator -fs "C:\Users\Utente\Videos\1.mp4"``


# Disclaimer

This script has been created purely for the purposes of academic research. Project maintainers are not responsible or liable for misuse of the script. Use responsibly.