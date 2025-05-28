import time

try:
    while True:
    
        current_time = time.strftime("%I:%M:%S %p")  
        print("========================")
        print("     DIGITAL CLOCK      ")
        print("========================")
        print(f"       {current_time}  ")
        print("========================")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nClock stopped.")


# def show_clock():
#     current_time = time.strftime("%I:%M:%S %p")
#     print("========================")
#     print("     DIGITAL CLOCK      ")
#     print("========================")
#     print(f"       {current_time}  ")
#     print("========================")
#     time.sleep(1)
#     show_clock()  # Recursive call

# show_clock()  #  File "d:\program\py\digita_watch.py", line 26, in show_clock show_clock()  # Recursive call   #KeyboardInterrupt
