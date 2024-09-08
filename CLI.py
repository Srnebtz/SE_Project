import os
import sys
from encoder import encode
from decoding import decode_bin_to_wav

def list_files(extension):
    """List files in the current directory with the given extension."""
    files = [f for f in os.listdir() if f.endswith(extension)]
    return files

def select_file(extension):
    """Prompt the user to select a file from a list of files with the given extension."""
    files = list_files(extension)
    if not files:
        print(f"No {extension} files found in the current directory.")
        return None
    print(f"\nAvailable {extension} files:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    choice = input(f"Select a file (1-{len(files)}) or press Enter to use the default: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(files):
        return files[int(choice) - 1]
    return None

def encode_file():
    input_file = select_file(".wav") or "input.wav"
    output_file = "output.bin"
    encode(input_file, output_file)
    print(f"Encoding complete. The file has been saved as {output_file}")

def decode_file():
    input_file = select_file(".bin") or "input.bin"
    output_file = "output.wav"
    decode_bin_to_wav(input_file, output_file)
    print(f"Decoding complete. The file has been saved as {output_file}")

def main():
    print("Welcome to the Audio Codec CLI!")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Encode a WAV file to binary")
        print("2. Decode a binary file to WAV")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            encode_file()
            input("Press Enter to return to the main menu...")  # Pause to allow user to see the result
        
        elif choice == "2":
            decode_file()
            input("Press Enter to return to the main menu...")  # Pause to allow user to see the result
        
        elif choice == "3":
            print("Thank you for using the Audio Codec CLI. Goodbye!")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to try again...")  # Pause before returning to the main menu

if __name__ == "__main__":
    main()
