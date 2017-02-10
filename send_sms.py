import smtplib


def send_sms(msg, number):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login("directionstogo@gmail.com", "directions1234")
    except SocketError as e:
        print str(e)
    except AuthError as e:
        print str(e)

    carrierList = ["@vmobile.ca",
                   "@txt.bellmobility.ca",
                   "@txt.bell.ca",
                   "@fido.ca",
                   "@pcs.rogers.com",
                   "@msg.telus.com",
                   "@msg.koodomobile.com",
                   "@sms.windmobile.ca",
                   "@text.mtsmobility.com",
                   "@sms.sasktel.com"]

    for carrier in carrierList:
        recipient = number + carrier
        try:
            server.sendmail("directionstogo@gmail.com", recipient, msg)
        except Exception as e:
            print str(e)
    server.quit()


#help_message = """Text this number with a request saying something like: "How can I get from LOCATION A to LOCATION B" and we will help you find your way."""

#send_sms(help_message, "6477817918")