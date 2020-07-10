import re
import linkGrabber
import time

time.sleep(8)

links = linkGrabber.Links('https://www.thewarehouse.pk/womens-caps-hats')
gb = links.find(limit=2000,duplicates=False,pretty=True)
print(gb)
