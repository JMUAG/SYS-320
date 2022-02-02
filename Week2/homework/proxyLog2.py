import proxyCheck
import importlib
importlib.reload(proxyCheck)
#SSH authentication failures
def proxy_events(filename, service, terms):

    #Call logCheck and return the results
    is_found = proxyCheck._logs(filename, service, terms)

    #found list
    found = []

    #loop through the results
    for eachFound in is_found:

        #split the results up into different variables and strings
        sp_results = eachFound.split(" ")

        #Append the split value to the found list
        #QQPlayer.exe - btrace.qq.com:80 open through proxy proxy.cse.cuhk.edu.hk:5070 HTTPS
        found.append(sp_results[0] + " " +  sp_results[2] + " " + sp_results[3] + " through proxy " + sp_results[6])
        
    #Remove duplicates by using set to convert the list to a dictionary
    getValues = set(found)

    #Print results
    for eachValue in getValues:

        print(eachValue)

    return