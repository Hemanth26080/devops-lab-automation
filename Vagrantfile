# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Base box
  config.vm.box = "ubuntu/jammy64"

  # Disable auto-update
  config.vm.box_check_update = false

  # Synced folder (optional, already default for /vagrant)
  config.vm.synced_folder "./", "/vagrant", disabled: false

  # 🔧 WEB SERVER
  config.vm.define "web" do |web|
    web.vm.hostname = "web-server"
    web.vm.network "private_network", ip: "192.168.56.10"

    web.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 1
      vb.name = "web-server"
    end

    web.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y python3
      chmod +x /vagrant/provisioning/web-provision.py
      /usr/bin/python3 /vagrant/provisioning/web-provision.py
    SHELL
  end

  # 💾 DB SERVER
  config.vm.define "db" do |db|
    db.vm.hostname = "db-server"
    db.vm.network "private_network", ip: "192.168.56.11"

    db.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 1
      vb.name = "db-server"
    end

    db.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y python3
      chmod +x /vagrant/provisioning/db-provision.py
      /usr/bin/python3 /vagrant/provisioning/db-provision.py
    SHELL
  end

  # 📊 MONITOR SERVER
  config.vm.define "monitor" do |monitor|
    monitor.vm.hostname = "monitor-server"
    monitor.vm.network "private_network", ip: "192.168.56.12"

    monitor.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 1
      vb.name = "monitor-server"
    end

    monitor.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y python3
      chmod +x /vagrant/provisioning/monitor-provision.py
      /usr/bin/python3 /vagrant/provisioning/monitor-provision.py
    SHELL
  end

end