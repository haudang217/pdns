from pysnmp.hlapi import *
import json
import logging
import time

def get_snmp_data(target, community, oid):
    result = []
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(community),
                              UdpTransportTarget((target, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):
        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                result.append(varBind)
    return result

def main(target, file):
    target = target
    community = 'something_easy_to_remember'
    interfaces_oid = '1.3.6.1.2.1.2.2.1.2'
    ip_addresses_oid = '1.3.6.1.2.1.4.20.1.2'

    interfaces = get_snmp_data(target, community, interfaces_oid)
    ip_addresses = get_snmp_data(target, community, ip_addresses_oid)

    interface_dict = {}
    for iface in interfaces:
        index = str(iface[0][-1])
        name = str(iface[1])
        interface_dict[index] = {'name': name, 'ip': ''}

    for ip in ip_addresses:
        index = str(ip[1])
        ip_address = str(ip[0][len(ip[0]) - 4:])
        if index in interface_dict:
            interface_dict[index]['ip'] = ip_address

    #final_dict = {value['name']: value['ip'] for key, value in interface_dict.items()}
    final_dict = {value['name']: value['ip'] for key, value in interface_dict.items() if value['ip']}

    with open(file, 'w') as f:
        json.dump(final_dict, f, indent=4)

if __name__ == '__main__':
    logging.basicConfig(
        filename='traceoption.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
    )
    listDevice = [
        "10.10.10.11",
        "10.10.10.12",
        "10.10.10.13",
    ]
    listResult = [
        "device10.10.10.11.json",
        "device10.10.10.12.json",
        "device10.10.10.13.json"
    ]
    while(True):
        for i in range(0,3):
            main(listDevice[i], listResult[i])
            logging.info(f'Connected to device {listDevice[i]} to get SNMP information')
        logging.critical('Request infor done, waitting 5min to restart')
        time.sleep(300)