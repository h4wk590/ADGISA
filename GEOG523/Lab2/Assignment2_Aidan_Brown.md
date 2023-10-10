
## Aidan Brown
## GEOG 523 Fall 2023



## Question 1

What does the histogram represent in general?

- The distribution of pixel values from 0 - 255 of the raster image.

## Question 2

Which spectral band has the largest frequency distribution range of brightness values? Support your  
claim by providing the minimum and maximum pixel values.

- **Band 4** has the largest distribution range of brightness values. Minimum value of 1, and maximum value of 198

## Question 3

Which band has the smallest frequency distribution range of brightness values? Support your claim by  
providing the minimum and maximum pixel values.


- **Band 2** has the smallest frequency of brightness values. The minimum pixel value is 18, and the highest is 175.

## Question 4

Which of two bands have the most similar histograms’ appearance (in terms of the shape and form of  
the histograms)? Explain your choice.

- **Band 1** and **Band 2**

These two bands have a very similar curve, and very similar highest pixel counts at around 12,000 for each histogram. 

## Question 5

Give one example of two bands that have very different histograms. Explain what makes these  
histograms different and relate your explanation back to the actual display of ground features within bands?

- **Bands 3 & 5**

The histography is immediately different visually as a first major difference between these two bands. Band 3 has a spike in terms of displaying more black values most likely showing more of the vegetation and water, while Band 5 has a small curve in the middle of the graph indicating more grey values to do with vegetation on the map.

## Question 6

![Pasted image 20231003122923.png](../../attachments/Pasted%20image%2020231003122923.png)

![Pasted image 20231003113827.png](../../attachments/Pasted%20image%2020231003113827.png)

Comment on the overall difference in pixel brightness values between the two image dates. By  
identifying Sub1999-1990-pixel values, provide at least three different examples (and their DNs, X, Y coordinates) of features that do not have experienced any change from September 1990 to September 1999.


| X Coordinate | Y Coordinate | Numeric Value 1999 - 1990 | Numeric Value ETM |
| -------| -------- | -------- | -------- |
| 123°53'09.1447"W | 49°03'15.5152"N | 119 | 119 |
| 123°53'03.2877"W | 49°03'09.8038"N | 90 | 90 |
| 123°49'48.0275"W | 49°06'57.2964"N | 60 | 60 |


## Question 7

Identify Sub1999-1990-pixel values over the deep ocean surface. What factors might cause minor  
overall difference in brightness between the two multi-date images?

- Clouds may get in the way of the remote sensor when gathering images.
- Ocean currents, may cause variations because of forming waves.
- Day time versus night time sensing may cause slight variations.

## Question 8

- Day and Month Acquisition 

1. **Crop yields** - Crop yields will have similar dates each year so day and month acquisition matters a lot here, where one is able to see the direct effects of crop yields every year and compare data.
2. **Environmental disasters** - Analyzing water levels for hurricanes, and floods, or precipitation levels for droughts are good examples of day and month acquisition needing to be as similar as possible to more closely analyze environmental data.


- Images Acquired by the same Sensor

When doing different types of analysis, such as urban development. The changes of the development should be as accurate as possible between growth or infrastructure changes.
## Question 10

![Pasted image 20231010100539.png](../../attachments/Pasted%20image%2020231010100539.png)
RVI1990 image

![Pasted image 20231010100617.png](../../attachments/Pasted%20image%2020231010100617.png)
RVI 1999 image.

Based on the visual nature of the images, and the following histogram comparisons:

![Pasted image 20231010101000.png](../../attachments/Pasted%20image%2020231010101000.png)
we can visually see that there is more vegetation in 1990 compared to 1999. There are more 4.0 number values in the 1990 histogram, and 5.0 values, which the 1999 histogram omits completely. We can come to the conclusion that Nanaimo went through a large amount of urban development and logging between the years of 1990 - 1999.

## Question 11

When viewing the attribute tables to compare pixel values of RVI1990 to RVI1999:

![Pasted image 20231010102736.png](../../attachments/Pasted%20image%2020231010102736.png)

**114.1102 km2** in area was lost between the years of 1990 - 1999. To get this value I added all pixel values that are => 4, and subtracted the greater value to the smaller value to get the number in sq meters, then converted to sq km.

## Question 13

- **Vegetation Density** - Based on the density of the forests and vegetation between 1990 and 1999, there will be variations in RVI reflection.
- **Types of Plants** - Different plant species will provide different levels of reflection based on the area. For instance, parks in the urban areas of Nanaimo will have lower reflection than that of high density forested areas near and on Mount Benson.
- **Changing of Seasons** -  Reflection and RVI values will greatly differ between each season.














