# File to traverse given directory and it's subdirs and retrieve all the files
import os, argparse
import csvReader

# parser
parser = argparse.ArgumentParser(

    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Jahseem Maxwell"

)

# Add the argument to pass the fs.py program
#parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")

parser.add_argument("-lf", "--logfield", required="True", help="Field you want searched for in logs.")

#parser.add_argument("-lt", "--logterm", required="True", help="Term you want searched for in logs")

# Parse the argument
args = parser.parse_args()

rootdir = input("Please enter the directory path: ")

logField = args.logfield

#logTerm = args.logterm



# Get information from the command line
#print(sys.argv)


# Directory to traverse
#rootdir = sys.argv[1]

#print(rootdir)



# In our story, we will traverse a directory

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()


# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:

        #print(root + "/" + f)
        fileList = root + "/" + f
        #print(fileList)
        fList.append(fileList)

print(fList)

def statFile(toStat):

    # i is goin to be the variable used for each of the metadata elements
    i = os.stat(toStat, follow_symlinks=False)
    
    # arguments
    arguments = i[1]

    # hostname
    hostname = i[2]

    # name
    name = i[3]

    # path
    path = i[4]

    # pid
    pid = i[5]

    #username
    username = i[6]

    print("|{}|{}|{}|{}|{}|{}|".format(toStat, arguments, hostname, name, path, pid, username))

for eachFile in fList:

    statFile(eachFile)

    csvReader.reader(eachFile, logField)

