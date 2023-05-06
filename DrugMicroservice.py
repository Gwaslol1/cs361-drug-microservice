import json
import zmq


def process_file(name):  # type:(str) -> dict
    """Processes the drug file and returns the dictionary corresponding to the given drug name."""

    data_dict = {}  # type:dict

    with open("Drug_List.json", "r") as in_file:
        data_dict = json.load(in_file)

    if name in data_dict:
        return {name: data_dict[name]}

    else:
        return {}


def main():
    context = zmq.Context()  # Create and connect to socket in response mode
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  # Binding socket to standard local port

    drug_name_request = ""  # type:str
    drug_to_return = {}  # type:dict

    while True:
        drug_name_request = socket.recv()
        print(f"Request received, '{drug_name_request.decode()}', processing...")

        if drug_name_request.decode() == "Stop":
            socket.close()
            break

        drug_to_return = process_file(drug_name_request.decode())

        if drug_to_return:
            print("Request processed, sending response...")
            socket.send_json(drug_to_return)

        else:
            print("Request processed, an error occurred...")
            socket.send_string(f"Drug name not found in database.")


if __name__ == "__main__":
    main()
