import time 

# use time.time() to get the time in seconds

'''x = time.time()
elapsed = 0
numbers = 0

while True:
    y = time.time
    elapsed = int(numbers
'''
start_time = time.time()
end_time = time.time()
time_difference = (end_time - start_time)
old_time_difference = (time_difference)

while True:
    end_time = time.time()
    time_difference = int(10000*end_time - 10000*start_time)
    if time_difference != old_time_difference:
        print(time_difference)
    old_time_difference = time_difference

