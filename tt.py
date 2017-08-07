#!c:\tools\Python\Python35\python.exe -u
''' My Track Time
' Track Time will track my IBM activity: Running in Background, it will recognize whether screen is unlocked
'    to start recording times.
' Usage: tt <key> : Set current work activity (educ, avp, l2, pause, other); defaults to pause
'       tt export: Export values to Excel or so
'       tt day|week: Sum billable time today | this week so far
'''

''' Find whether the workstation is locked: 
http://timgolden.me.uk/python/win32_how_do_i/see_if_my_workstation_is_locked.html
import time
import ctypes

user32 = ctypes.windll.User32
OpenDesktop = user32.OpenDesktopW
SwitchDesktop = user32.SwitchDesktop
DESKTOP_SWITCHDESKTOP = 0x0100

user32.LockWorkStation ()
#
# Slight pause to overcome what appears to
# be a grace period during which a switch
# *will* succeed.
#
time.sleep (1.0)

while 1:
  hDesktop = OpenDesktop ("default", 0, False, DESKTOP_SWITCHDESKTOP)
  result = SwitchDesktop (hDesktop)
  if result:
    print "Unlocked"
    break
  else:
    print time.asctime (), "still locked"
    time.sleep (2)
'''

'''  Find whether Notes is running:
import psutil    
"someProgram" in (p.name() for p in psutil.process_iter())
"nlnotes.exe" in (p.name() for p in psutil.process_iter())
'''

import time
import ctypes
import psutil

user32 = ctypes.windll.User32
OpenDesktop = user32.OpenDesktopW
SwitchDesktop = user32.SwitchDesktop
DESKTOP_SWITCHDESKTOP = 0x0100


#
# Slight pause to overcome what appears to
# be a grace period during which a switch
# *will* succeed.
#


while 1:
    hDesktop = OpenDesktop ("default", 0, False, DESKTOP_SWITCHDESKTOP)
    result = SwitchDesktop (hDesktop)
    if not result:
        print("Screen Locked")
        break

    if "nlnotes.exe" in (p.name() for p in psutil.process_iter()):
        print("Notes not running")
        break

    print("running")

