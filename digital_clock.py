import time
from datetime import datetime
import os

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def digital_clock():
    """Display a digital clock in the terminal."""
    try:
        while True:
            clear_terminal()
            current_time = datetime.now().strftime("%H:%M:%S")
            current_date = datetime.now().strftime("%A, %d %B %Y")
            print('\nDigital Clock')
            print(f"Date: {current_date}")
            print(f"Time: {current_time}")
            time.sleep(1)

    except KeyboardInterrupt:
        clear_terminal()
        print("\nClock stopped. Goodbye!")

if __name__ == "__main__":
    digital_clock()