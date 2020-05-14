**You need a Raspberry pi loaded with Raspbian Buster Lite for any of the following instructions to work**

boot up the raspberry pi normally and log in with the default username and password which are 'pi' and 'raspberry' respectively.

make an empty directory in the $HOME directory and move into it by doing:

//
cd $HOME
mkdir logger
cd logger
//

download the repository which is: [LINK] to your raspberry pi by doing:

//
git clone [LINK]
//


**Instructions for automatic control**

Before you do anything you need to configure the data logger to start logging as soon as it powers up.

open terminal and type this in:

//
sudo nano /ect/rc.local
//


after:

//
#Print the IP address
_ip=$(hostname -I) || true
if [ "$_IP" ]; then
   printf "My IP Address is %s/n" "$_IP"
fi
//

put this in and leave a space between the lines:

//
cd /home/pi su pi -c "SenseHatDataWrite.py" &
//

do ctrl+x and then 'y' then 'enter' in that order (this leaves the editor and saves the file)

type in:

//
sudo shutdown now
//

when you want to log data then plut it into the car's 12v connector


All logs are written to logs.csv

**ignore the /// as they are for structure and clarification**