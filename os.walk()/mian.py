#!/usr/bin/python3

#os.walk(preferpath): will output three parameter namely :dirpath,dirnames,filenames

import sys,os 

preferpath='./test/'

for dirpath,dirnames,filenames in os.walk(preferpath):
    # for filename in filenames:
    print ("dirpath: {}".format(dirpath))
    print ("dirnames: {}".format(dirnames))
    print ("filenames: {}".format(filenames))
        # if filename == 'temp1_input':
        #     value_node=os.path.join(dirpath,filename)
        # elif filename == 'temp1_max':
        #     max_node=os.path.join(dirpath,filename)
        # elif filename == 'temp1_max_hyst':
        #     min_node=os.path.join(dirpath,filename)