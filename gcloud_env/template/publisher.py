import json, os
from datetime import datetime

from google.cloud import pubsub_v1


class GPub(pubsub_v1.PublisherClient):

    def __init__(self, topic: str, project_id: str):
        super().__init__()
        self.topic = self.topic_path(project_id, topic)

    def publish(self, msg: dict):
        return super().publish(self.topic, json.dumps(msg).encode())


def main():

    TOPIC, PROJECT_ID = "changeme", "project_id_value"
    data = {}

    publisher = GPub(TOPIC, PROJECT_ID)
    res = publisher.publish(data)
    print(data, res.result())

if __name__ == "__main__":
    main()