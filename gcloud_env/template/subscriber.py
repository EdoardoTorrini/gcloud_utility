import os, json

from google.cloud import pubsub_v1


class GSub(pubsub_v1.SubscriberClient):

    def __init__(self, sub_name: str, project_id: str):
        super().__init__()
        self.sub = self.subscription_path(project_id, sub_name)
    

    def subscribe(self, callback):
        return super().subscribe(self.sub, callback=callback)


def callback(msg) -> None:
    msg.ack()
    payload = json.loads(msg.data.decode())
    print(f"{payload = }")


def main():
    SUB_NAME, PROJECT_ID = "changeme", "project_id_value"

    sub = GSub(SUB_NAME, PROJECT_ID)
    pull = sub.subscribe(callback)

    try: pull.result(timeout=30)
    except KeyboardInterrupt: print(f"closing subscriber")
    except Exception as e: print(f"err: {str(e)}")
    pull.cancel()

if __name__ == "__main__":
    main()