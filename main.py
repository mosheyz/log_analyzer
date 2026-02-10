from reader import load_csv
from analyzer import check_outside_ip, check_sensitive_port, check_large_file

load_csv("network_traffic.log")
check_outside_ip(load_csv("network_traffic.log"))
check_sensitive_port(load_csv("network_traffic.log"))
check_large_file(load_csv("network_traffic.log"))
