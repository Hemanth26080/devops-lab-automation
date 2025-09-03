#!/bin/bash
echo "🔧 Setting up Monitoring Server..."

apt-get update

# Install basics
apt-get install -y curl wget vim

# Add Prometheus user
useradd -rs /bin/false prometheus

# Make directories
mkdir /etc/prometheus /var/lib/prometheus

echo "✅ Monitoring server ready for Prometheus/Grafana (Week 2)"