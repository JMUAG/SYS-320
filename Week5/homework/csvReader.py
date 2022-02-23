import csv, re

def reader(filename, searchTerm):

    with open(filename)as f:
        contents = csv.reader(f)

        results = []

        for x in range(7):
            next(contents)

        for keyword in searchTerm:

            for eachLine in contents:
                xx = str(eachLine)
                searcher=re.findall(r''+keyword+'', xx)

                for search in searcher:
                    results.append(search[2])

            print(results)
                
                
