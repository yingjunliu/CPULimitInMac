#coding=utf8
from AppKit import NSWorkspace

def getWindowName():
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

