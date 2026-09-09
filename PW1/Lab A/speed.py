from decay import simulate_loop, simulate
import time
N0=20000
start=time.perf_counter()
simulate_loop(20000,0.4)
ltime=time.perf_counter()-start 
start=time.perf_counter()
simulate(20000,0.4)
ntime=time.perf_counter()-start 
print("loop time",ltime)
print("numpy time",ntime)
print(f"Numpy is {ltime/ntime} times faster")
