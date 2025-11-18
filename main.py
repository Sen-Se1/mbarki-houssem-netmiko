from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_c8000V',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'secret': 'enablepass'
}

def acces_netmiko():
  net_connect = ConnectHandler(**device)
  net_connect.enable()

  clock = connection.send_command("show clock")
  print("date : " + clock)


  interfaces = net_connect.send_command("show ip interface brief")
  with open("interfaces.txt", "w") as f:
    f.write(interfaces)
  print("interfaces : " + interfaces)

  net_connect.disconnect()

print("Hello, Git!")
dire_bonjour()

def dire_salut():
  print("Salut, Git!")

dire_salut()
