import logging
import socket

# Set up the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set the target IP range
ip_range = "192.168.1.0/24"

# Set the port to scan
port = 4560

# Split the IP range into individual IPs
ips = ip_range.split("/")[0]
start, end = ips.split(".")[-1], ips.split(".")[-1]
start, end = int(start), int(end)

# Scan the network for the log4j vulnerability
for ip in range(start, end+1):
    target = ".".join(ips.split(".")[:-1]) + "." + str(ip)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            logger.info(f"{target}:{port} is vulnerable to log4j vulnerability")
        sock.close()
    except Exception as e:
        logger.error(e)
