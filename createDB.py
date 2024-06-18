import mysql.connector
import random
import string

# Function to generate a random IP address
def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# Function to generate a random string of 12 characters
def generate_random_string(length=12):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Function to generate random interface
def generate_random_interface():
    return f"ae{random.randint(1, 1000)}"

# Function to generate random device
def generate_random_device():
    device_number = random.randint(1, 10)
    return f"MX480-{device_number}"

# Function to get IP MGMT based on device
def get_ip_mgmt(device):
    device_number = int(device.split('-')[1])
    return f"10.10.10.{device_number}"

# Function to create and populate the database
def create_database(num_records):
    # Connect to MariaDB
    conn = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                        `key` VARCHAR(15) PRIMARY KEY,
                        `description` VARCHAR(12),
                        `interface` VARCHAR(10),
                        `device` VARCHAR(10),
                        `action_flag` INT,
                        `ip_mgmt` VARCHAR(15))''')
    
    # Populate the database with random records
    for _ in range(num_records):
        key = generate_random_ip()
        description = generate_random_string()
        interface = generate_random_interface()
        device = generate_random_device()
        action_flag = random.randint(0, 3)
        ip_mgmt = get_ip_mgmt(device)
        
        cursor.execute('''INSERT INTO records (key, description, interface, device, action_flag, ip_mgmt)
                          VALUES (%s, %s, %s, %s, %s, %s)''', (key, description, interface, device, action_flag, ip_mgmt))
    
    conn.commit()
    cursor.close()
    conn.close()

# Create the database with 100 records
create_database(100)
