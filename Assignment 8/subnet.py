ip_subnet_map = {
    "A":[0,127,"255.0.0.0"],
    "B":[128,191,"255.255.0.0"],
    "C":[192,223,"255.255.255.0"],
    "D":[224,239,"255.255.0.0"],
    "E":[240,255,"255.255.0.0"],
}

def is_ip_valid(ip_add:str) -> bool:
    subnets = ip_add.split(".")
    for subnet in subnets:
        if not(0 <= int(subnet) <= 255):
            return False
        
    return True

    
def get_ip_and_subnet_mask(first_octet:int):
    subnet_mask = None
    ip_class = None

    for k,v in ip_subnet_map.items():
        if(v[0] <= first_octet <= v[1]):
            subnet_mask = v[2]
            ip_class = k
            return subnet_mask,ip_class
    
    return None,None


if __name__ == "__main__":
    ip_add = input("Enter IP\n")

    if(is_ip_valid(ip_add)):
        first_octet = int(ip_add[:3])
        subnet_mask,ip_class = get_ip_and_subnet_mask(first_octet)
        print(f"IP Address class is {ip_class} \nSubnet mask is {subnet_mask}")
    else:
        print("Invalid IP address")