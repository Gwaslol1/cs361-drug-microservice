import zmq

context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

message_to_send = ""  # type:str

while True:
    message_to_send = input("Enter the drug you want")

    socket.send_string(f"{message_to_send}")

    if message_to_send == "Stop":
        socket.close()
        break

    message = socket.recv()
    print(f"Response from server: {message.decode()}")
