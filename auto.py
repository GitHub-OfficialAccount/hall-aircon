import atexit, time, requests, json, datetime

# remove everything about atexit if you don't want to turn off the AC when the script is closed
# change time.sleep to your desired interval if you want to
# change min_temperature and max_temperature based on your needs

token = "<your token>"

def check_status():
    print('Checking status')

    url = "https://apintu-prod.daikinpayu.com/me"
    headers = {
        "user-agent": "Dart/3.0 (dart:io)",
        "accept-encoding": "gzip",
        "authorization": f"Bearer {token}",
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200: print('Success')

    print()

    current_temperature = data['data']['aircon']['current_temperature']
    print('Current temperature:', current_temperature)

    balance = data['data']['balance']
    print('Balance:', balance)

    power = data['data']['aircon']['power']

    return current_temperature, power

def control(power):
    if power == 1: print('Turning on')
    else: print('Turning off')

    url = 'https://apintu-prod.daikinpayu.com/v2/ac/control'
    headers = {
        'User-Agent': 'Dart/3.0 (dart:io)',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'power': f'{power}'
    }
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200: print('Success')

    return

def exit_handler():
    print('Application closing')
    control(0)

atexit.register(exit_handler)

min_temperature = 25
max_temperature = 25

while True:

    print(datetime.datetime.now())

    try:

        current_temperature, power = check_status()

        print()

        if power == 1: print('AC is on')
        else: print('AC is off')

        print()

        if current_temperature > max_temperature and power == 0: control(1)
        elif current_temperature < min_temperature and power == 1: control(0)
        else: print('No control needed')

    except Exception as e:
        print('Error encountered:', e)
        print('Error ignored')

    print()

    time.sleep(60)
