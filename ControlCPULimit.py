import MacAPITool
import CommandTool
import time

_interval = 1

def startControl(argv):
    CommandTool.killCPUThrottles()
    pid = CommandTool.getPIDFormAppName(argv[1])
    windowName = argv[2]
    limit = argv[3]
    while True:
        time.sleep(_interval)
        if windowName == str(MacAPITool.getWindowName().encode('utf8')):
            CommandTool.killCPUThrottles()
        else:
            CommandTool.startCPUThrottles(pid, limit)

