#Get a list of running processes
#Get-process

#Get list of members
#Get-process | Get-member

#Get a list of processes: name, id, path
#Get-process | Select-Object ProcessName, id, Path 

#Save the output to a CSV file
#Get-process | Select-Object ProcessName, id, Path | Export-csv -Path "\Users\jahseem\Desktop\processes.csv"

$outputName = "\Users\jahseem\Desktop\processes.csv"

#System Services and Properties
#Get-Service | Get-member 
#Get-Service | select-object Status, Name, DisplayName, BinaryPathName | Export-csv -Path $outputName

#Get a list of running services
# $_. = To access the properties of a commandlet in powershell
# -eq = "equal"

Get-service | Where-object { $_.Status -eq "Running" } | Export-csv -Path $outputName

#Check to see if the file exists
if ( Test-path $outputName ){

    write-host -backgroundcolor "Green" -foregroundcolor "White" "Services file was created!"

} else {
    write-host -backgroundcolor "red" -foregroundcolor "White" "Services file was not created!"
}

