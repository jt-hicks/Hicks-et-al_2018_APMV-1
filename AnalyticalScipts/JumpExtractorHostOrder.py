#JumpExtractor.py: Extracts Markov jump counts from a directory of complete jump history log files.
#Author: Joseph Hicks

import re, os
import pandas as pd


def extractor(dirname, history):
    os.chdir(dirname)
    print(os.getcwd())
#   Specifies categories depending on the log file name
    if "ClassI_HostOrder" in history:
        source = ['ANS', 'CHA', 'CHI', 'Older']
    elif "ClassI_USRegion" in history:
        source = ["AK","MW","NE","S","W","X","UN"]
    elif "ClassI_WorldGeo" in history:
        source = ["EastAsia","Europe","CentralAsia","NorthAmerica","UN"]
    elif "ClassII_HostOrder" in history:
        source = ["ANS","CHI","COL","GAL","PSI","SUL","Older"]
    elif "ClassII_USRegion" in history:
        source = ["AK","MW","NE","P","S","W","X","UN"]
    elif "ClassII_WorldGeo" in history:
        source = ["Africa","CentralAmerica","CentralAsia","EastAsia","Europe","MiddleEast","NorthAmerica","SouthAmerica","SouthAsia","SoutheastAsia","Older"]

    results = pd.DataFrame(columns=['Year', 'Source', 'Sink', 'Count'])

#   Summarize annual jump counts for each jump type for the most recent 20 years. 
    for clock in range(20):
        count = {}
        infile = open(os.path.join(dirname, history), "r")
        infile.readline()
#       Status of program.
        print("Working on year {} of 30 for {}".format(clock, history))
#       Format log lines to easily parse jump types and times
        for line in infile:
#            print("Line read")
            cleanline1 = re.sub(r'.+\t', '', line)
            cleanline2 = re.sub(r'\s\d+', '', cleanline1)
            cleanline3 = re.sub(r'{{','{', cleanline2)
            cleanline4 = re.sub(r'}}\n','',cleanline3)
#            print(cleanline4)
            jumps = cleanline4.split("},{")
            for i in jumps:
                packet = i.split(",")
                year = eval(packet[1])
                if year <= (clock + 1) and year > clock:
                    if packet[2] + "\t" + packet[3] in count:
                        count[packet[2] + "\t" + packet[3]] += 1
                    else:
                        count[packet[2] + "\t" + packet[3]] = 1
        infile.close()
#       Specify that jump types with no counts = 0
        for x in source:
            for y in source:
                if x != y:
                    if x + "\t" + y not in count:
                        count[x + "\t" + y] = 0
        report = list(count.items())
        report.sort()
#       Create jump history report files.
        for item in report:
            locations, average = item
            separated = locations.split('\t')
            row = pd.DataFrame(
                {'Year': [clock], 'Source': [separated[0]], 'Sink': [separated[1]], 'Count': [average / 9001]})
            results = results.append(row, ignore_index=True)
    results.to_csv(dirname + '/JumpHistory/' + 'Counts_' + history + '.txt', index=False, sep='\t')


def main():
    dirname = input("Enter directory path: ")
    os.chdir(dirname)
    print(os.getcwd())
    os.makedirs('./JumpHistory')
#   Loop through all files within the directory, ignoring the JumpHistory folder and the Mac OS file ".DS_Store"
    for filename in os.listdir('.'):
        if filename != '.DS_Store' and filename != 'JumpHistory':
            extractor(dirname, filename)


main()
