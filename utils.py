import sys 
import time

# for waiting calculation
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
def run_spinning_cursor(): 
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    sys.stdout.write('\b')
    
