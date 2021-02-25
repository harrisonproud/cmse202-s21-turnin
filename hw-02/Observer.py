from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images():
        '''
        This function is taking the inputted data files and extracting the necessary data to complete our calculations
        '''
        red = fits.open(f1)
        ir = fits.open(f2)

        color_data = {f1: red[0].data,
                     f2: ir[0].data}
        
        return color_data
    
    def make_composite(self):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
        # Define the array for storing RGB values
        rgb = np.zeros((self.im1_data.shape[0],self.im1_data.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_data.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        rgb[:,:,1] = (((im_dict[f2].astype("float") + im_dict[f1].astype("float"))/2)/norm_factor) 
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0

        rgb[:,:,2] = (im_dict[f1].astype("float")/norm_factor) 
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0

        hdu = fits.open(f1)

        IR_Projection = WCS(hdu[0].header)

        plt.figure(figsize = (15,10))
        plt.imshow(image_data_ir, origin = 'lower')
        plt.inferno()
        plt.grid()
        plt.xlabel('Right Acsension')
        plt.ylabel('Declination')