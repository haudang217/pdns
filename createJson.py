import json
import random
import string

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_random_string(length=12):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_interface():
    return f"ae{random.randint(1, 1000)}"

def generate_random_device():
    device_number = random.randint(1, 1000)
    return f"MX480-{device_number}"

def get_ip_mgmt(device):
    device_number = int(device.split('-')[1])
    return f"10.10.10.{device_number}"

def generate_recordName(interface, device, ip_mgmt):
    return f"{interface}-{device}-{ip_mgmt}.dc.vngcloud.vn"

def create_data(num_records):
    records = []    
    for _ in range(num_records):
        key = generate_random_ip()
        device = generate_random_device()
        interface = generate_random_interface()
        ip_mgmt = get_ip_mgmt(device)
        record = {
            "description": generate_random_string(),
            "interface": interface,
            "device": device,
            "action_flag": random.randint(0, 3),
            "ip_mgmt": ip_mgmt,
            "record_name": generate_recordName(interface,device, ip_mgmt)
        }
        records.append({key: record})
    return records

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

data = create_data(1000)
save_to_json(data, 'db.json')

##Checking
with open("db.json", 'r') as f:
    data1 = json.load(f)
list_appeared = set()
new_data = []
for record in data1:
    key = list(record.keys())[0]
    #print(key)
    record_name = record[key]['record_name']
    if record_name not in list_appeared:
        new_data.append(record)
        list_appeared.add(record_name)
    else:
        print(f"Duplicate data in: {record_name}")
save_to_json(new_data, 'db1.json')