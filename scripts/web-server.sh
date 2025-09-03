#!/bin/bash
echo "🔧 Installing Apache Web Server..."

apt-get update
apt-get install -y apache2

# Enable Apache
systemctl enable apache2
systemctl start apache2

# Create test page
cat > /var/www/html/index.html << EOF
<html>
<h1>🌐 Web Server (192.168.56.10)</h1>
<p>This server is managed by Vagrant + DevOps!</p>
</html>
EOF

echo "✅ Web server ready! Visit http://192.168.56.10"