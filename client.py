from socket import *
import threading
import zipfile
import traceback

# change the folder path and ip address below
FOLDER = r"path\to\client\folder"
IP = "85.114.112.78" # ip of the server

# you can you some port forwarding technique
# or a domain to access your server globally

def extract_zip(zip_filename, extract_dir):
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extractall(extract_dir)

class FTP_Connection:
    def recv_modifications(self):
        while True:
            try:
                buffer_size = int(self.ftp_socket.recv(1024))
                self.ftp_socket.send(b'0')
                data = b''
                while True:
                    if len(data) < buffer_size:
                        data += self.ftp_socket.recv(20_000)
                    else:break
                file = open("shared_folder_c.zip", 'wb')
                file.write(data); file.close()
                print("New Modifications!")
                extract_zip("shared_folder_c.zip", FOLDER)
            except (ConnectionError, ConnectionAbortedError, error,
            ConnectionRefusedError, ConnectionResetError):
                traceback.print_exc()
                print("Cannot Connect To FTP Server!")
                self.__init__()
    def __init__(self):
        try:
            HOST = (IP, 8888)
            self.ftp_socket = socket(AF_INET, SOCK_STREAM)
            self.ftp_socket.connect(HOST)
            threading.Thread(target=self.recv_modifications, args=()).start()
        except:
            traceback.print_exc()
            print("Cannot Connect To FTP Server!")
            self.__init__()

if __name__ == '__main__':
    serve_connection = FTP_Connection()
