import json
from collections import UserDict

folder = "logs"


class Logger(UserDict):
    """ Custom class to manage logging. """

    def unless_empty(self, key: str, value: 'MultipleCardsHolder'):
        """ Adds a value to the log if it's not empty. """
        if len(value) == 0:
            return
        self.data[key] = value.log_all()

    def format_logs(self) -> dict:
        """ Returns the inner data of this log. """
        # Unless it's card name, then just return the card name.
        formatted_logs = {}
        for key, value in self.data.items():
            print(key, value)
        pass

    def save_log(self):
        """ Saves the log to a file. """
        # TODO -> dynamically determine the file name.
        filename = f"{folder}/game_00.json"

        with open(filename, "w", encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2, default=dict)
