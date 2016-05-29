from multiprocessing import Process,Value,Array
import time
def child(n,a):
    for i in range(len(a)):
        if(i>0):
            print "child process: " , a[i]

if __name__ == '__main__':
    num = Value('f',0.3)
    num1 = Value('f',0.7)
    arr = Array('i',range(10000))
    t1 = time.time()
    print 'Start Time:',t1
    p = Process(target=child,args=(num,arr))
    p.start()

    for i in range(len(arr)):
            if(i>0):
                print "Prent:", arr[i]

    t2 = time.time()
    print "End Time: ",t2
    print "Difference: ",t2 - t1