#!/usr/bin/env python3
import subprocess
import os

def run(cmd):
    """Run shell command and fail on error"""
    print(f"[+] Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[-] Error: {result.stderr}")
        exit(1)
    return result.stdout

def copy_file(src, dest):
    """Copy file from shared folder to Apache directory"""
    if os.path.exists(src):
        run(f"cp {src} {dest}")
        run(f"chown www-data:www-data {dest}")
        print(f"✅ Copied {src} → {dest}")
    else:
        print(f"[-] Source file not found: {src}")
        exit(1)

print("🚀 Starting Web Server Provisioning with Python...")

# Update & Install Apache
run("apt-get update")
run("apt-get install -y apache2")

# Enable and start Apache
run("systemctl enable apache2")
run("systemctl start apache2")

# Define paths
web_dir = "/var/www/html"

# Copy your custom files
copy_file("/vagrant/web-content/index.html", f"{web_dir}/index.html")
copy_file("/vagrant/web-content/style.css", f"{web_dir}/style.css")
copy_file("/vagrant/web-content/script.js", f"{web_dir}/script.js")

# Ensure ownership
run(f"chown -R www-data:www-data {web_dir}")

print("✅ Web server fully provisioned with custom content!")