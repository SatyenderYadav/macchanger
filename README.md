# macchanger
A simple and easy script to change your MAC address in Linux. 

# Setup
1. Download and open repo directory.

2. Add your linux root password in "yourpassword" in mac.py

3. Copy your mac.py file in /bin/mac
         
         git clone https://github.com/aks060/macchanger.git
         
         cd macchanger
         
          # set your password in mac.py
          
         sudo cp mac.py /bin/mac
         
# Change MAC

1. To set MAC Address randomly, simply rum mac

          mac -w
          mac -e
          mac                       #To change all MAC addresses
         
2. To set specified MAC address, run

          mac -w -m 00:00:00:00:00:00           # your specific MAC address
          mac -e -m 00:00:00:00:00:00
          
          # -w is for wifi and -e is for ethernet
