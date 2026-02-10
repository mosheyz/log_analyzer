from reader import load_csv
from analyzer import check_outside_ip, check_sensitive_port, check_large_file, tag_traffic_size
log = load_csv("network_traffic.log")

check_outside_ip(log)
check_sensitive_port(log)
check_large_file(log)
tag_traffic_size(log)
