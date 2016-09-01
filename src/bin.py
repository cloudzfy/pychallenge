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

# Email received from Leopold Mozart:
#
# From: "Leopold Mozart" <leopold.moz@pythonchallenge.com>
# Date: Thu, 1 Sep 2016 01:39:31 -0700
# Message-ID: <CALLh7wynAe1OncB50MLBVeTLwG7HT8=-BRKx-gg1zAga2iZPeA@mail.gmail.com>
# Subject: Re: my broken zip Re: sorry
# MIME-Version: 1.0
# Content-Type: text/plain; charset=UTF-8
# Content-Transfer-Encoding: 7bit
# Content-Disposition: inline
# Precedence: bulk
# X-Autoreply: yes
# Auto-Submitted: auto-replied
# 
# Never mind that.
# 
# Have you found my broken zip?
# 
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
# 
# Can you believe what one mistake can lead to?
