import dns.resolver
import dns.reversename
import dns.query
from datetime import datetime

# Hàm thực hiện reverse DNS lookup
def reverse_dns_lookup(ip_address, dns_server, dns_port):
    try:
        # Tạo đối tượng resolver
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]
        resolver.port = dns_port

        # Chuyển đổi IP sang tên miền ngược
        reverse_name = dns.reversename.from_address(ip_address)

        # Thực hiện truy vấn PTR
        query = dns.message.make_query(reverse_name, dns.rdatatype.PTR)
        response = dns.query.udp(query, dns_server, port=dns_port)
        
        # Trích xuất kết quả từ phản hồi
        for rrset in response.answer:
            for rdata in rrset:
                if rdata.rdtype == dns.rdatatype.PTR:
                    return rdata.to_text()
        return "Không tìm thấy PTR record"
    except Exception as e:
        return f"Không thể thực hiện reverse DNS lookup cho {ip_address}: {e}"

# Địa chỉ IP cần reverse lookup
ip_address = '10.114.0.63'

# Thông tin DNS server
dns_server = '49.213.77.200'
dns_port = 5300

# Thực hiện reverse DNS lookup và in kết quả
hostname = reverse_dns_lookup(ip_address, dns_server, dns_port)
print(f"Hostname cho {ip_address} là: {hostname}")

# Ghi kết quả vào tệp với thời gian ghi
with open('resultReverseDNS.txt', 'a') as file:
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    file.write(f"{timestamp} - Hostname cho {ip_address} là: {hostname}\n")
