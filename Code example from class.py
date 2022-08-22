#!/usr/bin/env python3

#imports the Path class from pathlib
from pathlib import Path

# imports the socket class
import socket

# imports the os class
import os

# defines the Address class
class Address:
    
    # defines the __init__ function 
    def __init__(self, octet1, octet2, octet3, octet4):
        
        # sets the passed through arguements to integer values
        self.firstOctet = int(octet1)
        self.secondOctet = int(octet2)
        self.thirdOctet = int(octet3)
        self.fourthOctet = int(octet4)
    
    # defines the determine class function
    def determineClass(self):
        
        # if statements to determine the ip address type
        if self.firstOctet >= 1 and self.firstOctet <= 126:
            ip_class = "A"
        elif self.firstOctet >= 128 and self.firstOctet <= 191:
            ip_class = "B"
        elif self.firstOctet >= 192 and self.firstOctet <= 223:
            ip_class = "C"
        elif self.firstOctet >= 224 and self.firstOctet <= 239:
            ip_class = "D"
        
        # returns the variable to the calling function
        return ip_class
    
    # defines the convert to binary function
    def convert_b(self):
        
        # converts the addresss to binary
        o1 = bin(self.firstOctet)[2:]
        o2 = bin(self.secondOctet)[2:]
        o3 = bin(self.thirdOctet)[2:]
        o4 = bin(self.fourthOctet)[2:]
        
        # converts data to ip address format
        a_bin = f"{o1}.{o2}.{o3}.{o4}"
        
        # returns the value of the variable to the calling function
        return a_bin
    
    # defines the convert to hexidecimal function
    def convert_h(self):
        
        # converts the address to hexidecimal
        o1 = hex(self.firstOctet)[2:]
        o2 = hex(self.secondOctet)[2:]
        o3 = hex(self.thirdOctet)[2:]
        o4 = hex(self.fourthOctet)[2:]
        
        # converts the data back to ip address format
        a_hex = f"{o1}.{o2}.{o3}.{o4}"
        
        # returns the value of the variable to the calling function
        return a_hex

# defines the grab ip address      
def grab_ip():
    
    # sets the ip variable to the pc's ip address
    ip = socket.gethostbyname(socket.gethostname())
    
    # returns the value of the variable to the calling function
    return ip

# defines the split ip function
def split_ip(ip):
    
    # splits the ip address into the four different octets
    sp1it = ip.split(".")
    
    # returns the value of the variable to the calling function
    return sp1it

# defines the output function
def output(ip, a_split):
    
    # sets info as an Addess class variable and passes the ip address information to that class
    info = Address(*a_split)
    
    # sets the output to variables for use later
    f_line = f"The IPv4 address is: {ip}"
    s_line = f"This address is a class: {info.determineClass()}"
    t_line = f"Your IPv4 address in binary is as follows: {info.convert_b()}"
    fo_line = f"Your IPv4 address in hex is as follows: {info.convert_h()}"
    
    # prints the output
    print(f_line)
    print(s_line)
    print(t_line)
    print(fo_line)
    
    # sets the output as a list variable
    lst = f_line, s_line, t_line, fo_line
    
    # returns the value of the variable back to the calling function
    return lst

# defines the check function
def check():
    
    # sets path as the path for the temp folder
    path = Path("c:/temp")
    
    # if and else statement that creates the folder if it does not exist
    if (path.exists()):
        pass
    else:
        os.mkdir(path)
    
    # sets path1 as the path for the project folder
    path1 = Path("c:/temp/AcreeIP_Project_folder")
    
    # if and else statement that creates the folder if it does not exist
    if (path1.exists()):
        pass
    else:
        os.mkdir(path1)
    
    # returnes the value of the variable back to the calling function
    return path1

# defines the text_file function
def text_file(path1, lst):
    
    # changes the current directory to the one for the file to be created in
    os.chdir(path1)
    
    # sets file to opening the file in write mode
    file = open("AcreeIP_Project_file.txt", "w")
    
    # writes the information into the file, if the file does not exists it creates the file
    file.write(f"{lst [0]}\n{lst [1]}\n{lst [2]}\n{lst [3]}\n")
    
    # returns to the calling function
    return

# defines the main function      
def main():
    
    # sets the 
    # sets the ip variable to the output of the grab ip function
    ip = grab_ip()
    
    # sets the address split variable to the results of passing the ip variable to the split_ip function
    a_split = split_ip(ip)
    
    # sets the list variable to the results of passing the ip, and address split variable to the output function
    lst = output(ip, a_split)
    
    # sets the path1 variable to the results of the check function
    path1 = check()
    
    # calls the text file function by passing the path1 and lst variable to create the folders and files on the computer system
    text_file(path1, lst)
    
# if started as the main module, call the main function
if __name__ == "__main__":
    
    # execute the main function
    main()