import sys, os
if __name__ == "__main__":
    print("Utilities was executed.")
else:
    print("Utilities was imported.")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import useful_functions
