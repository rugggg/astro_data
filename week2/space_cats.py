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


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
