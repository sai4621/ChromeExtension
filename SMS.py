import sys
import smtplib
from email.message import EmailMessage

carrierMail = {
    'at&t': '@txt.att.net',
    'boost mobile': '@sms.myboostmobile.com',
    'cricket wireless': '@mms.cricketwireless.net',
    'google project fi': '@msg.fi.google.com',
    'republic wireless': '@text.republicwireless.com',
    'sprint': '@messaging.sprintpcs.com',
    'straight talk': '@vtext.com',
    't-mobile': '@tmomail.net',
    'ting': '@message.ting.com',
    'u.s. cellular': '@email.uscc.net',
    'verizon': '@vtext.com',
    'virgin mobile': '@vmobl.com'
}

def send_sms(number, carrier, message):
    """
    Send a URL to the specified number using the specified carrier.
    """
    num = number + carrierMail[carrier.lower()]

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('selfshare074@gmail.com', 'zxejddcojfknacuk')
    server.sendmail('selfshare074@gmail.com', num, message)
    server.quit()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python test.py <number> <carrier> <message>")
        sys.exit(1)
    else:
        send_sms(sys.argv[1], sys.argv[2], sys.argv[3])
        sys.exit(0)