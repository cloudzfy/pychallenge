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

* **Level 9** [connect dots](http://www.pythonchallenge.com/pc/return/good.html)

  * To connect dots, you may check the HTML comments for the dots, and connect one by one.
  
  * Hint: Hmm, it's a male.

* **Level 10** [what are you looking at?](http://www.pythonchallenge.com/pc/return/bull.html)

  * Check the HTML comments for `len(a[30])`, you may find it is a count-and-say.

* **Level 11** [odd even](http://www.pythonchallenge.com/pc/return/5808.html)

  * The image provided could be sliced by odd and even. If you cannot find the clue, adjust the brightness of your screen.

* **Level 12** [dealing evil](http://www.pythonchallenge.com/pc/return/evil.html)

  * Clue is hided in the image. Since it is `evil1.jpg`, how about `evil2.jpg`, `evil3.jpg`, or even `evil4.jpg`. Not all the image file are image format. Do the file partition just like dealing with the cards.
  * Hint: Bert is evil! go back!

* **Level 13** [call him](http://www.pythonchallenge.com/pc/return/disproportional.html)

  * You may find the number `5` is clickable. Use `xmlrpclib` to call him.

* **Level 14** [walk around](http://www.pythonchallenge.com/pc/return/italy.html)

  * Rearrange the image file just like the bread.
  * Hint: its name is uzi.

* **Level 15** [uzi](http://www.pythonchallenge.com/pc/return/uzi.html)

  * Use `calendar.isleap` and `datetime.date`, you may find it easy to get the year. Then check the history.

* **Level 16** [let me get this straight](http://www.pythonchallenge.com/pc/return/mozart.html)

  * Get the image straight as the hint said. Use `a[1:]`.

* **Level 17** [eat?](http://www.pythonchallenge.com/pc/return/romance.html)

  * You may find the image at the corner fimiliar. Check the browser cookies for hint. Use `cookielib.CookieJar()` to retrieve cookie values.
  * Hint:
    * yummy! chocolate chips. 
    * do you want to eat or to play?
    * then go back and play.
    * If you came here from level 4 - go back! You should follow the obvious chain... and the next busynothing is 44827
  * Use `urllib.unquote_plus()` and `bz2` to unveil the code.
  * Call Leopold using the phone.
  * Hint: no! i mean yes! but ../stuff/violin.php.
  * Use `cookielib.Cookie` to create cookie for request.

* **Level 18** [can you tell the difference?](http://www.pythonchallenge.com/pc/return/balloons.html)

  * First question is easy, `brightness` is the difference.
  * Check the comment, you may find the file `deltas.gz`, which is a text file, but needed to be compare using `difflib.Differ`. To convert the text back to hex, use `binascii.unhexlify`.

