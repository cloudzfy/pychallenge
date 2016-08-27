from string import maketrans

s1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw "
s2 = "fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq "
s3 = "pcamkkclbcb. lmu ynnjw ml rfc spj."

s = s1 + s2 + s3

mfrom = maketrans('', '')[97:123]
mto = mfrom[2:26] + mfrom[0:2]
print s.translate(maketrans(mfrom, mto))

url = 'map'
print url.translate(maketrans(mfrom, mto))
