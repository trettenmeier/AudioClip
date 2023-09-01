import os
import tkinter as tk
from pygame import mixer


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Clip")

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        music_directory = "./music/point"
        self.music_files_point = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if
                                  file.endswith(".mp3")]
        music_directory = "./music/misc"
        self.music_files_misc = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if
                                 file.endswith(".mp3")]
        music_directory = "./music/set"
        self.music_files_set = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if
                                file.endswith(".mp3")]
        music_directory = "./music/timeout"
        self.music_files_timeout = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if
                                    file.endswith(".mp3")]

        # point stuff
        frame_point = tk.Frame(self.root, borderwidth=2, relief="solid")
        frame_point.pack(padx=10, pady=10, fill="x")
        label = tk.Label(frame_point, text="Point Clips")
        label.pack(padx=2, pady=2, fill="x")

        for music_file in self.music_files_point:
            file_text = App.beautify_file_name(music_file)
            button = tk.Button(frame_point, text=file_text, command=lambda file=music_file: self.play_selected_music(file))
            button.pack(fill="x")

        # timeout stuff
        frame_timeout = tk.Frame(self.root, borderwidth=2, relief="solid")
        frame_timeout.pack(padx=10, pady=10, fill="x")
        label = tk.Label(frame_timeout, text="Timeout Clips")
        label.pack(padx=2, pady=2, fill="x")

        for music_file in self.music_files_timeout:
            file_text = App.beautify_file_name(music_file)
            button = tk.Button(frame_timeout, text=file_text, command=lambda file=music_file: self.play_selected_music(file))
            button.pack(fill="x")

        # set stuff
        frame_set = tk.Frame(self.root, borderwidth=2, relief="solid")
        frame_set.pack(padx=10, pady=10, fill="x")
        label = tk.Label(frame_set, text="Set Clips")
        label.pack(padx=2, pady=2, fill="x")

        for music_file in self.music_files_set:
            file_text = App.beautify_file_name(music_file)
            button = tk.Button(frame_set, text=file_text, command=lambda file=music_file: self.play_selected_music(file))
            button.pack(fill="x")

        # misc stuff
        frame_misc = tk.Frame(self.root, borderwidth=2, relief="solid")
        frame_misc.pack(padx=10, pady=10, fill="x")
        label = tk.Label(frame_misc, text="Misc Clips")
        label.pack(padx=2, pady=2, fill="x")

        for music_file in self.music_files_misc:
            file_text = App.beautify_file_name(music_file)
            button = tk.Button(frame_misc, text=file_text, command=lambda file=music_file: self.play_selected_music(file))
            button.pack(fill="x")

        mixer.init()

    def stop_music(self):
        mixer.music.stop()

    def play_selected_music(self, music_file):
        mixer.music.load(music_file)
        mixer.music.play()

    @staticmethod
    def beautify_file_name(text):
        try:
            return text.replace("/", "#").replace("\\", "#").split("#")[-1].replace(".mp3", "")
        except Exception:
            return text


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
