import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("500x250")
        
        # Variables
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="MP4")
        self.video_title = tk.StringVar(value="Video Title Will Appear Here")
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # URL Entry
        ttk.Label(self.root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        url_entry = ttk.Entry(self.root, textvariable=self.url_var, width=50)
        url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        # Fetch Button
        fetch_btn = ttk.Button(self.root, text="Fetch Video", command=self.fetch_video)
        fetch_btn.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Video Title Display
        title_label = ttk.Label(self.root, textvariable=self.video_title, wraplength=400)
        title_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        # Format Selection
        ttk.Label(self.root, text="Select Format:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        format_menu = ttk.OptionMenu(self.root, self.format_var, "MP4", "MP4", "MP3")
        format_menu.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        # Download Button
        download_btn = ttk.Button(self.root, text="Download", command=self.download_video)
        download_btn.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        
    def fetch_video(self):
        url = self.url_var.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        try:
            self.yt = YouTube(url)
            self.video_title.set(self.yt.title)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch video: {str(e)}")
    
    def download_video(self):
        if not hasattr(self, 'yt'):
            messagebox.showerror("Error", "Please fetch a video first")
            return
            
        download_dir = filedialog.askdirectory()
        if not download_dir:
            return
            
        try:
            if self.format_var.get() == "MP4":
                stream = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                stream.download(output_path=download_dir)
            else:
                stream = self.yt.streams.filter(only_audio=True).first()
                download_file = stream.download(output_path=download_dir)
                base, ext = os.path.splitext(download_file)
                new_file = base + '.mp3'
                os.rename(download_file, new_file)
                
            messagebox.showinfo("Success", "Download completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()

