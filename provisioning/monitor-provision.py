#!/usr/bin/env python3
import subprocess
import os

def run(cmd):
    print(f"[+] Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[-] Error: {result.stderr}")
        exit(1)
    return result.stdout

print("🚀 Preparing Monitoring Server...")

# Create user for Prometheus (no login shell)
if not os.path.exists("/home/prometheus"):
    run("useradd -rs /bin/false prometheus")

# Create required directories
run("mkdir -p /etc/prometheus /var/lib/prometheus")

print("✅ Monitoring server ready for Prometheus installation!")