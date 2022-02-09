#
import csv, sys, re
#

def urlHausOpen(filename,searchTerm):
#

    with open(filename, 'rt') as f:
        contents = csv.reader(f)

        #results = []

    for y in range(9):
        next(contents)

        print(y)
    #for keyword in searchTerm:

        #for eachLine in contents:
           # x = re.findall(r''+keyword+'',eachLine[2])

            #for z in x:

                #results.append(z)

# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
    #the_url = eachLine[2].replace("http","hxxp")
    #the_src = eachLine[4]
    #print("""
    #URL:
    #Info: 
    #{}""",format(the_url, the_src,"*"+60))
