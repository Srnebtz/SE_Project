import sys
import wave

def encode(input_file, output_file):
    with wave.open(input_file, 'rb') as wav_file, open(output_file, 'wb') as out_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(wav_file.getnframes())

        # Print parameters for debugging
        print(f"Debug - WAV parameters: {params}", file=sys.stderr)

        # Write raw PCM data to .bin file
        out_file.write(frames)

        print(f"Encoded {len(frames)} bytes to {output_file}", file=sys.stderr)

def main():
    if len(sys.argv) != 4 or sys.argv[1] != "--encode":
        print("Usage: python encoder.py --encode input.wav output.bin")
        sys.exit(1)

    input_file = sys.argv[2]
    output_file = sys.argv[3]
    encode(input_file, output_file)

if __name__ == "__main__":
    main()