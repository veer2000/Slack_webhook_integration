# accept message input from command line and send to our slack alert channel
import os
import requests
import sys
import getopt

from dotenv import load_dotenv

load_dotenv()
# send message to slack
url = os.getenv("SLACK_URL")
print(url)

def send_slack_message(message):
    print("Sending Slack Message Inside send_slack_message function")
    payload = '{"text" : "%s"}' % message
    print(payload)
    response = requests.post(url = url, data = payload )
    result = {'response code ' : response.status_code,
              'text is ': response.text,}
    print(result)

def main(argv):
    print('Slack alert message')
    message = ' ' # is a default empty

    try:
        opts, args = getopt.getopt(sys.argv,"hm:", ["message="])
        print(f'opts: {opts} and args: {args}')
        print(args[2])
    except getopt.GetoptError:
        print(' at try Slack_alert_message.py -m <message>')
        sys.exit(2)

    print(f'message is {message} and its lenght is {len(message)}')

    if len(opts) == 0:
        message = args[2]

    for opt, arg in opts:
        if opt == '-h':
            print('at for Slack_alert_message.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = args[2]
    print(f'message is {message} and its lenght is {len(message)}')
    send_slack_message(message)

if __name__ == '__main__' :
    main(sys.argv[1:])