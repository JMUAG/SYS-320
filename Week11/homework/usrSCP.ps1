#Array of websites containing threat intel
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules', 'https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

#Loop through the URL's for the rules list

foreach ($u in $drop_urls) {

    #Extract the filename
    $temp = $u. split("/")
    #Split takes a string and turns it into an array

    #The last element in the array plucked off is the filename
    $file_name = $temp[-1]

    if (Test-Path $file_name){

        continue
    } else {

    
        #Download the rules list
        Invoke-WebRequest -Uri $u -OutFile $file_name

        }#Close the if statement

}#close the foreach loop

#Array containing the filename
$input_paths = @('.\compromised-ips.txt', '.\emerging-botcc.rules')
#Extract the IP Adresses
#108.190.109.107
#108.191.2.
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

#Append the IP Address to the temporary IP list
select-string -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "ips-bad.tmp"

#Get the IP addresses discovered, loop through and replace the beginning of the line with the IPTables syntax
#After the IP address, add the remaining IPTables syntax and save the results to a file
#iptables -A INPUT -s 108.191.2.72 -j DROP
(Get-Content -Path ".\ips-bad.tmp") | % `
{ $_ -replace "^","iptables -A INPUT -s " -replace "$", " -j DROP"} | `
Out-file -FilePath "C:\Users\benhacked.EMUL\Desktop\SYS-320-SP22\Week11\homework\iptables.bash"


#$usrInput = Read-Host -Prompt "Please Enter Windows or IPTables"

<#switch ( $usrInput )
{
    IPTables {(Get-Content -Path ".\ips-bad.tmp") | % `
    { $_ -replace "^", "iptables -A INPUT -s " -replace "$", " -j DROP"} | `
    Out-File -FilePath ".\Week11\homework\iptab.bash" | Set-SCPItem -ComputerName '192.168.6.71' -Port 2222 -Credential (Get-Credential jahseem.maxwell) `
    -Destination '/home/jahseem.maxwell' -Path '.\Week11\homework\iptab.bash'}
 
    Windows {(Get-Content -Path '.\ips-bad.tmp') | % `
    {"netsh advfirewall add rule name=`"IP blocking $_`" action=block dir=in remoteip=$_"} | `
    Out-File -FilePath ".\Week11\homework\IPBlocking.bat" | `
    Set-SCPItem -ComputerName '192.168.6.71' -Port 2222 -Credential (Get-Credential jahseem.maxwell) `
    -Destination '/home/jahseem.maxwell' -Path '.\Week11\homework\IPBlocking.bat' }

}
#>
Set-SCPItem -ComputerName '192.168.6.71' -Port 2222 -Credential (Get-Credential jahseem.maxwell) `
-Destination '/home/jahseem.maxwell' -Path '.\Week11\homework\IPBlocking.bat'