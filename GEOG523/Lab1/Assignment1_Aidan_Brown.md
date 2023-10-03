
# Aidan Brown
# GEOG 523 Fall 2023


## Question 1: 

On what date (y/m/d) was this image acquired?

- 1999/09/21/


Question 2: What is the coordinate system for this image? More specifically, what are the projection and its parameters, what is the datum, and what are the imagery’s coordinate bounds (in the Geographic coordinates)?

- Projection: UTM
- Datum: NAD83
- Coordinate Bounds: 

LL latitude - 048.248639696
LL longitude - -125.917169
UL latitude - 049.819597571
UL longitude - -125.3179582
LR latitude - 047.896828387
LR longitude - -123.5026422
UR latitude - 049.455307073
UR longitude - -122.8331045

## Question 3: 

What are the dimensions of a multispectral band? How many lines (rows) and pixels (columns)?

- Number_of_pixels_multi - 7690
- Number_of_lines_multi - 7346


## Question 4: 

What approximate ground area (in sq. km including null pixels) does this Landsat image cover? Show your calculations. Tip: Open any multispectral band of 048026_0100_990921_l7_X_utm10.tif in ArcGIS and examine grid cell size or spatial resolution parameter for a pixel from the Layer Properties dialog.

Columns * Rows  * Cell Size * 0.3 (7690 * 7344 * 30 * 30 ) = 

**50340 km2**

## Question 5:

What is the approximate file size of the L8_Island.pix file you created from the multiple Landsat 8 multispectral GEOTIFF files? How does it compare to the L7_Island.pix file you created? What would explain such a large discrepancy between the file sizes?

- The file size of L8_Island.pix is approximately 1GB,  Whereas L7_Island.pix is approximately 340 MB. 
- L8 being a lot newer than L7 would improve image quality as technology advances. This would improve the spectral bands of L8 and provide more image details, resulting in larger file sizes.


## Question 6:

What is the common name for the combination of bands and what are the computer display colors that are now  What is the common name for the combination of bands and what are the computer display colors that are now loaded?


- Common colour name: **True Colour Composite**
- Band 3 is RED, Band 2 is GREEN, Band 1 is BLUE.

## Question 7:

What is the common name for the combination of bands and what are the computer display colors that are now loaded?

-  Common colour name: Panchromatic
- RGB are within the 4th channel. 

## Question 8:

What is the common name for the combination of bands and what are the computer display colors that are now shown?

- Common colour name: **False Colour Composite**.
- Band 4 is red, Band 3 is Green, Band 2 is blue.

## Question 9:

What differences (at least two) do you notice between these two versions (Band 3-2-1 and Band 4-3-2) of the image?

- **Viewability between the two as a user.** Band 3-2-1 displays colour accurate representations of what the colours look in reality.
- Band 4-3-2 uses Near infrared in this case, so the extent of this band is generally for a more analytical view of the map, whereas band 3-2-1 is for viewability.


## Question 10

Briefly describe a color and band combination (other than those used above) that you feel provides a useful depiction of the study area and explain why.

- Band 6-3-1

depicts the bodies of water as emphasized, and also very much outlines the city structures and roads against the natural geology and forested area around the area,


## Question 11

What is the common name for the combination of bands and what are the computer display colors that are now loaded?

- The common name for the combination: **True Colour Composite**.
- (3-2-1 RGB) resembles close to the human eye. Forested/plant areas being green, geology and man-made structures are defined as brown and white, water is blue.

## Question 12

Experiment with displaying the two images at different zoom levels. What do you think is the largest scale at  which each image (Landsat 7 and QuickBird) can be displayed and still being useful? Tip: you can see a zoom level at the left corner of bottom information bar:

- **QuickBird:** 52,500 scale size has the best viewability of the entire map extent, going any further doesn't capture the entire map extent.
- **L7_Nanaimo**: 420,000 scale size has the best viewability for this extent, increasing the scale too little or too much here results in a lot of image distortion.






