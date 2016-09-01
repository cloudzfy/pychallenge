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

import md5
import zipfile
import StringIO
import Image

file = open('mybroken.zip')
src = file.read()
file.close()

for i in range(len(src)):
	for j in range(256):
		changed = src[:i] + chr(j) + src[i+1:]
		if md5.md5(changed).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
			src = changed
			break

z = zipfile.ZipFile(StringIO.StringIO(src))
Image.open(StringIO.StringIO(z.read('mybroken.gif'))).show()
