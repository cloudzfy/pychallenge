import urllib
import re
import email
import wave

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html').read()
text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->').findall(src)[0]

msg = email.message_from_string(text[1:])

for index, part in enumerate(msg.walk()):
	if part.get_content_type() == 'audio/x-wav':
		file = open('indian.wav', 'wb')
		file.write(part.get_payload(decode=True))
		file.close()
		print 'indian.wav'

wav1 = wave.open('indian.wav', 'r')
wav2 = wave.open('idiot.wav', 'w')
wav2.setnchannels(1)
wav2.setsampwidth(wav1.getsampwidth())
wav2.setframerate(wav1.getframerate() // 2)
wav2.writeframes(wav1.readframes(wav1.getnframes())[0::2])
wav1.close()
wav2.close()
print 'idiot.wav'