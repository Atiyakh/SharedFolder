from socket import *
import threading, os
import zipfile, time

# Change the folder path below
FOLDER = r"path\to\folder"

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_format(startpath=FOLDER):
    data = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        data += '{}{}/'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            data += '{}{}'.format(subindent, f)
    return data

def create_zip(zip_filename, source_dir):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))

former_dir = get_format(FOLDER)

def directory_watcher(dir=FOLDER):
    while True:
        time.sleep(0.5)
        if get_format(FOLDER) != former_dir:
            directory_modified()

def directory_modified():
    global former_dir
    print("New Modification Detected!")
    delete_file("shared_folder_s.zip")
    create_zip("shared_folder_s.zip", FOLDER)
    file = open("shared_folder_s.zip", 'rb')
    data = file.read(); file.close()
    server.send_file(data)
    former_dir = get_format(FOLDER)

class FTP_Server:
    def send_file(self, data):
        for conn in self.connections:
            print(conn)
            try:
                conn.send(len(data).__str__().encode('utf-8'))
                conn.recv(1); conn.sendall(data)
            except:pass
    def accepting_connections(self):
        while True:
            self.ftp_socket.listen()
            conn, addr = self.ftp_socket.accept()
            print(conn)
            self.connections.append(conn)
            print(f"New Connection {addr}")
    def __init__(self):
        self.connections = []
        self.ftp_socket = socket(AF_INET, SOCK_STREAM)
        self.ftp_socket.bind((gethostbyname(gethostname()), 8888))
        self.accepting_connections()

if __name__ == '__main__':
    threading.Thread(target=directory_watcher, args=()).start()
    server = FTP_Server()
