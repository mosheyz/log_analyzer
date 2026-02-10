def check_outside_ip(file):
    outside = [line[1] for line in file if not line[1].startswith("192.168") and not line[1].startswith("10.")]
    return outside