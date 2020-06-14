import time
import webbrowser

count=0
num_of_breaks=2
time_intervals=60

print ("This program started on "+time.ctime())
while count<num_of_breaks:
    time.sleep(time_intervals)
    webbrowser.open("https://www.youtube.com/watch?v=4Tr0otuiQuU")
    count=count+1
