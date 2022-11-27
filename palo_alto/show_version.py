from netmiko import ConnectHandler

paloalto = {
    'device_type': 'paloalto_panos',
    'host': '127.0.0.1',
    'username': 'admin',
    'password': 'yourP@ss'
}

net_connect = ConnectHandler(**paloalto)
output = net_connect.send_command(command_string="show system info",expect_string=r">")
print(output)
net_connect.disconnect()