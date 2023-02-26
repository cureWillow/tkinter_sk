class DataModel:
    def __init__(self):
        self.data = []

    def load_data_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.data.append(line.strip())

    def get_data(self):
        return self.data
