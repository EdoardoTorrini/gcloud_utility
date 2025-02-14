# GCloudUtily
It was deploy to work is a smart way with the suite of google cloud platform, for now it was implent the template for the api, firestore and pub/sub

# Usage

## Docker installation

It is possible to work both in your physical machine or in the docker create with all the tools need for the correct usage, if you want to use the docker it needs a docker-compose file, examples:

```yaml
services: 
  pc:
    build:
      context: .
      args:
        USER: user
    ports:
      - 2225:22
      - 4242:4242
    volumes:
      - "/home/user/path/to/gcloud_docker/environment"
```

After that you can build and run your docker using:
```bash
$ docker compose up --build -d
$ ssh -p 2225 user@localhost
```

## Enable Virtual Environment

For enabling virtual environment you have to execute:
```bash
$ source setenv PROJECT_ID
```
and substitute the PROJECT_ID with a name's projects of yours (alredy existing or not), after that the `setenv` have alredy create a directory named like your project and an ad hoc python virtual environment. 

In the `gcloud_env` there is a directory `bin` contain useful script that will be perfom some common operation, before that in you **GCloud Dashboard** you have to enable the firestore and create in the **recommended way**, and **enable billing**.
- `deploy PROJECT_ID YAML_PATH`: permit to deploy your own application in the **App Engine**
- `create_topic TOPIC_NAME`: permit to create new topic
- `create_sub SUBSCRIPTION_NAME TOPIC`: create a new subscription_name for a certain topic

In the directory `gcloud_env/bin/api_check` there are 4 python script to check the correctness of the implementation of your API.