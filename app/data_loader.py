import json
import os

def load_shipments():
    """
    Loads shipment data using absolute path (safe for all OS)
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "shipments.json")

    with open(data_path, "r") as file:
        data = json.load(file)

    return data
