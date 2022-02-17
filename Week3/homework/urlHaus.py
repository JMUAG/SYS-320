import csv, re, sys

def urlHausOpen(filename, searchTerm):

    with open('../../Logs/urlHausTestDataSet.csv')as f:
        contents = csv.reader(f)

        for _ in range(9):
            next(contents)

        for keyword in searchTerm:

            for eachLine in contents:

                x=re.findall(r''+keyword+'', eachLine[2])

                for _ in x:
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
                    the_url = eachLine[2].replace("http","hxxp")
                    the_src = eachLine[6]
                    print("""
                    URL:{}
                    Info: {}
                    {}""".format(the_url, the_src,"*"*60))