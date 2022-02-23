import logcheck
import importlib
importlib.reload(logcheck)
#Shell event monitoring
def result_events(filename, service, terms):

    #Call logCheck and return the results
    is_found = logcheck._logs(filename, service, terms)

    #found list
    found = []

    #loop through the results
    for eachFound in is_found:

        #split the results up into different variables and strings
        sp_results = eachFound.split(" ")

        #Append the split value to the found list
        #QQ.exe - tcpconn.tencent.com:80 close, 133 bytes sent, 0 bytes received
        found.append(
            sp_results[0] + " " +
            sp_results[2]
            + " " + sp_results[3] 
            + " " + sp_results[4] 
            + " " + sp_results[5]
            + " " + sp_results[6] 
            + " " + sp_results[7] 
            #+ " " + sp_results[8]
            #+ " " + sp_results[9] 
            )
        
    #Remove duplicates by using set to convert the list to a dictionary
    getValues = set(found)

    #Print results
    for eachValue in getValues:

        print(eachValue)

    return