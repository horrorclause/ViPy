import optparse


parser = optparse.OptionParser('usage %prog -H ' + '<target host> -p <target port>')
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')

print(parser.usage)