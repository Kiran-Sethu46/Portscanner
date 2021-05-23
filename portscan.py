import sys
import socket
from datetime import datetime 

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
else:
      print("Invalid amount of arguments")
      print("syntax :python3 scanner.py <ip>")
    
 
 print("scanning target "+target)
 print("time started: " +str(datetime.now())) 
 
 try:
      for port in range(50,85):
         s = socket.socket(socket>AF_INET, socket.SOCK_STREAM)
         socket.setdefaulttimeout(1)
         result = s.connect_ex((target,port))
         if result ==0:
                 print("port{} is open".format(port))
          s.close()
          
except KeyboardInterrupt:
          print("\n exiting program.")
          sys.exit()
          
except socket.gaierror:
          print("Hostname could not be resolved ")
          sys.exit()
          
except socket.error:
         print("couldnt connect to server.")
         sys.exit()
 
    