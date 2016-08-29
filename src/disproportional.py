import xmlrpclib

server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.system.listMethods()
print server.system.methodHelp('phone')
print server.phone('Bert')