import math
import numpy as np

def hms2dec(h, m, s):
  return(15*(h + m/60 + s/(60*60)))

def dms2dec(h, m, s):
  mod = 1
  if h < 0:
    mod = -1
  return mod*(abs(h) + m/60 + s/(60*60))

# Write your import_bss function here.
def import_bss():
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  c = [(idx+1, hms2dec(item[0], item[1], item[2]), dms2dec(item[3], item[4], item[5]))for idx, item in enumerate(cat)]
  return c
  return tuple(map(tuple, cat))

def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  return [(idx+1, item[0], item[1]) for idx, item in enumerate(cat)]       

def angular_dist(ra1, dec1, ra2, dec2):
    d1 = np.radians(dec1)
    d2 = np.radians(dec2)
    r1 = np.radians(ra1)
    r2 = np.radians(ra2)
    b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
    a = np.sin(abs(d1 - d2)/2)*np.sin(abs(d1 - d2)/2)
    d = 2*np.arcsin(np.sqrt(a + b))
    return np.degrees(d)
  
# Write your find_closest function here
def find_closest(cat, ra, dec):
  dists = [angular_dist(i[1], i[2], ra, dec) for i in cat]
  return np.argmin(dists)+1, np.min(dists)

# Write your crossmatch function here.
def crossmatch(bss_cat, super_cat, max_dist):
  # for each in bss, 
  # find closest in super
  # if less than dist
  # add to match
  closest = []
  for idx, i in enumerate(bss_cat):
    k = list(find_closest(super_cat, i[1], i[2]))
    k.insert(0, idx+1)
    closest.append(tuple(k))
  matches = [tuple(item) for item in closest if item[2] <= max_dist]
  no_matches = [item[0] for item in closest if item[2] > max_dist]
  return matches, no_matches

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
