# SharedFolder

SharedFolder is a simple FTP-like Folder Synchronization Server that allows you to synchronize folders between a server and a client. It's a lightweight solution for sharing files and data between computers on a network.

## How to Set Up

Follow these steps to set up and use SharedFolder:

### 1. Specify IP Addresses

In order to establish a connection between the server and the client, you need to specify the IP addresses of both machines. Make sure they are on the same network.

### 2. Choose Synchronized Folders

Decide which folders you want to synchronize between the server and the client. You'll need to specify the paths to these folders for both the server and the client.

### 3. Start the Server

On the machine you intend to use as the server, run the server code. This will make the server ready to accept incoming connections from clients.

### 4. Run the Client

On the machine you intend to use as the client, run the client code. Ensure that you specify the server's IP address and the synchronized folder paths for the client.

### 5. Synchronize Folders

Once the server and client are both running, SharedFolder will automatically synchronize the specified folders between them. Any changes made in the server's folder will be mirrored in the clients' folders as long as the both of them are running.

## Contributing

If you'd like to contribute to this project, feel free to open issues or submit pull requests. We welcome any improvements or bug fixes!

## License

This project is licensed under the MIT License - see the[MIT License](LICENSE) file for details.

