from app.models.data_model import DataModel
from app.views.main_view import MainView

class MainController:
    def __init__(self, master):
        self.master = master
        self.file_data = {}

        self.data_model = DataModel()
        self.view = MainView(self.master, self)
        self.view.pack()
        # self.update_view()

    def show_message(self, message):
        # メッセージを表示する処理
        print('aiueo')
        pass

    def add_file_data(self, filename, contents):
        self.file_data[filename] = contents

    # def update_view(self):
    #     self.view.update(self.data_model.get_data())
