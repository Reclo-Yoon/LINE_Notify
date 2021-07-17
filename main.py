from lineNotify import LineNotify


def main():
    lineNotifyToken = 'input token'
    lineNotify = LineNotify(lineNotifyToken=lineNotifyToken)

    notificationMessage = 'input text message'
    lineNotify.setPayload(notificationMessage=notificationMessage)

    lineNotify.sendRequest()


if __name__ == "__main__":
    main()
