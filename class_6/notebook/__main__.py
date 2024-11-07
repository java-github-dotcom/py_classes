# notebook/__main__.py

import sys
import os

# Add the notebook directory to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from note_operator import BaseOperations  # Now this should work

def main():
    operations = BaseOperations()
    operations.show_menu()
    while True:
        operations.uchoice()

if __name__ == "__main__":
    main()
