# CYB333 Midterm Project

## Project Overview

This project was created for the CYB 333 Security Automation midterm assignment. The goal of this project was to demonstrate basic Python networking concepts, including client-server communication and port scanning. The project includes three Python programs that work together to show how network connections can be established and how open ports can be identified on a target system.

## Files Included

### server.py
This file creates a TCP server that listens for incoming connections on a specified port. Once a client connects, the server sends a response message and closes the connection.

### client.py
This file acts as a client that connects to the server. The client receives and displays the message sent by the server.

### port_scanner.py
This file scans a target host for open ports within a specified range. The scanner attempts to connect to each port and reports which ports are open.

## Requirements

- Python 3.x
- Visual Studio Code (optional)
- Git and GitHub

## How to Run the Programs

### Run the Server

```bash
python server.py
```

### Run the Client

```bash
python client.py
```

### Run the Port Scanner

```bash
python port_scanner.py
```

## Learning Objectives

This project demonstrates:

- Python socket programming
- Client-server communication
- Basic network reconnaissance
- Port scanning techniques
- Security automation concepts
- GitHub repository management

## Author

Nicole Soucy

CYB 333 – Security Automation

National University
