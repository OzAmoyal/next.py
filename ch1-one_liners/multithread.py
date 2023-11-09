import threading
import time
def func():
    print('ran at '+time.strftime('%H:%M:%S')+ ' by '+threading.current_thread().name)
    time.sleep(1)
    print('done')

x = threading.Thread(target=func)
y=threading.Thread(target=func)
x.start()
y.start()