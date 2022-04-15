#List the files in a directory and 
# List all files and print the full path.
# Get-ChildItem -Recurse -Include *.pdf,*.docx,*.txt -Path .\Week12\class\Documents | select FullName

Get-ChildItem -Recurse -Include *.pdf,*.docx,*.txt -Path ..\SYS-320-SP22\ |Export-Csv `
-Path ./Week12/class/xtra.csv

# Import CSV File
$listFile = import-csv -Path ./Week12/class/xtra.csv -header FullName
# $flistFile


# Loop through the results
foreach ($x in $listFile) {

    Get-ChildItem -Path $x.FullName

}