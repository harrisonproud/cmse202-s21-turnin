from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.wcs import WCS

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self, f1 = '', f2 = ''):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = f1
        self.im2_filename = f2
        self.load_images(self.im1_filename, self.im2_filename)
        
    def load_images(self, f1, f2):
        '''
        This function is taking the inputted data files and extracting the necessary data to complete our calculations
        '''
        self.red = fits.open(self.im1_filename)
        self.ir = fits.open(self.im2_filename)

        self.color_data = {f1: self.red[0].data,
                     f2: self.ir[0].data}
        
        return self.color_data
    
    def make_composite(self, im_dict):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
        # Define the array for storing RGB values
        rgb = np.zeros((im_dict[self.im1_filename].shape[0],im_dict[self.im1_filename].shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = im_dict[self.im1_filename].astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (im_dict[self.im2_filename].astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        rgb[:,:,1] = (((im_dict[self.im2_filename].astype("float") + im_dict[self.im1_filename].astype("float"))/2)/norm_factor) 
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0

        rgb[:,:,2] = (im_dict[self.im1_filename].astype("float")/norm_factor) 
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0

        hdu = fits.open(self.im1_filename)

        IR_Projection = WCS(hdu[0].header)

        plt.figure(figsize = (15,10))
        plt.imshow(rgb, origin = 'lower')
        plt.inferno()
        plt.grid()
        plt.xlabel('Right Acsension')
        plt.ylabel('Declination')