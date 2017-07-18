from astropy.io import fits
import matplotlib.pyplot as plt

hdulist = fits.open('m42_40min_red.fits')
data = hdulist[0].data

# plot
plt.imshow(data, cmap=plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar
plt.show()
