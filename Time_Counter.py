import time

def time_countdown(sec_input):
    
    
    while(sec_input>0):
        mins=int(sec_input/60)
        secs=int(sec_input%60)
        current_time='{:02d}:{:02d}'.format(int(mins), int(secs))
        print(current_time,end='\r')
        time.sleep(1)
        sec_input=sec_input-1
    print("00:00\nTime's up!") 
    
    

sec_input=int(input("Enter time in secs: "))
time_countdown(sec_input)