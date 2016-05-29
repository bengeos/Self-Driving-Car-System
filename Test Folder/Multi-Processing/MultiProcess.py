import os

def child():
    print 'Thi is Child Process',os.getpid()
    os._exit(0)
def parent():
    while True:
        newPID = os.fork()
        if newPID == 0:
            child()
        else:
            print 'This is Parent Process ',os.getpid()
parent()