import requests
import json


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization' : '7YPfN8RSJDmw0Hq6t4gGk29O1pviUxdzlAuhXVyMFKEC5cbroTVnOrp4HLIcwoF92MB5CNRY6bljJ0sd',
        'sender_id'     : 'FSTSMS',
        'message'       :  message,
        'language'      :  'english',
        'route'         :  'p',
        'numbers'       : number,
        
    }
    responce = requests.get(url, params=params)
    dic = responce.json()
    print(dic)

send_sms("8750303257", " This is message from scific web")


