import syslogCheck
import importlib
importlib.reload(syslogCheck)
#SSH authentication failures
def ssh_fail(filename, searchTerms):

    #Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, searchTerms)

    #found list
    found = []

    #loop through the results
    for eachFound in is_found:

        #split the results up into different variables and strings
        sp_results = eachFound.split(" ")

        #Append the split value to the found list
        found.append(sp_results[8])

    #Remove duplicates by using set to conver the list to a dictionary
    hosts = set(found)

    #Print results
    for eachHost in hosts:

        print(eachHost)
