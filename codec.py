import soundfile as sf
import numpy as np
import io

def read_wav(file_path, downsample_factor=1):
    data, samplerate = sf.read(file_path)
    if downsample_factor > 1:
        data = data[::downsample_factor] 
        samplerate //= downsample_factor
    return data, samplerate

def compress_to_bin(file_path, data, samplerate):
    with io.BytesIO() as flac_buffer:
        sf.write(flac_buffer, data, samplerate, format='FLAC')
        compressed_data = flac_buffer.getvalue() 
    with open(file_path, 'wb') as bin_file:
        bin_file.write(compressed_data) 

def decompress_from_bin(file_path):
    with open(file_path, 'rb') as bin_file:
        flac_data = bin_file.read()
    with io.BytesIO(flac_data) as flac_buffer:
        data, samplerate = sf.read(flac_buffer)
    return data, samplerate

def write_wav(file_path, data, samplerate):
    sf.write(file_path, data, samplerate, format='WAV')
