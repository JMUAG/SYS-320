# File to traverse given directory and it's subdirs and retrieve all the files
import os, argparse
import result_print

# parser
parser = argparse.ArgumentParser(

    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Jahseem Maxwell"

)

# Add the argument to pass the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")

parser.add_argument("-lf", "--logfield", required="True", help="Field you want searched for in logs.")

parser.add_argument("-lt", "--logterm", required="True", help="Term you want searched for in logs")

# Parse the argument
args = parser.parse_args()

rootdir = args.directory

logField = args.logfield

logTerm = args.logterm



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
    
    # mode
    mode = i[0]

    #inode
    inode = i[1]

    #uid
    uid = i[4]

    #gid
    gid = i[5]

    # file size
    fsize = i[6]

    print("|{}|{}|{}|{}|{}|{}|".format(toStat, inode, mode, uid, gid, fsize))

for eachFile in fList:

    statFile(eachFile)


    results = result_print.result_events(eachFile, logField, logTerm)
    

    


#




