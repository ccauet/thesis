#!/usr/bin/env python

import os
import re
import pexpect

patterns = ['Words in text', 'Words in headers', 'Words outside text (captions, etc.)', 'Number of math inlines', 'Number of math displayed']

def get_subcount(text, pattern):
  match = re.compile('(.*'+pattern+'.*:)\s+([0-9]*)').search(text)
  n = 0
  if match:
     n = int(match.group(2))
  return n

if __name__ == "__main__":
  print "Counting words..."
  n_total = 0
  
  path = os.getcwd()+'/content/content.tex'
  out = pexpect.run('/usr/texbin/texcount '+path)
  for pattern in patterns:
    n_total = n_total + get_subcount(out, pattern)
    
  print 'Total:', n_total
