import threading
import time

def update_db():
    print("updating...")
    time.sleep(5)
    print("updated")
    
def nums(n):
    for i in range(1,n+1):
        print(i)
        
# update_db()
t1 = threading.Thread(target=update_db)
t1.start()
 
nums(6)

print(threading.active_count())
print(threading.enumerate())

t1.join()
print("finished")