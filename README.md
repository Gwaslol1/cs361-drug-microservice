# CS361-drug-microservice

# Note: make sure to have imported ZeroMQ and a JSON parsing library
```python
import zmq
import json
```

# Request (shown in Python)

### To make a request to the service, connect to the socket on the standard port
```python
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```
### Then, send the name of the drug over the socket as a string
```python
socket.send_string(f"{DRUG_NAME}")
```

# Receive (shown in Python)

### To receive a request from the service, use the provided recv() function
```python
DRUG_INFORMATION = socket.recv()
```
This will be a JSON string, but it will still be encoded by ZeroMQ, and so must be decoded to actually be useful. This is done through the provided decode function.
Use your language's built in JSON parsing library to turn the response into a useable JSON object.
```python
DRUG_INFORMATION_DICTIONARY = json.loads(DRUG_INFORMATION.decode())
```

# UML Sequence Diagram
![image](https://user-images.githubusercontent.com/107678957/236915439-6c47d585-d79c-4906-b00f-43f91f68e334.png)
