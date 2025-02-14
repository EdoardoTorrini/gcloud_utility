#!/usr/bin/python3
import requests, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="set the host: https://hostname:port/", required=True)
parser.add_argument("-api", "--api-path", help="set the path of the API: path/to/api/", required=True)
parser.add_argument("-q", "--query-parameter", help="add the query parameter for the request", required=True)
args = parser.parse_args()

url = f"{args.url}{args.api_path}{args.query_parameter}"

ret = requests.delete(url)

if 100 < ret.status_code < 300:
    print(f"{ret.json() = }")
    exit(0)

print(f"[ status code ]: {ret.status_code}")
print(f"[ msg ]: {ret.text}")