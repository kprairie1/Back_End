import pyaudio
import wave

form_1 = pyaudio.paInt16
audio = pyaudio.PyAudio()
numChannels = 1
sample_rate = 44100
chunk = 4096
record_secs = 3

for i in range(audio.get_device_count()):
	if("USB" in p.get_device_info_by_index(i).get('name')):
		index = i
		break

stream = audio.open(format = form_1, rate = sample_rate, channels = numChannels, 
					input_device_index = index, input = True, frames_per_buffer = chunk)

print("Recording")
frames = []

for i in range (0, int((sample_rate/chunk) * record_secs)):
	data = stream.read(chunk)
	frames.append(data)
	
print("Finished Recording")

stream.stop_stream()
stream.close()
audio.terminate()

wavefile = wave.open("Test.wav", 'wb')
wavefile.setnchannels(numChannels)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.writeframes(b''.join(frames))
wavefile.close()
