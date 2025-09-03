# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  # Web Server
  config.vm.define "web" do |web|
    web.vm.hostname = "web-server"
    web.vm.network "private_network", ip: "192.168.56.10"
    web.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 1
    end
    web.vm.provision "shell", path: "scripts/web-server.sh"
  end

  # DB Server
  config.vm.define "db" do |db|
    db.vm.hostname = "db-server"
    db.vm.network "private_network", ip: "192.168.56.11"
    db.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 1
    end
    db.vm.provision "shell", path: "scripts/db-server.sh"
  end

  # Monitoring Server
  config.vm.define "monitor" do |monitor|
    monitor.vm.hostname = "monitor-server"
    monitor.vm.network "private_network", ip: "192.168.56.12"
    monitor.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 1
    end
    monitor.vm.provision "shell", path: "scripts/monitor-server.sh"
  end

  # Synced folder (optional)
  config.vm.synced_folder ".", "/vagrant", disabled: true
end