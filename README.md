# Raspberry Pi Sense Hat Logger
**You need a Raspberry pi loaded with Raspbian Buster Lite for any of the following instructions to work**

  

- boot up the raspberry pi normally and log in with the default username and password:

```sh
Username: pi
Password: Raspberry
```

**make an empty directory in the $HOME directory and move into it by doing:**

```sh
>cd $HOME

>mkdir logger

>cd logger
```
   

download the repository which is: https://github.com/svakula/SenseHatLogger.git to your raspberry pi by doing:

  
```sh
git clone https://github.com/svakula/SenseHatLogger.git
```

**Setting up the Program**

1. Before you do anything you need to configure the data logger to start logging as soon as it powers up.

open terminal and type this in:

  
```sh

sudo nano /ect/rc.local

```

  


2. after:

  ```sh
#Print the IP address
_ip=$(hostname -I) || true
if [ "$_IP" ]; then
printf "My IP Address is %s/n" "$_IP"
fi
```

put this in and leave a space between the lines:

```sh

cd /home/pi su pi -c "SenseHatDataWrite.py" &

```
It will look like this when completed:
```sh
#Print the IP address
_ip=$(hostname -I) || true
if [ "$_IP" ]; then
printf "My IP Address is %s/n" "$_IP"
fi

cd /home/pi su pi -c "SenseHatDataWrite.py" &
```

  do ctrl+x and then 'y' then 'enter' in that order (this leaves the editor and saves the file)

 
3. type in:

 
```sh

sudo shutdown now

```
This shuts off the Raspberry pi and it is now ready to log data in its next bootup
  

when you want to log data then plug it into the car's 12v connector

  
  

All logs are written to logs.csv which should be in the same directory as the main files

  

**ignore the /// as they are for structure and clarification**
