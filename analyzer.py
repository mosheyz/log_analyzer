from config import sensitive_ports

def check_outside_ip(file):
    outside = [line[1] for line in file if not line[1].startswith("192.168") and not line[1].startswith("10.")]
    return outside

def check_sensitive_port(file):
    sensitive = [line for line in file if line[3] in sensitive_ports]
    return sensitive
