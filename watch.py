from bitcoinrpc.authproxy import AuthServiceProxy

import requests
import settings
import time


tx_fee = 0.0001

twilio_root = "https://api.twilio.com/2010-04-01"
twilio_sms = "{root}/Accounts/{sid}/Messages.json".format(root=twilio_root, sid=settings.twilio_sid)

def send_sms(data):
    for to_number in settings.alert_numbers:
        r = requests.post(twilio_sms, data={
            "From": settings.twilio_from,
            "To": to_number,
            "Body": data
        }, auth=(settings.twilio_sid, settings.twilio_auth))
        time.sleep(5)

def main():
    access = AuthServiceProxy(settings.rpc_connect)
    access.settxfee(tx_fee)

    unspent = access.listunspent(0)
    balance = float(sum(map(lambda u: u["amount"], unspent)))
    if balance != 0.0:
        to_send = balance - tx_fee
        if to_send > 0.000005:
            try:
                access.sendtoaddress(settings.forward_to, to_send)
            except:
                pass
            else:
                send_sms("Forwarded {0:.8f} coins.".format(to_send))

if __name__ == '__main__':
  main()
  