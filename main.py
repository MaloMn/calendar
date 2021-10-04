from urllib import request
import codecs


class Content:

    def __init__(self, text):
        self.text = text

    def get_json(self):
        return ""


class Data:

    def __init__(self, group):
        self.output = "data.json"
        self.group = group
        url = "https://edt-v2.univ-nantes.fr/calendar/ics?timetables[0]=" + str(group)

        with request.urlopen(url) as response:
            html = response.read()
            self.content = Content(html.decode('UTF-8'))

        self.json = self.content.get_json()

    def update(self):
        # Replace old data by new data & add new data
        pass

    def export(self):
        with open(self.output, 'w') as f:
            f.write(self.json)


if __name__ == "__main__":
    group_id = 48361
    d = Data(group_id)
