import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

root = tk.Tk()
root.title("MiniTik")
root.geometry("400x700")
root.configure(bg="black")

# Store likes so they update
posts_data = [
    {"user": "@cool_gamer", "caption": "My first FPS game 🔥", "likes": 120},
    {"user": "@coding_king", "caption": "Learning Python!", "likes": 340},
    {"user": "@onitsha_vibes", "caption": "Sunset in Onitsha 🌅", "likes": 890},
]

title = tk.Label(root, text="🔥 MiniTik", fg="white", bg="black", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Upload button
def upload_post():
    user = simpledialog.askstring("Upload", "Enter your username:", parent=root)
    caption = simpledialog.askstring("Upload", "Enter caption:", parent=root)
    if user and caption:
        posts_data.insert(0, {"user": f"@{user}", "caption": caption, "likes": 0})
        refresh_feed()
        messagebox.showinfo("Success", "Post uploaded!")

upload_btn = tk.Button(root, text="+ Upload Post", command=upload_post, bg="red", fg="white", font=("Arial", 12, "bold"))
upload_btn.pack(pady=5)

canvas = tk.Canvas(root, bg="black")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="black")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

def like_post(index):
    posts_data[index]["likes"] += 1
    refresh_feed()

def refresh_feed():
    # Clear old posts
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    
    # Add all posts again
    for i, post in enumerate(posts_data):
        frame = tk.Frame(scrollable_frame, bg="black", pady=10)
        frame.pack(fill="x", padx=10)
        
        tk.Label(frame, text=post["user"], fg="white", bg="black", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(frame, text="📹 Video", fg="white", bg="grey", width=40, height=15).pack(pady=5)
        tk.Label(frame, text=post["caption"], fg="white", bg="black").pack(anchor="w")
        
        # LIKE BUTTON ROW
        like_frame = tk.Frame(frame, bg="black")
        like_frame.pack(anchor="w")
        tk.Label(like_frame, text="❤️", fg="red", bg="black", font=("Arial", 14)).pack(side="left")
        tk.Label(like_frame, text=f" {post['likes']}", fg="white", bg="black").pack(side="left")
        tk.Button(like_frame, text="Like", command=lambda idx=i: like_post(idx), bg="red", fg="white").pack(side="left", padx=10)
        
        tk.Label(frame, text="--------------------------------", fg="grey", bg="black").pack()

refresh_feed()

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
