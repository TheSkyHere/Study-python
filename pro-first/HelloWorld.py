#!/usr/bin/python3
import sys,os 

print ("morton1")
# raw_input()
def is_dir_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False


def PrintSomeThing(): 
    print(os.path.dirname(os.sys.argv[1])) 
    # raw_input() 
    print ("123456789") 
    preferpath='/home/morton/workspace/Study/Study-python/pro-first/hwomon/hwomon12/temp1_input'
    if is_dir_exist(preferpath):
        print ("yes")
    else:
        print ("no")

if __name__ == "__main__":
    print ("test 0 morton")
    PrintSomeThing() 
    print ("test--morton")

