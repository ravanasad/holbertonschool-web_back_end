#!/bin/usr/env python3
""" 12. Log stats """
from pymongo import MongoClient


if __name__ == "__main__":
    collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx

    n_logs = collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')
