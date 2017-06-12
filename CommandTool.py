import os


def getPIDFormAppName(appName):
    lines = os.popen("ps -axo 'pid, command' | grep '%s' | grep -v 'grep\|Limit'" % appName).readlines()
    if len(lines) > 1:
        print ("There are more than one process have Same appName: \n" + lines)
        exit(0)
    elif len(lines) == 0:
        print ("There is no running app name: " + appName)
        exit(0)
    else:
        return getPID(lines[0])


def getPID(record):
    return str.split(record.strip(), ' ')[0]


def killCPUThrottles():
    lines = os.popen("ps -axo 'pid, command' | grep 'cputhrottle' | grep -v 'grep'").readlines()
    for line in lines:
        pid = getPID(line)
        os.popen("kill %s" % pid)

def killLimitSelf():
    lines = os.popen("ps -axo 'pid, command' | grep 'Limit' | grep -v 'grep' | grep -v 'unLimit'").readlines()
    for line in lines:
        if line.find("sudo") != -1:
            pid = getPID(line)
            os.popen("kill %s" % pid)


def checkCPUThrottles(pid):
    lines = os.popen("ps -axo 'pid, command' | grep 'cputhrottle' | grep -v 'grep' | grep '%s'" % pid).readlines()
    if len(lines) > 0:
        return False
    else:
        return True

def startCPUThrottles(pid, limit):
    if checkCPUThrottles(pid):
        os.popen("cputhrottle %s %s &" % (pid, limit))
