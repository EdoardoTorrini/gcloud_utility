#!/usr/bin/python3
import requests, argparse, json, os

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="set the host: https://hostname:port/", required=True)
parser.add_argument("-api", "--api-path", help="set the path of the API: path/to/api/", required=True)
# parser.add_argument("-q", "--query-parameter", help="add the query parameter for the request", default=None)
parser.add_argument("-f", "--file", help="json file with the payload of request", required=True)
args = parser.parse_args()

assert os.path.exists(args.file)
payload = None

with open(args.file, "r+") as f: payload = json.loads(f.read())
assert isinstance(payload, dict)

# test, change or you can pass via parameter
name = payload["nome"][0].lower() + payload["cognome"].lower()
url = f"{args.url}{args.api_path}{name}"

ret = requests.post(url, json=payload)

if 100 < ret.status_code < 300:
    print(f"{ret.json() = }")
    exit(0)

print(f"[ status code ]: {ret.status_code}")
print(f"[ msg ]: {ret.text}")