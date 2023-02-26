import tkinter as tk
import tkinterdnd2 as tk2
import os
from tkinter import filedialog

class MainView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.filename = ''

        # ウィンドウの設定
        self.parent = parent
        self.parent.geometry("400x300")

        # フレームを設定
        self.frame = tk.Frame(self, bd=2, relief=tk.SUNKEN)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # ラベルを作成
        label = tk.Label(self.frame, text="ファイルを選択してください")
        label.pack(side="left")

        # # Listboxウィジェットの生成
        # self.listbox = tk.Listbox(self)
        # self.listbox.drop_target_register(tk2.DND_FILES)
        # self.listbox.dnd_bind('<<Drop>>', self.add_listbox)
        # self.listbox.pack(fill=tk.X, side=tk.LEFT)

        # ファイル名を表示するリストボックスを追加
        self.listbox = tk.Listbox(self)
        self.listbox.pack(padx=10, pady=10, fill='both', expand=True)

        # ファイルをドロップして読み込むための設定
        self.listbox.drop_target_register(tk2.DND_FILES)
        self.listbox.dnd_bind('<<Drop>>', self.drop_files)
        # self.bind('<<DragEnter>>', self.drag_enter)
        # self.bind('<<DragLeave>>', self.drag_leave)
        self.drop_target = tk.Label(self, text='Drop files here')
        self.drop_target.pack(padx=10, pady=10, fill='both', expand=True)

        # スクロールバーの生成
        scroll = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.listbox.configure(yscrollcommand=scroll.set)
        scroll.config(command=self.listbox.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # フレームをドロップ可能にする
        # self.frame.drop_target_register(tk2.DND_FILES)
        # self.frame.dnd_bind('<<Drop>>', self.on_drop)

    def on_button_click(self):
        # ボタンがクリックされたときの処理
        self.controller.show_message("Button clicked!")

    def add_listbox(self, event):
        self.listbox.insert("end", event.data)

    def on_select_file(self):
        # ファイル選択ダイアログを開く
        file_path = filedialog.askopenfilename()
        if file_path:
            # ファイルが選択された場合、選択したファイルの名前を表示する
            self.filename = file_path.split("/")[-1]
            self.filename_label.config(text=self.filename)

    def on_drop(self, event):
        # ファイルパスを取得
        self.file_path = event.data[tk2.DND_FILES][0]

        # ファイルを読み込んでテキストボックスに表示
        with open(self.file_path, 'r') as f:
            text = f.read()
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, text)

    def drag_enter(self, event):
        # ドロップ操作が入った時の処理
        self.drop_target.config(bg='gray')

    def drag_leave(self, event):
        # ドロップ操作が出た時の処理
        self.drop_target.config(bg='white')

    def drop_files(self, event):
        # ドロップされたファイルを処理する

        for file in self.listbox.tk.splitlist(event.data):
            # 拡張子を取得
            ext = os.path.splitext(file)[1].lower()

            print('loop',file)

            # CSV以外のファイルはスキップする
            if ext != ".csv":
                continue

            # filename = file.encode('utf-8')
            # print(filename)
            if os.path.isfile(file):
                print('isfile')
                # ファイルの内容を保持する辞書を作成する
                filename = os.path.basename(file)
                with open(file, 'r') as f:
                    contents = f.read()
                self.controller.add_file_data(filename, contents)

                # ファイル名をリストボックスに追加する
                self.listbox.insert('end', filename)
