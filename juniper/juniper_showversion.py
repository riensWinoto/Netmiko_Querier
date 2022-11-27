from netmiko import ConnectHandler

juniper = {
    'device_type': 'juniper_junos',
    'host': '127.0.0.1',
    'username': 'admin',
    'password': 'yourP@ss'
}

net_connect = ConnectHandler(**juniper)
output = net_connect.send_command(command_string="show version")
print(output)
net_connect.disconnect()