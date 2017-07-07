import system

PASSWD = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

for i in xrange(1000, 10000):
	os.system("echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ %s | nc 127.0.0.1 >> result" % PASSWD)
