import time

from plyer import notification

notification_title = "This is Demo..."
notification_message = "Please Drink a water"

time.sleep(5),

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = None,
    timeout = 5,
    toast = False
  )