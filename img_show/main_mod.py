from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, filedialog

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        try:
            image = Image.open(file_path)
            image.thumbnail((500, 500))  # 画像サイズを調整する場合は適宜変更してください
            image_tk = ImageTk.PhotoImage(image)

            label.configure(image=image_tk)
            label.image = image_tk  # 参照を保持するために必要です

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open the image: {str(e)}")

# Tkinterウィンドウの作成
window = tk.Tk()
window.title("Image Viewer")

# 画像表示用のラベル
label = tk.Label(window)
label.pack()

# ボタン
button = tk.Button(window, text="Open Image", command=open_image)
button.pack()

# ウィンドウを表示
window.mainloop()
