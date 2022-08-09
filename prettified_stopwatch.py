import time
import pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                     # press Enter to begin
print('Started.')
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1


# Start tracking the lap times.
lapString = ''
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapString += 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(8), str(lapTime).rjust(7))
        lapString += '\n'
        print('Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(8), str(lapTime).rjust(7)), end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy(lapString)
    print('\nDone.')


#print('\n')
#print(pyperclip.paste())
