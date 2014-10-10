from selenium import webdriver
from PIL import Image
import sys
import time

if (len(sys.argv) != 3):
    print "Usage: python %s filename baseurl" % sys.argv[0]
    print "  baseurl sample "
    quit()
fi = open(sys.argv[1])
baseurl=sys.arv[2]
line = fi.readline()
while line:
    line = line.rstrip()
    print line
    f = line.split(',')
    line = fi.readline()
    fox = webdriver.Firefox()
    fox.set_script_timeout(30000)
    fox.implicitly_wait(30000)
    
    if len(f)==3:
        print "[%s][%s][%s]" % (f[0], f[1], f[2])

        fox.get(baseurl+'/?name='+f[0]+'%3A'+f[1]+'..'+f[2])
        # now that we have the preliminary stuff out of the way time to get that image :D
        time.sleep(30)
        fox.save_screenshot('screenshot_'+f[0]+'_'+f[1]+'_'+f[2]+'.png') # saves screenshot of entire page
        fox.quit()
    else:
        print "[%s]" % (f[0])

        fox.get(baseurl+'/?name='+f[0])
        time.sleep(30)

        # now that we have the preliminary stuff out of the way time to get that image :D
        fox.save_screenshot('screenshot_'+f[0]+'.png') # saves screenshot of entire page
        fox.quit()
        

