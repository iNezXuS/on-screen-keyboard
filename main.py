import tkinter as tk
import ctypes
from ctypes import wintypes

# Necessary configurations to use Windows API functions
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Constants
WM_SETTEXT = 0x000C  # Message for setting the text of a window

class VirtualKeyboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("On-Screen Keyboard")  # Title of the window
        self.root.attributes('-topmost', True)  # Keep the window always on top
        self.root.overrideredirect(True)  # Remove the window frame

        # Key mapping
        self.key_mappings = {
            "'": "'",
            '"': '"',
            '(': '(',
            ')': ')',
            '=': '=',
            '&': '&',
            '!': '!',
            '{': '{',
            '}': '}',
            '[': '[',
            ']': ']',
            '$': '$'
        }
        
        self.create_ui()  # Create the user interface

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=5, pady=5)
        row = 0
        col = 0
        
        # Create buttons for each symbol in the key mappings
        for symbol in self.key_mappings.keys():
            btn = tk.Button(
                frame,
                text=symbol,
                width=4,
                height=2,
                command=lambda s=symbol: self.send_key(s)  # Send the key when clicked
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def send_key(self, symbol):
        try:
            # Find the window by its title
            hwnd = user32.FindWindowW(None, "Target Window Title")  # Replace with your target window title
            if hwnd:
                # Find the text box within the target window
                edit_hwnd = user32.FindWindowExW(hwnd, None, "Edit", None)  # Replace "Edit" with the class name of the text box if needed
                if edit_hwnd:
                    # Send the character to the text box
                    ctypes.windll.user32.SendMessageW(edit_hwnd, WM_SETTEXT, 0, symbol)
                    print(f"Key sent: {symbol}")  # Log the sent key
                else:
                    print("Text box not found.")
            else:
                print("Window not found.")
        except Exception as e:
            print(f"Error: {e}")  # Log any errors

    def run(self):
        self.root.mainloop()  # Start the Tkinter main loop

if __name__ == "__main__":
    keyboard = VirtualKeyboard()  # Create an instance of the virtual keyboard
    keyboard.run()  # Run the application
