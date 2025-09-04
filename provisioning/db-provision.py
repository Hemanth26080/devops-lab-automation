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

print("🚀 Starting Database Server Provisioning...")

# Prevent interactive prompts
run('export DEBIAN_FRONTEND=noninteractive')

# Install MySQL
run('apt-get update')
run('apt-get install -y mysql-server')

# Allow remote connections
config_file = '/etc/mysql/mysql.conf.d/mysqld.cnf'
if os.path.exists(config_file):
    run(f'sed -i "s/bind-address.*/bind-address = 0.0.0.0/" {config_file}')
    run(f'sed -i "s/#port/port/" {config_file}')

# Restart MySQL
run('systemctl restart mysql')
run('systemctl enable mysql')

# Secure setup via SQL commands
commands = [
    "CREATE USER 'dev'@'%' IDENTIFIED BY 'devpass';",
    "GRANT ALL PRIVILEGES ON *.* TO 'dev'@'%';",
    "FLUSH PRIVILEGES;"
]

for cmd in commands:
    run(f"mysql -e \"{cmd}\"")

print("✅ Database server setup complete!")