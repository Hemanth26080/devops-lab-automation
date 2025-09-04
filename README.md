# 🚀 Project 1: DevOps Lab Automation with Vagrant & Python

## *"Automated 3-Tier Infrastructure Using Python Instead of Bash"*

I built a **fully automated DevOps lab** using **Vagrant**, **VirtualBox**, and **Python** for provisioning — replacing traditional Bash scripts with clean, readable, and maintainable Python code.

This simulates a real-world **3-tier architecture**:
- 🌐 **Web Server**: Apache (provisioned via Python)
- 💾 **Database Server**: MySQL (configured by Python)
- 📊 **Monitoring Server**: Ready for Prometheus (prepared using Python)

All servers are automatically set up when you run `vagrant up`. No manual steps needed!

---

## 🏗️ Architecture Overview

profile
Qwen3-235B-A22B-2507
9:26 pm
Here is the complete README.md content in plain text format. You can copy and paste it directly into a file named README.md:



1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
# 🚀 Project 1: DevOps Lab Automation with Vagrant & Python

## *"Automated 3-Tier Infrastructure Using Python Instead of Bash"*

I built a **fully automated DevOps lab** using **Vagrant**, **VirtualBox**, and **Python** for provisioning — replacing traditional Bash scripts with clean, readable, and maintainable Python code.

This simulates a real-world **3-tier architecture**:
- 🌐 **Web Server**: Apache (provisioned via Python)
- 💾 **Database Server**: MySQL (configured by Python)
- 📊 **Monitoring Server**: Ready for Prometheus (prepared using Python)

All servers are automatically set up when you run `vagrant up`. No manual steps needed!

---

## 🏗️ Architecture Overview

+------------------+ +------------------+ +---------------------+
| Web Server | | DB Server | | Monitor Server |
| 192.168.56.10 |<----->| 192.168.56.11 | | 192.168.56.12 |
| Apache + HTML | | MySQL | | Ready for Prometheus |
+------------------+ +------------------+ +---------------------+

↑
|
Access from Host
http://192.168.56.10


All VMs run on a private network for secure communication.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|--------|
| **Vagrant** | Defines and manages VMs (Ruby DSL) |
| **VirtualBox** | Runs the virtual machines |
| **Ubuntu 22.04 LTS** | Guest OS for all servers |
| **Python 3** | Replaces Bash scripts for provisioning logic |
| **Git & GitHub** | Version control for infrastructure code |

---

## 📂 Project Structure

devops-lab-automation/
├── Vagrantfile
├── provisioning/
│ ├── web-provision.py # Installs Apache via Python
│ ├── db-provision.py # Configures MySQL via Python
│ └── monitor-provision.py # Prepares monitoring env
├── web-content/
│ ├── index.html # Custom HTML page
│ ├── style.css # Custom styling
│ └── script.js # Interactive JavaScript
└── README.md


---

## ▶️ How to Run This Project

### Prerequisites
- [VirtualBox](https://www.virtualbox.org/) installed
- [Vagrant](https://www.vagrantup.com/) installed

### Steps
```bash
# Clone the repo
git clone https://github.com/your-username/devops-lab-automation.git
cd devops-lab-automation

# Launch all VMs and auto-provision with Python
vagrant up

# After completion, access the web server:
# Open your browser and go to:
# http://192.168.56.10
