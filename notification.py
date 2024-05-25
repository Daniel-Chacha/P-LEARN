import time
from plyer import notification

if __name__ == "_main_":
    while True:
        notification.notify(
            title='ALERT',
            message='Keep going, You are not yet there!',
            timeout=18
        )
        time.sleep(30)
