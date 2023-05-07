# cs361-drug-microservice

# NOTE: MAKE SURE TO HAVE IMPORTED/INCLUDED ZEROMQ
```python
import zmq
```

# REQUEST (shown in Python)

### To make a request to the service, first connect to the socket on the standard port
```python
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```
### Then, send the name of the drug over the socket as a string
```python
socket.send_string(f"{DRUG_NAME}")
```

# RECIEVE (shown in Python)
