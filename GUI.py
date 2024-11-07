import tkinter as tk
from tkinter import filedialog, messagebox
import os
import codec 

root = tk.Tk()
root.title("Codec")
root.geometry("800x400") 

file_path = ""
output_path = ""

def select_file():
    global file_path, output_path
    file_path = filedialog.askopenfilename(filetypes=[("WAV and BIN files", "*.wav *.bin")])
    if file_path:
        label_file_path.config(text="Input File: " + file_path)
        output_extension = ".bin" if file_path.endswith(".wav") else ".wav"
        output_path = os.path.splitext(file_path)[0] + "_output" + output_extension
        label_output_path.config(text="Output File: " + output_path)
        print(f"Selected input file: {file_path}")

def select_output_file():
    global output_path
    if file_path:
        output_extension = ".bin" if file_path.endswith(".wav") else ".wav"
        output_path = filedialog.asksaveasfilename(defaultextension=output_extension,
                                                   filetypes=[("Binary files", "*.bin"), ("WAV files", "*.wav")])
        if output_path:
            label_output_path.config(text="Output File: " + output_path)
            print(f"Selected output file: {output_path}")

def process_file():
    if not file_path:
        messagebox.showerror("Error", "Please select an input file.")
        return

    if file_path.endswith(".wav") and output_path.endswith(".bin"):
        data, samplerate = codec.read_wav(file_path)
        codec.compress_to_bin(output_path, data, samplerate)
        messagebox.showinfo("Success", f"File encoded to {output_path}")
    elif file_path.endswith(".bin") and output_path.endswith(".wav"):
        data, samplerate = codec.decompress_from_bin(file_path)
        codec.write_wav(output_path, data, samplerate)
        messagebox.showinfo("Success", f"File decoded to {output_path}")
    else:
        messagebox.showerror("Error", "Invalid file selection. Please check input and output file types.")

def reset_selections():
    global file_path, output_path
    file_path = ""
    output_path = ""
    label_file_path.config(text="Input File: None")
    label_output_path.config(text="Output File: None")
    print("Selections have been reset.")

label_file_path = tk.Label(root, text="Input File: None")
label_file_path.pack(pady=10)

button_select_file = tk.Button(root, text="Select Input File", command=select_file)
button_select_file.pack(pady=5)

label_output_path = tk.Label(root, text="Output File: None")
label_output_path.pack(pady=10)

button_select_output = tk.Button(root, text="Select Output Location (Optional)", command=select_output_file)
button_select_output.pack(pady=5)

button_process = tk.Button(root, text="Process File", command=process_file)
button_process.pack(pady=20)

button_reset = tk.Button(root, text="Reset Selections", command=reset_selections)
button_reset.pack(pady=5)

root.mainloop()
