import socket
import concurrent.futures

# Define the subnet to scan and the output file
subnet = '172.16.11.'
well_known_ports = range(1, 1024)  # Well-known ports
output_file = 'open_ports.txt'  # File where results will be saved

def scan_ip_port(ip, port):
    """
    Attempts to connect to the specified IP and port.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Timeout for the socket connection
        try:
            s.connect((ip, port))
            return ip, port, True
        except (socket.timeout, ConnectionRefusedError):
            return ip, port, False

def scan_subnet(subnet, output_file):
    """
    Scans all IPs in the subnet for well-known ports and writes results to a file.
    """
    with open(output_file, 'w') as file:
        file.write("Open ports:\n")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=255) as executor:
        future_to_ip_port = {executor.submit(scan_ip_port, f'{subnet}{ip}', port): (f'{subnet}{ip}', port) 
                             for ip in range(1, 255) for port in well_known_ports}
        for future in concurrent.futures.as_completed(future_to_ip_port):
            ip, port = future_to_ip_port[future]
            try:
                _, _, is_open = future.result()
                if is_open:
                    result = f"{ip}:{port}\n"
                    print(f"Open: {result.strip()}")
                    with open(output_file, 'a') as file:
                        file.write(result)
            except Exception as exc:
                print(f'{ip}:{port} generated an exception: {exc}')

# Start the subnet scan
if __name__ == '__main__':
    scan_subnet(subnet, output_file)
    print(f"Scan completed. Check {output_file} for a list of open ports.")

