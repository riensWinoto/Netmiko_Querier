from netmiko import ConnectHandler
import sys
paloalto = {
    'device_type': 'paloalto_panos',
    'host': '127.0.0.1',
    'username': 'admin',
    'password': 'yourP@ss'
}

rulename=sys.argv[1]
application=sys.argv[2]
net_connect = ConnectHandler(**paloalto)
net_connect.send_command(command_string="configure\n",expect_string=r"#")
net_connect.send_command(command_string=f"set rulebase security rules {rulename} application {application}",expect_string=r"#")
net_connect.disconnect()