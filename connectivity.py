import questionary
import requests
import json
from terminaltables import AsciiTable


class Connectivity:

    def __init__(self, token=None):
        self.token = token

    def connect(self, connector, adaptor, time, token):
        # connect
        link = "http://192.168.60.224/operation/add_queue"
        data = {"params": {"action": 1, "connector": connector, "adaptor": adaptor,
                           "start_time": "current_timestamp", "user_id": 1, "token": token}}

        r = requests.post(url=link, json=data)
        r = r.json()
        print(r)

    def disconnect(self, connector, adaptor, time, token):
        # disconnect
        link = "http://192.168.60.224/operation/add_queue"
        data = {"params": {"action": 2, "connector": connector, "adaptor": adaptor,
                           "start_time": "current_timestamp", "user_id": 1, "token": token}}

        r = requests.post(url=link, json=data)
        r = r.json()
        print(r)

    def recovery(self, connector, adaptor, time, token):
         # recovery
        link = "http://192.168.60.224/operation/add_queue"
        data = {"params": {"action": 3, "connector": connector, "adaptor": adaptor,
                           "start_time": "current_timestamp", "user_id": 1, "token": token}}

        r = requests.post(url=link, json=data)
        r = r.json()
        print(r)

    def calibrate(self, connector, adaptor, time, token):
         # calibrate
        link = "http://192.168.60.224/operation/add_queue"
        data = {"params": {"action": 4, "connector": connector, "adaptor": adaptor,
                           "start_time": "current_timestamp", "user_id": 1, "token": token}}

        r = requests.post(url=link, json=data)
        r = r.json()
        print(r)

    def queue_manage(self, token):
        # print('Queue Manage')
        q_answer = questionary.select(
            "What do you want to do?",
            choices=[
                'Queue',
                'Re-Order',
                'Back to main menu'
            ]).ask()  # returns value of selection

        if(q_answer == 'Queue'):
            # calibrate
            link = "http://192.168.60.224/operation/get_queue"
            data = {"params": {"token": token}}

            r = requests.post(url=link, json=data)
            r = r.json()
            print(r)

            for x in r:
                table_data = [
                    ['Queue ID', 'Connector', 'Adaptor',
                        'Start_Date', 'Action', 'Status'],
                    [x['id'], x['connector_idx'], x['adapter_idx'],
                        x['start_date'], x['operation_id'], x['status']],
                ]
                # x['connector_location'] x['adapter_location']
                table = AsciiTable(table_data)
                print(table.table)


if __name__ == '__main__':
    cli = Connectivity()
    # cli.queue_manage()
