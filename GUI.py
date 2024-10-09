import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Create the main window
root = tk.Tk()
root.title("Codec")
root.geometry("800x400")  # Adjust window size

# Global variables to store file paths
file_path = ""
output_path = ""

# Function to select the input file
def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), ("WAV files", "*.wav"), ("BIN files", "*.bin")])
    if file_path:
        label_file_path.config(text="Input File: " + file_path)
        print(f"Selected input file: {file_path}") 

# Function to select the output file location based on input file type
def select_output_file():
    global output_path
    # Check the extension of the input file to decide the output file type
    if file_path.endswith(".wav"):
        output_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin"), ("All files", "*.*")])
        if not output_path:
            output_path = get_default_output_path("_encoded.bin")
    elif file_path.endswith(".bin"):
        output_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav"), ("All files", "*.*")])
        if not output_path:
            output_path = get_default_output_path("_decoded.wav")
    else:
        messagebox.showwarning("Warning", "Unsupported input file type")
        return

    if output_path:
        label_output_path.config(text="Output File: " + output_path)
        print(f"Selected output file: {output_path}") 

# Function to generate a default output file path based on operation (encode/decode)
def get_default_output_path(suffix):
    base_name = os.path.splitext(file_path)[0]
    default_output = base_name + suffix
    print(f"Generated default output path: {default_output}")  # Debug print
    return default_output

# Function to handle encoding
def encode_file():
    global output_path
    if file_path.endswith(".wav"):
        if not output_path:
            output_path = get_default_output_path("_encoded.bin")
        try:
            subprocess.run(['python', 'codec.py', '--encode_audio', file_path, output_path], check=True)
            messagebox.showinfo("Success", f"File has been encoded! Saved to: {output_path}")
            print(f"Encoded file saved to: {output_path}")  
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Encoding failed: {e}")
            print(f"Error during encoding: {e}")  
    else:
        messagebox.showwarning("Warning", "Please select a .wav file to encode.")

# Function to handle decoding
def decode_file():
    global output_path
    if file_path.endswith(".bin"):
        if not output_path:
            output_path = get_default_output_path("_decoded.wav")
        try:
            subprocess.run(['python', 'codec.py', '--decode_audio', file_path, output_path], check=True)
            messagebox.showinfo("Success", f"File has been decoded! Saved to: {output_path}")
            print(f"Decoded file saved to: {output_path}")  
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Decoding failed: {e}")
            print(f"Error during decoding: {e}") 
    else:
        messagebox.showwarning("Warning", "Please select a .bin file to decode.")

# Function to exit the program
def exit_program():
    root.quit()  # Close the main window and exit the program

# Create buttons and labels
btn_select_file = tk.Button(root, text="Select Input File", command=select_file)
btn_select_file.pack(pady=10)

btn_select_output_file = tk.Button(root, text="Select Output File", command=select_output_file)
btn_select_output_file.pack(pady=10)

btn_encode = tk.Button(root, text="Encode", command=encode_file)
btn_encode.pack(pady=10)

btn_decode = tk.Button(root, text="Decode", command=decode_file)
btn_decode.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=exit_program)
btn_exit.pack(pady=10)

label_file_path = tk.Label(root, text="No input file selected")
label_file_path.pack(pady=10)

label_output_path = tk.Label(root, text="No output file selected")
label_output_path.pack(pady=10)

# Start the main loop
root.mainloop()
