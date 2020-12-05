# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 
import subprocess
import random 

#function to run
def FindPi(interval):  
    circle_points= 0
    square_points= 0
    

    for i in range(interval): 
        rand_x= random.uniform(-1, 1) 
        rand_y= random.uniform(-1, 1) 
    
        origin_dist= rand_x**2 + rand_y**2
    
        if origin_dist<= 1: 
            circle_points+= 1 
        square_points+= 1

    pi = 4* circle_points/ square_points 
    return(str(pi))    


# thread function 
def threaded(c,addr): 
    while True: 
  
        # comand received from client 
        data = c.recv(1024) 
        if not data: 
            print('Connection to:',addr[0],"closed")  
            break
        
        out = FindPi(int(str(data.decode('utf-8'))))
        print('Result of:',addr[0],":",addr[1]," is ",out)

        # send back reversed string to client 
        c.send(bytes(out,'utf-8')) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,addr)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 