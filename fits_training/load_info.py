from astropy.io import fits


# get info
hdulist = fits.open('m42_40min_red.fits')
hdulist.info()

# get shape
data = hdulist[0].data
print(data.shape)
