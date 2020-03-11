# Example by Saul Johnson <saul.johnson@tees.ac.uk>
# We wrote this file together in class.
#
# **DO NOT REMOVE THIS HEADER**
#
# Notes:
#   + This file is for demonstration purposes only.
#   + You must use this example to guide your own solution.
#     **DO NOT SUBMIT THIS FILE FOR ASSESSMENT**

# This is the *client* portion of the chat application. It must be started
# *last* and *sends* messages *to* the *server*.

# Remember to import the socket library.
import socket

# The address of the local loopback interface (see msg-server.py).
HOST_IP = '127.0.0.1'

# This port number must match that in msg-server.py.
PORT_NUM = 50003

# A resource block that will close our socket when we're done with it.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST_IP, PORT_NUM))
    # Loop forever, sending messages.
    print("Chat started! Type '/exit' to quit...")
    buffer = input("Message: ")
    while buffer.strip().lower() != "/exit": # Type "/exit" to quit.
        sock.sendall(buffer.encode()) # encode() needed here to turn string to bytes!
        buffer = input("Message: ")
