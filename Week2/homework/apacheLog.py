import logCheck
import importlib
importlib.reload(logCheck)
#SSH authentication failures
def apache_events(filename, service, terms):

    #Call logCheck and return the results
    is_found = logCheck._logs(filename, service, terms)

    #found list
    found = []

    #loop through the results
    for eachFound in is_found:

        #split the results up into different variables and strings
        sp_results = eachFound.split(" ")

        #Append the split value to the found list
        #GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"
        found.append(sp_results[3] + " " +  sp_results[0] + " " + sp_results[1])

    #Remove duplicates by using set to convert the list to a dictionary
    getValues = set(found)

    #Print results
    for eachValue in getValues:

        print(eachValue)
