import paramiko

#note
#install paramiko before execution
#open terminal
# pip install paramiko 

ip = input("Enter IP:")
username = input("Enter username:")
password = input("Enter Password:")

def exec_command(target_cmd):
    stdin, stdout, stderr = client.exec_command(target_cmd) #sends the command to client machine and stores results in variables resp.
    for line in stdout:
        print(line.strip('\n')) #breaks and prints o/p line by line

try:
    target_command = input("Command:")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)
    exec_command(target_command)
except:
    print("An error occured!\nPlease check the inputs and network connection and try again.")

finally:
    client.close()

