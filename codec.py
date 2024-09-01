import sys
import wave
import struct

def encode(input_stream, output_stream):
    with wave.open(input_stream, 'rb') as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(wav_file.getnframes())
    
    # Print parameters for debugging
    print(f"Debug - WAV parameters: {params}", file=sys.stderr)
    
    # Extract only the required integer parameters
    int_params = (params.nchannels, params.sampwidth, params.framerate, params.nframes)
    
    # Simple compression: keep only every 4th sample
    compressed = b''.join([frames[i:i+2] for i in range(0, len(frames), 8)])
    
    # Write compressed data
    output_stream.write(struct.pack('4I', *int_params))
    output_stream.write(compressed)

def decode(input_stream, output_stream):
    # Read parameters
    nchannels, sampwidth, framerate, nframes = struct.unpack('4I', input_stream.read(16))
    
    # Read compressed data
    compressed = input_stream.read()
    
    # Simple decompression: repeat each sample 4 times
    decompressed = b''.join([sample[0] * 4 for sample in struct.iter_unpack('2s', compressed)])
    
    # Write WAV file
    with wave.open(output_stream, 'wb') as wav_file:
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.writeframes(decompressed)

def main():
    if len(sys.argv) != 2:
        print("Usage: python codec.py --encode|--decode")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "--encode":
        encode(sys.stdin.buffer, sys.stdout.buffer)
    elif mode == "--decode":
        decode(sys.stdin.buffer, sys.stdout.buffer)
    else:
        print("Invalid mode. Use --encode or --decode.")
        sys.exit(1)

if __name__ == "__main__":
    main()