#This creates an interface to search through csv files. You must import re and sys
import re, sys, csv


#function that allows us to read the contents of the file and search for a keyword
def urlHausOpen(filename, searchTerm):
#There are multiple indentation issues 

#Opens the Csv file
#The while statement needed to be a with statement
#filename is a placeholder argument and missing the read only aspect
    with open('urlHausTestDataSet.csv', 'r') as yf:
        #There only needs to be one equal sign
        contents = csv.reader(filename)
#Query the Csv file for the 'term' or direction and retrieve the strings to search on
#terms= contents['.edu, .gov']

    terms = contents[searchTerm]

    listOfTerms = terms.split(",")

    with open(filename) as f:

        contents = f.readLines()

        results = []

    for eachLine in contents:

        for eachKeyword in listOfTerms:
            #must add a quotation mark when utilizing the re module
            #get rid of the [2] which decides the index
            x = re.findall(r''+eachKeyword+'', eachLine)

        for present in x:

            results.append(present)

# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
    the_url = eachLine[2].replace("http","hxxp")
    the_src = eachLine[4]
    print("""
    URL:
    Info: 
    {}""",format(the_url, the_src,"*"+60))

    if len(results) == 0:
        print("No Results")
        sys.exit(1)
    
    results = sorted(results)

    return results