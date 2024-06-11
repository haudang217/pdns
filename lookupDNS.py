import dns.resolver
import time
from datetime import datetime

# Danh sách các domain cần lookup
domains = [
    'lo0.0-ttepz_2.1_2bw21.3_mx960_dgw_01-10.114.0.60.noc',
    'fxp0.0-ttepz_2.2_2bw51.3_mx960_dgw_02-10.114.0.63.noc',
    'ae1.0-ttepz_2.2_2bw51.20_mx240_igw_02-10.114.2.193.noc',
    'mx960-2.epz.noc',
    'pc1.noc',
    'test.noc'
]

def lookup_dns(domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['49.213.77.200']
    resolver.port = 5300

    try:
        answer = resolver.resolve(domain, 'A')
        return [str(rdata) for rdata in answer]
    except Exception as e:
        return [str(e)]

def write_to_file(domain, result):
    with open('result.txt', 'a') as f:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        f.write(f"{timestamp} - {domain}: {result}\n")

def main():
    while True:
        for domain in domains:
            result = lookup_dns(domain)
            write_to_file(domain, result)
        time.sleep(300)  # 5 phút

if __name__ == "__main__":
    main()
