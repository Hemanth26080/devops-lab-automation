#!/bin/bash
echo "🔧 Installing MySQL Database..."

# Auto-skip MySQL interactive setup
export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y mysql-server

# Allow remote connections
sed -i 's/127.0.0.1/0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf
systemctl restart mysql

# Create dev user
mysql -e "CREATE USER 'dev'@'%' IDENTIFIED BY 'devpass';"
mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'dev'@'%';"
mysql -e "FLUSH PRIVILEGES;"

echo "✅ DB Server ready! Port 3306 open to web server"