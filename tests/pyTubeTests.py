import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from PIL import Image, ImageTk
import io
import threading


class YouTubePlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("YouTube Player")
        self.master.geometry("800x600")

        self.video_url_entry = ttk.Entry(master)
        self.video_url_entry.pack(pady=10, padx=10, fill='x')

        self.stream_button = ttk.Button(
            master, text="Stream Video", command=self.stream_video)
        self.stream_button.pack(pady=5)

        self.video_frame = tk.Frame(master)
        self.video_frame.pack(pady=10, padx=10)

    def stream_video(self):
        video_url = self.video_url_entry.get()
        yt = YouTube(video_url)
        stream = yt.streams.filter(
            progressive=True, file_extension='mp4').first()

        buffer = io.BytesIO()
        stream.stream_to_buffer(buffer)

        self.video_stream = buffer
        self.play_video()

    def play_video(self):
        self.player = tk.Label(self.video_frame)
        self.player.pack()

        self.video_stream.seek(0)


def main():
    root = tk.Tk()
    youtube_player = YouTubePlayer(root)
    root.mainloop()
    youtube_player.play_video()


if __name__ == "__main__":
    main()
