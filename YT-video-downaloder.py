import tkinter as tk
from tkinter import messagebox, font
import yt_dlp

def create_gui():
    # Set up the root window
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    root.geometry("500x450")
    root.configure(bg="#f0f0f0")  # Set background color

    # Define custom fonts
    title_font = font.Font(family="Helvetica", size=18, weight="bold")
    label_font = font.Font(family="Helvetica", size=12)
    button_font = font.Font(family="Helvetica", size=10, weight="bold")

    # Add title label
    title_label = tk.Label(root, text="YouTube Video Downloader", font=title_font, fg="#333", bg="#f0f0f0")
    title_label.pack(pady=20)

    # URL input section
    tk.Label(root, text="Enter YouTube Video URL:", font=label_font, fg="#333", bg="#f0f0f0").pack(pady=10)
    url_entry = tk.Entry(root, width=50, font=("Helvetica", 10))
    url_entry.pack(pady=5)

    # Quality selection section
    tk.Label(root, text="Select Quality:", font=label_font, fg="#333", bg="#f0f0f0").pack(pady=10)
    quality_var = tk.StringVar(value="360p")
    qualities = [
        ("1080p (HD)", "1080p"),
        ("720p (MHD)", "720p"),
        ("360p (Low)", "360p"),
        ("MP3 (Audio Only)", "mp3")
    ]
    for text, quality in qualities:
        tk.Radiobutton(root, text=text, variable=quality_var, value=quality, font=("Helvetica", 10),
                       fg="#555", bg="#f0f0f0", selectcolor="#d1d1d1").pack(anchor='w', padx=180)

    # Download button with custom styling
    download_button = tk.Button(root, text="Download", font=button_font, bg="#4CAF50", fg="white",
                                activebackground="#45a049", width=15, height=2,
                                command=lambda: download_video(url_entry.get(), quality_var.get()))
    download_button.pack(pady=30)

    root.mainloop()

def download_video(url, quality):
    # Validate URL input
    if not url.strip():
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    try:
        # Set download options based on selected quality
        if quality == "mp3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:
            ydl_opts = {
                'format': f'best[height={quality[:-1]}]/best',  # Specify resolution or best available
                'outtmpl': '%(title)s.%(ext)s',
            }

        # Download with yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    create_gui()
