import os 

ip_list = ["8.8.8.8", "8.8.8.4", "192.168.100.1"]
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4"in response:
        print(f"UP {ip} Ping successful")
    else:
        print(f"DOWN {ip} Ping unsuccessful")