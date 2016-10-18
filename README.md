## Python Challange

Copyright (C) 2016 Cloudzfy. All Rights Reserved.

========================================================

This is a solution for [Python Challenge](http://pythonchallenge.com), a puzzle game website, which in the meantime, is a best place for Python beginner.

* **Level 0** [warming up](http://www.pythonchallenge.com/pc/def/0.html)
  
  * Just do the calculation 2<sup>38</sup> and put it in the URL address.

* **Level 1** [What about making trans?](http://www.pythonchallenge.com/pc/def/map.html)
  
  * Apply dictionary mapping to the encrypted text.

* **Level 2** [ocr](http://www.pythonchallenge.com/pc/def/ocr.html)

  * Check the comments in HTML source code, and find the rare characters.

* **Level 3** [re](http://www.pythonchallenge.com/pc/def/equality.html)

  * Check the comments in HTML source code, and find the substring with XXXxXXX.

* **Level 4** [follow the chain](http://www.pythonchallenge.com/pc/def/linkedlist.php)

  * There is a link on the image. Use the number as a clue to fine the tail of the linkedlist.

* **Level 5** [peak hell](http://www.pythonchallenge.com/pc/def/peak.html)

  * "Peak hell" sounds like `pickle`. Download the data from `<peakhell>` label and use `pickle` to extract information.
  * Trick: When printing the data from pickle, you may find the correlation between each character and its frequency.

* **Level 6** [now there are pairs](http://www.pythonchallenge.com/pc/def/channel.html)

  * Download the ZIP file `channel.zip` with a linkedlist based on the names of text files. Check `readme.txt`, You may use `zip.getinfo().comment` to retrieve comments of each text file in the ZIP.

* **Level 7** [smarty](http://www.pythonchallenge.com/pc/def/oxygen.html)

  * Check the gray bar in the image file, using `Image`. Note for gray color, R == G == B. Transfer the color into ASCII.

* **Level 8** [working hard?](http://www.pythonchallenge.com/pc/def/integrity.html)

  * The bee has link with username and password, which can be found in the HTML comment. Use `bz2` to decompress.

* **Level 9** [connect dots](http://huge:file@www.pythonchallenge.com/pc/return/good.html)

  * Connect the dots according to the coordinates of HTML comments, one by one.

* **Level 10** [what are you looking at?](http://huge:file@www.pythonchallenge.com/pc/return/bull.html)

  * Check the HTML comments for `len(a[30])`, it is a count-and-say.

* **Level 11** [odd even](http://huge:file@www.pythonchallenge.com/pc/return/5808.html)

  * The image provided could be sliced by odd and even. If you cannot find the clue, adjust the brightness of your screen.

* **Level 12** [dealing evil](http://huge:file@www.pythonchallenge.com/pc/return/evil.html)

  * Clue is hidden in the names of images. Since it is `evil1.jpg`, how about `evil2.jpg`, `evil3.jpg`, or even `evil4.jpg`. Not all the image file are image format. Do the file partition just like dealing with the cards.

* **Level 13** [call him](http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html)

  * You may find the number `5` is clickable. Use `xmlrpclib` to call him.

* **Level 14** [walk around](http://huge:file@www.pythonchallenge.com/pc/return/italy.html)

  * Sort the image file just like the bread.

* **Level 15** [uzi](http://huge:file@www.pythonchallenge.com/pc/return/uzi.html)

  * Use `calendar.isleap` and `datetime.date`, you may find it easy to get the year. Then check the history for Mozart and his father.

* **Level 16** [let me get this straight](http://huge:file@www.pythonchallenge.com/pc/return/mozart.html)

  * Get the image straight as the hint said. Use `a[1:]`.

* **Level 17** [eat?](http://huge:file@www.pythonchallenge.com/pc/return/romance.html)

  * You may find the image at the corner fimiliar. Check the browser cookies on Level 4, go through the linkedlist and gather the information hidden in the cookies.
  * Call Leopold using the phone.
  * Manually create the HTTP request with cookie `the+flowers+are+on+their+way`, Mozart's father will reply anyway.

* **Level 18** [can you tell the difference?](http://huge:file@www.pythonchallenge.com/pc/return/balloons.html)

  * First question is easy, `brightness` is the difference.
  * Download the file `deltas.gz` and unzip, compare the differences between the two parts of the text file, use `unhexlify`, and get three images finally.

* **Level 19** [please!](http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html)

  * Notice there is an email hidden in the HTML comments. By decoding the attachment, `indian.wav` was saying something about sorry.
  *Notice there are some redundent information in the data of the WAVE file, by simply removing it and changing the framerate, we can get the clue `idiot`.

* **Level 20** [go away!](http://butter:fly@www.pythonchallenge.com/pc/hex/idiot2.html)

  * By inspecting the image file `unreal.jpg`, you may find the response header is highly suspicous.
  * The `Range` field is unusual in the response headers, by adding and testing different number ranges of the field in an HTTP request, you will get a file talking about what you should do in the next level.

* **Level 21** package.pack

  * By checking the data inside the package, you may find it familiar. It is a file compress many times by ZLIB and BZ2 directly and reversely.
  * The log is more important than the original file.

* **Level 22** [emulate](http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html)
 
  * Download the GIF file `white.gif`, it is an animated GIF file, and there is a bright dot hidden inside. What we need to do is to figure out the trajectory of the dot's movement.

* **Level 23** [what is this module?](http://butter:fly@www.pythonchallenge.com/pc/hex/bonus.html)

  * This is actually a bonus level. Check `this` function in Python for more details.

* **Level 24** [from top to bottom](http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html)

  * Use Breath-First Search or Depth-First Search to check the path of the maze from top to bottom. BLACK color marks the entrance and exit, WHITE color marks the wall. The colors of the path are the data of a ZIP file.

* **Level 25** [imagine how they sound](http://butter:fly@www.pythonchallenge.com/pc/hex/lake.html)

  * Download the 25 WAVE files, which are almost noise by the way. Actually they are parts of the images, like a jigsaw.

* **Level 26** [be a man - apologize!](http://butter:fly@www.pythonchallenge.com/pc/hex/decent.html)

  * The title `apologize` reminds us about Mozart's father.
