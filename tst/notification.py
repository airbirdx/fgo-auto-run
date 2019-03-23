from subprocess import call

string = "It is a test notification under MacOS" 
cmd = 'display notification \"' + \
    string + '\" with title \"fgo-auto-run\"'
call(['osascript', '-e', cmd])
