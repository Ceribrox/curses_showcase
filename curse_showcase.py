import curses
import time
import os
from curses.textpad import Textbox, rectangle

#test change 

def main(stdscr):
    # Setting color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    BLACK_AND_GREEN = curses.color_pair(1)
    
    # Hides Cursor
    curses.curs_set(0)

    # Draws a rectangle and displays first lines
    rectangle(stdscr, 0, 3, 4, 23)
    stdscr.addstr(1, 6, "Matrix Showcase")
    stdscr.addstr(3, 5, "Press up to begin")
    stdscr.refresh()

    # Creating two windows and 2 pads
    win_load = curses.newwin(1, 14, 3, 8)
    win_scan = curses.newwin(2, 20, 4, 7)
    pad = curses.newpad(100, 100)
    pad_bar = curses.newpad(1, 12)

    # Adding an empty string for loading visual
    pad_bar.addstr("          ", BLACK_AND_GREEN | curses.A_REVERSE)

    # Returns key as standard KEY_KEY
    key = stdscr.getkey()

    # If KEY_UP, begin scan
    if key == "KEY_UP":
        stdscr.clear()
    
        # Printing the first line and refreshing the screen
        stdscr.addstr(1, 5, "Initializing Matrix")
        rectangle(stdscr, 0, 3, 4, 25)
        stdscr.refresh()


        # Creates a "loading" bar 
        for n in range(101):
            win_load.clear()
            color = BLACK_AND_GREEN

            #if n % 2 == 0:
                #color = BLACK_AND_WHITE
            
            win_load.addstr(f"Loading: {n}%", color)
            win_load.refresh()
            time.sleep(0.05)

        # Displays second state of title, clears the old one and refreshes the screen
        stdscr.clear()
        rectangle(stdscr, 0, 0, 18, 27)
        stdscr.addstr(1, 5, "Matrix Initialized")
        stdscr.refresh()

        # Fills the pad with random characters 100 times
        for i in range(100):
            for j in range(26):
                char = chr(67 + j)
                pad.addstr(char, BLACK_AND_GREEN)

        # Moves the pad across to show different parts of pad, and then updates "scanning" window
        for i in range(100):
            # Clears the screen, add's the scanning text to win_scan and updates based on i
            win_scan.clear()
            win_scan.addstr(f"Scanning: {i}%", color)
            win_scan.refresh()
            
            # Shows more of the loading bar based on i//10 + 7, the + 7 is to ensure it starts from the correct position
            pad_bar.refresh(0, 0, 3, 8, 3, (round(i//10) + 8))
            
            #Moves x position of pad start based on i
            pad.refresh(0, i, 6, 4, 15, 23)
            time.sleep(0.2)

        # Clears old title, displays new one and refreshes the screen
        stdscr.clear()
        rectangle(stdscr, 0, 0, 4, 25)
        stdscr.addstr(1, 5, "Matrix Complete!")
        stdscr.addstr(3, 3, "Press UP to restart")
        stdscr.refresh()

        # listens for user input again
        key = stdscr.getkey()
        
        # If KEY_UP, restart program
        if key == "KEY_UP":
            stdscr.clear()
            curses.wrapper(main)
            



# Initialize main function
curses.wrapper(main)