#Send an email using Powershell

#Creates an array that can send emails to multiple addresses
$toSend = @('email@champlain.edu', 'stor@champlain.edu', 'duns@champlain.edu')

#Message body
$msg = "Hello"

while ($true) {
    foreach ($email in $toSend) {


#Send the email
        Write-Host "Send-MailMessage -from 'email@champlain.edu' -To 'email@champlain.edu' -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"

        #Pause for 1 second
        start-sleep 1
    }
}