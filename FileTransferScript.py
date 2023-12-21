import paramiko
from io import StringIO

def transfer_file():
    source_file = input("Enter the source file path: ")
    destination_host = input("Enter the destination host: ")
    destination_path = input("Enter the destination path: ")
    destination_file = input("Enter the destination file name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    key_filename = input("Enter the path to your private key file (or press Enter if not using key-based authentication): ")

    choice = input("Do you want to copy the entire file? (y/n): ")

    if choice.lower() == 'y':
        with open(source_file, 'r') as file:
            content = file.read()
    else:
        lines_to_copy = int(input("Enter the number of lines to copy: "))
      
        with open(source_file, 'r') as file:
            content = ''.join(file.readline() for _ in range(lines_to_copy))

    # Create a StringIO object to simulate a file object
    file_object = StringIO(content)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if password:
        ssh.connect(destination_host, username=username, password=password)
    elif key_filename:
        ssh.connect(destination_host, username=username, key_filename=key_filename)
    else:
        raise ValueError("Either password or key_filename must be provided.")

    sftp = ssh.open_sftp()

    sftp.chdir(destination_path)

    with sftp.file(destination_file, 'w') as remote_file:
        remote_file.write(file_object.read())

    sftp.close()
    ssh.close()

transfer_file()
