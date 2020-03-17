import sys, os
scriptpath = os.path.abspath(__file__)
scriptbase = os.path.dirname(scriptpath)
sourcebase = os.path.dirname(scriptbase)
sys.path.insert(0, sourcebase)