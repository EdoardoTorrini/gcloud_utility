#!/usr/bin/python3
import requests, argparse, json

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="set the host: https://hostname:port/", required=True)
parser.add_argument("-api", "--api-path", help="set the path of the API: path/to/api/", required=True)
parser.add_argument("-q", "--query-parameter", help="add the query parameter for the request", required=True)
parser.add_argument("-d", "--dict-modify", help="json file with the payload of request", required=True)
args = parser.parse_args()

try: payload = json.loads(args.dict_modify)
except Exception as e: print(f"[ error ]: {str(e)}"); exit(1)

url = f"{args.url}{args.api_path}{args.query_parameter}"

ret = requests.put(url, json=payload)

if 100 < ret.status_code < 300:
    print(f"{ret.json() = }")
    exit(0)

print(f"[ status code ]: {ret.status_code}")
print(f"[ msg ]: {ret.text}")