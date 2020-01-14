import questionary
from connectivity import Connectivity


class ListOfMenu:

    def __init__(self, token=None):
        self.token = token

    def main_menu(self, token):
        self.token = token

        main_answer = questionary.select(
            "What do you want to do?",
            choices=[
                'Connectivity',
                'Device Setting',
                'User Management',
                'Current Status',
                'Logout'
            ]).ask()  # returns value of selection

        if(main_answer == 'Connectivity'):
            connectivity_answer = self.connectivity_menu()

            if(connectivity_answer == 'Connect'):
                connector = input("Enter Connector: ")
                adaptor = input("Enter Adaptor: ")

                date_time = input(
                    "Enter Date and Time: (format: 2019-Aug-28 10:10:00)\n")

                a = Connectivity()
                a.connect(connector, adaptor, date_time, self.token)

            elif(connectivity_answer == 'Disconnect'):
                connector = input("Enter Connector: ")
                adaptor = input("Enter Adaptor: ")

                date_time = input(
                    "Enter Date and Time: (format: 2019-Aug-28 10:10:00)\n")

                a = Connectivity()
                a.recovery(connector, adaptor, date_time, self.token)

            elif(connectivity_answer == 'Recovery'):
                connector = input("Enter Connector: ")
                adaptor = input("Enter Adaptor: ")

                date_time = input(
                    "Enter Date and Time: (format: 2019-Aug-28 10:10:00)\n")

                a = Connectivity()
                a.disconnect(connector, adaptor, date_time, self.token)

            elif(connectivity_answer == 'Calibrate'):
                connector = input("Enter Connector: ")
                adaptor = input("Enter Adaptor: ")

                date_time = input(
                    "Enter Date and Time: (format: 2019-Aug-28 10:10:00)\n")

                a = Connectivity()
                a.calibrate(connector, adaptor, date_time, self.token)

            elif(connectivity_answer == 'Queue Management'):
                a = Connectivity()
                a.queue_manage(self.token)

        elif(main_answer == 'Device Setting'):
            print('2')
        elif(main_answer == 'User Management'):
            print('3')
        elif(main_answer == 'Current Status'):
            print('4')
        elif(main_answer == 'Logout'):
            print('--Goodbye--')
            return -1
        return 0

    def connectivity_menu(self):
        answer = questionary.select(
            "What do you want to do?",
            choices=[
                'Connect',
                'Disconnect',
                'Recovery',
                'Calibrate',
                'Queue Management',
                'Back to main menu'
            ]).ask()  # returns value of selection
        return answer

    def queue_management_menu(self):
        answer = questionary.select(
            "What do you want to do?",
            choices=[
                'Queue',
                'Re-Order',
                'Back to main menu'
            ]).ask()  # returns value of selection
        return answer


if __name__ == '__main__':
    c = ListOfMenu()
