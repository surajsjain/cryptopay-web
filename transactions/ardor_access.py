import requests
import json

from django.conf import settings

def get_unsigned_transaction_bytes(receiver_account_id,payment_amount,sender_public_key,chain=1):

    print('Function Called')

    base = settings.ARDOR_REQUEST_BASE_URL
    payment_amount = payment_amount * (10**8)
    # print(base+'nxt?chain=1&requestType=sendMoney&recipient='+receiver_account_id+'&publicKey='+public_key+'&amountNQT='+payment_amount+'&feeNQT=1&deadline=60')
    print('Making a Request')
    data=requests.post(base+'nxt?chain='+str(chain)+'&requestType=sendMoney&recipient='+str(receiver_account_id)+'&publicKey='+str(sender_public_key)+'&amountNQT='+str(payment_amount)+'&feeNQT=-1&deadline=10')
    print('request completed')
    # print(type(data))
    x=data.json()
    # print(type(x))
    # print(x)
    return x['transactionJSON']

def confirm_transaction(unsignedTransactionJSON,secret_pass_phrase):
    base = settings.ARDOR_REQUEST_BASE_URL
    # print(unsignedTransactionJSON)
    unsignedTransactionJSON=json.dumps(unsignedTransactionJSON)
    data=requests.post(base+'nxt?requestType=signTransaction&unsignedTransactionJSON='+unsignedTransactionJSON+'&secretPhrase='+secret_pass_phrase)
    x=data.json()
    # print(x)
    status = x['verify']
    if(status is True):
        transactionJSON=x['transactionJSON']
        transactionJSON=json.dumps(transactionJSON)
        broadcast_data=requests.post(base+'nxt?requestType=broadcastTransaction&transactionJSON='+transactionJSON)
        # print("Success")
    return status
