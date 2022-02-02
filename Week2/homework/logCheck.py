#Create an interface to search through syslog files
import re, sys, yaml

# Open the Yaml file
try:

    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strerror)

def _logs(filename, service, term):

    #Query the Yaml file for the 'term' or direction and retrieve the strings to search on
    #terms= keywords['apache']['php']
    terms = keywords[service][term]

    listOfKeywords = terms.split(",")
    #Open a file
    with open(filename) as f:

        #read in the file and save it to a variable
        contents = f.readlines()

        #lists to store the results
        results = []

    #loop through the list returned. Each element is a line from the syslog file
    for line in contents:
        
        #loops through keywords
        for eachKeyword in listOfKeywords:

            #if the 'line' contains the keyword then it will print
            #if eachKeyword in line: 
            #searches and returns results using a regular expression search
            x = re.findall(r''+eachKeyword+'', line)
            # print(x)
            for found in x:

                #Append the return keywords to the results list
                results.append(found)

    #Check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    #Sort the list
    results = sorted(results)   

    return results
    #print(x)