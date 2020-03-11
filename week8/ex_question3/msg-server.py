# Example by Saul Johnson <saul.johnson@tees.ac.uk>
# We wrote this file together in class.
#
# **DO NOT REMOVE THIS HEADER**
#
# Notes:
#   + This file is for demonstration purposes only.
#   + You must use this example to guide your own solution.
#     **DO NOT SUBMIT THIS FILE FOR ASSESSMENT**

# This is the *server* part of the chat application. It must be
# started *first* and *recieves* messages *from* the *client*.

# Remember to import the socket library.
import socket

# You might recognise this as the standard IP address for the "local
# loopback interface", the address your computer can use to connect
# to itself:
HOST_IP = '127.0.0.1'

# There are 65,535 TCP ports numbered from 0 to 65,534. Many of these
# are registered (they have official uses according to the Internet
# Assigned Numbers Authority (IANA).
#
# The first 1024 ports (numbered from 0 to 1023) we should never use
# unless we know exactly what we're doing. These are official ports
# that are so widely used for specific purposes that we shouldn't
# use them for anything else.
#
# See a list of registered (privileged) ports here. Avoid using these
# unless you know what you're doing:
# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
PORT_NUM = 50003

# Recognise this? A resource block (with block) that will automatically
# close and tidy up the socket when we're finished with it.
# Let's break a few things down:
#   + socket.AF_INET specifies that we're using IPv4 addresses
#   + socket.SOCK_STREAM specified that we're streaming over this
#     socket, it'll be just like writing to a file.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Bind the socket on the current machine, at the port number above,
    # and start listening for connections.
    sock.bind((HOST_IP, PORT_NUM))
    sock.listen()
    # This will pause the program until a connection is made.
    conn, addr = sock.accept() # Accept the connection!
    # Now, we must enclose the connection in a with block too to close
    # it when we're done.
    with conn:
        print('Someone connected!', addr) # Show that a connection is made.
        while True: # Loop forever...
            data = conn.recv(1024) # Recieve 1024 bytes of data.
            if not data: # If no data is recieved, break out of loop.
                break
            # Print data recieved.
            print('Received message:', data.decode())
