import sys
import json
import datetime

if __name__=='__main__':
    jsonFile = sys.argv[1] # Takes input values as per terminal
    inputFile = open(jsonFile, "r")
    metadata = json.load(inputFile)
    print datetime.datetime.fromtimestamp(metadata['createdAt'])
