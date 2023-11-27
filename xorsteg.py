import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image
import sys
import time
def embed_text(image_path, text, output_path):
    message_bytes = text.encode() + b'\x00'

    image = Image.open(image_path)
    image_bytes = bytearray(image.tobytes())

    if len(message_bytes) * 8 > len(image_bytes):
        raise ValueError("Message too long to fit in the image")

    for i in range(len(message_bytes) * 8):
        image_bytes[i] &= 0xFE
        message_index, bit_index = divmod(i, 8)
        image_bytes[i] |= (message_bytes[message_index] >> bit_index) & 1

    image.frombytes(image_bytes)
    image.save(output_path)

def extract_text(image_path):
    stego_image = Image.open(image_path)
    image_bytes = stego_image.tobytes()
    message_bytes = bytearray()
    message_byte = 0

    for i, byte in enumerate(image_bytes):
        bit_index = i % 8
        message_byte |= (byte & 1) << bit_index
        if bit_index == 7:
            if message_byte:
                message_bytes.append(message_byte)
                message_byte = 0
            else:
                break

    try:
        return message_bytes.decode()
    except UnicodeDecodeError:
        return 'No valid message found.'

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")

        self.select_image_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_image_button.pack(pady=10)

        self.message_entry = tk.Entry(root, width=40)
        self.message_entry.pack(pady=10)

        self.embed_button = tk.Button(root, text="Embed Text", command=self.embed_text)
        self.embed_button.pack(pady=10)

        self.extract_button = tk.Button(root, text="Extract Text", command=self.extract_text)
        self.extract_button.pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(title="Select Image File")

    def embed_text(self):
        start_time = time.time()
        if not hasattr(self, 'image_path') or not self.image_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        text = self.message_entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter a message to embed.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")],
                                                    title="Save Embedded Image")

        try:
            embed_text(self.image_path, text, output_path)
            messagebox.showinfo("Success", "Text embedded successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        end_time = time.time()
        print("Embed time: " + str(end_time - start_time)) 
    def extract_text(self):
        start_time = time.time()
        if not hasattr(self, 'image_path') or not self.image_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        try:
            extracted_text = extract_text(self.image_path)
            print(sys.getsizeof(extracted_text))
            messagebox.showinfo("Extracted Text", extracted_text)
        except UnicodeDecodeError:
            messagebox.showinfo("Extracted Text", "No valid message found.")
        end_time = time.time()
        print("Extract time: "+ str(end_time - start_time))


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()