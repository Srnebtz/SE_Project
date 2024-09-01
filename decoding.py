import wave
import struct

def decode_bin_to_wav(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    # Assuming each sample is 16-bit (2 bytes), sample rate is 44100Hz, and mono audio
    sample_width = 2
    sample_rate = 44100
    num_channels = 1

    # Calculate the number of samples
    num_samples = len(data) // sample_width

    # Create the WAV file
    with wave.open(output_file, 'w') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(sample_rate)

        # Convert binary data to WAV sample data
        samples = struct.unpack('<' + 'h' * num_samples, data)
        wav_file.writeframes(struct.pack('<' + 'h' * num_samples, *samples))

if __name__ == "__main__":
    input_filename = "payload.bin"
    output_filename = "output.wav"
    decode_bin_to_wav(input_filename, output_filename)
    print(f"Decoding complete. Output file is {output_filename}")
