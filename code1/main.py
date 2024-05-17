##Ping 
#Ping command is used to check if the source computer can reach a specified computer/website. Ping stands for Packet INternet Groper. Ping command sends an ICMP (Internet Control Message Protocol) request to check the network connectivity. It is an improved version of ifconfig  command.
#Syntax: ping <destination>
#PING geeksforgeeks.org

#Host
#Host command is used for DNS Lookup operations that is it is used to find the IP address associated with a domain and vice versa.  Host command outputs both IPv4 and IPv6 addresses along with mx (mail exchanger) record. (used for redirection of email sent to a domain).
#Syntax: host <domain-address>
#host google.com

#Iwconfig
#Iwconfig is used to view information about connected networks such as SSID, frequency, bit rate, etc. It is like ifconfig but dedicated for wireless networks only.
#Syntax: iwconfig [INTERFACE] [OPTIONS]
#

#Wget
#Wget command is used to download a file from a url using CLI. It saves the content to a file instead of outputing it in console.
#Syntax: wget [fileLink]
#wget google.com/doodles/new-years-day-2024

#Ip monitor
#This command is used state of network devices. It displays the IPv6 address along with 3 possible outputs [PROBE, REACHABLE, STALE]. PROBE – indicates that the network device is being actively tested (test packets are being sent) and response is awaited. REACHABLE – indicates that the network device has been tested (test packets have been sent and response has been received) and it is responsive. STALE – indicates that packets from the device are outdated and status is unavailable based on current data.
#Syntax: ip [options]
#ip monitor

#Speedtest-cli
#This command is used to test the network speed. It outputs the server ip address, upload speed, download speed and latency. Additionally, ip address of sever, server’s location, distance and ISP is also retrieved.
#Syntax: - speedtest-cli
#speedtest-cli

#Hostname
#It retrieves the name of assigned to host on a computer network and can also set the hostname if option –b is specified. It can also write hostname to a file.
#Syntax:  hostname - [option] [file].
#hostname

#Ifplugstatus
#This command is used to check if a network cable is plugged in and is being detected by the system or not. It outputs link beat detected if the cable is detected or simply unplugged if it is not detected.
#Syntax: ifplugstatus
#ifplugstatus


#Tracepath
#This command is used to detect network delays (latencies) . It traces the route to the destinations and identifies each hop. It also recognizes the point where network is weak.
#Syntax: tracepath  <destination>
#tracepath mindmajix.com


#Curl 
#The curl command is used to transfer information from a server. To write it to a file use the –O option.
#Syntax: curl [options] [file_name] [url]
#curl -o test.html https://www.geeksforgeeks.org






