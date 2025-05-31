import threading
import time
from concurrent.futures import ThreadPoolExecutor
def fun(seconds):
    time.sleep(seconds)
    print(f"The waiting time of execution is {seconds}")
    return seconds
#Normal code
# time1=time.perf_counter()
# t1=fun(5)
# t2=fun(3)
# t3=fun(2)
# time2=time.perf_counter()0 
# print(time2 - time1)

#Same code using thread
# time3=time.perf_counter()
# t1=threading.Thread(target=fun, args=[5])
# t2=threading.Thread(target=fun, args=[3])
# t3=threading.Thread(target=fun, args=[2])
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# time4=time.perf_counter()
# print(time4 - time3)

#advance type
def poolingDemo():
    with ThreadPoolExecutor() as executor:
    #     future=executor.submit(fun,3)
    #     print(future.result())
    #     future=executor.submit(fun,5)
    #     print(future.result())
    #     future=executor.submit(fun,2)
    #     print(future.result())
        l=[2,7,8,4]
        result=executor.map(fun,l)
        for i in result:
            print(i)

poolingDemo()