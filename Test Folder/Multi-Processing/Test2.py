from multiprocessing import Process,Value,Array,Pool
import time
def child(n,a):
    n.value = 3.1415927
    for i in range(len(a)):
        if(i>0):
            a[i] = -a[i]
            print 'Child Process: ',a[i]
            time.sleep(0.01)
    return 1
if __name__ == '__main__':
    g = Pool()

    with Pool(processes=5) as p:
        num = Value('d',0.0)
        arr = Array('i',range(100))
        p.map(child,(num,arr))