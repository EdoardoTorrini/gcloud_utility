# GCloudUtily
It was deploy to work is a smart way with the suite of google cloud platform, for now it was implent the template for the api, firestore and pub/sub

## Usage
It is possible to work both in your physical machine or in the docker create with all the tools need for the correct usage, if you want to use the docker it needs a docker-compose file, examples:

```yaml
services: 
  pc:
    build:
      context: .
      args:
        USER: et
    ports:
      - 2225:22
      - 4242:4242
    volumes:
      - "/home/user/path/to/gcloud_docker/environment"
```