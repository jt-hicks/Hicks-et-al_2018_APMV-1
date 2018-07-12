#JumpExtractor.py: Extracts Markov jump counts from a full jump history log file.

def main():
    #source = ['Africa','CentralAmerica','CentralAsia','EastAsia','Europe','MiddleEast','NorthAmerica','Oceania','SouthAmerica','SouthAsia','SoutheastAsia']
    #source = ['EastAsia','Europe','CentralAsia','NorthAmerica']
    #source = ['ANS','CHI','COL','GAL','PSI','SUL']
    source = ['AK','MW','NE','P','S','W','X']
    for clock in range(30):
        infile = open("ClassII_USRegion_MJ_050418jumpHistoryComb.log", "r")
        count = {}
        for line in infile:
            jumps = line.split("},{")
            for i in jumps:
                packet = i.split(",")
                year = eval(packet[1])
                if year <= (clock+1) and year > clock:
#                    count[packet[2] + " " + packet[3]] = count.get(packet[2]+" "+packet[3],0) + 1/500
                    if packet[2]+" "+packet[3] in count:
                        count[packet[2]+" "+packet[3]] += 1/1500
                    else:
                        count[packet[2]+" "+ packet[3]] = 1/1500
        for x in source:
            for y in source:
                if x != y:
                    if x+" "+y not in count:
                        count[x+" "+y] = 0
        report = list(count.items())
        report.sort()
        for item in report:
            locations, average = item
            print(clock,locations,average)
    infile.close()
    infile = open("ClassII_USRegion_MJ_050418jumpHistoryComb.log", "r")
    count = {}
    for line in infile:
        jumps = line.split("},{")
        for i in jumps:
            packet = i.split(",")
            if packet[2]+" "+packet[3] in count:
                count[packet[2]+" "+packet[3]] += 1/1500
            else:
                count[packet[2]+" "+ packet[3]] = 1/1500
    for x in source:
        for y in source:
            if x != y:
                if x+" "+y not in count:
                    count[x+" "+y] = 0
    report = list(count.items())
    report.sort()
    print("Total Counts:")
    for item in report:
        locations, average = item
        print(locations,average)
    infile.close()
main()