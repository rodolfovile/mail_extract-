from optparse import OptionParser
import os.path
import re

'''
@author: Rdfl//VlN
'''

regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

def file_to_str(ark):
    with open(ark) as f:
        return f.read().lower()

def get_emails(s):
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog <ark>")
    #ADD OPTIONS IF YOU NEED !!!
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        exit(1)

    for arg in args:
        if os.path.isfile(arg):
            for email in get_emails(file_to_str(arg)):
                print email
        else:
            print '"{}" is not a file :(.'.format(arg)
            parser.print_usage()







