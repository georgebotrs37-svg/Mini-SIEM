import re

def analyze(line):
    line = line.strip()

    ip_match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
    ip = ip_match[0] if ip_match else "Unknown"

    user_match = re.findall(r'for (\w+)', line)
    user = user_match[0] if user_match else "Unknown"

    if "Failed password" in line:
        return {
            "type": "Brute Force",
            "severity": "HIGH",
            "ip": ip,
            "user": user,
            "raw": line
        }

    if "Accepted password" in line:
        return {
            "type": "Login Success",
            "severity": "LOW",
            "ip": ip,
            "user": user,
            "raw": line
        }

    return None