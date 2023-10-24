
## Aidan Brown
## GEOG 523 Fall 2023

## Question 1

- Match_Addr - Contains the matched address from the geocoded output.
- Status - Contains the results of geocoding for each address.
- Score - The quality of the match based on the data that was input.
- Addr_type - Types of addressed that were matched (Street vs intersection).
- LatLong - Geographic coordinates that are mapped to each mapped location.

## Question 2

- Geocoding takes many inputs and tries to validate those inputs into a score based system. Many factors can effect the score, like not having the data validated before-hand, or using locations that aren't centralized to a specific region or city. The more spread the coordinates are, the chances of unmatched addresses can be greater. The score system is a generalized quality of measure of the input data.

## Question 3

- A score value of 72 would mean it would not be a good match in our case, as the minimum match score is set to 72.
- and R side means that the match was made on the **right** side of a street.

## Question 4

- The actual address for **Bright Beginnings Early Childhood Centre** is **22 Cortex Pl**, but the locator picked up another address on that same street.

## Question 5

- We could improve the standards of the process of inputting attribute data. For example, all 'streets' attributes could be prefixed to 'St.' This simple change would improve the match score to 100%. Or we could create an entire new field called "street type", to indicate whether it is a street, Cal-de-sac, avenue, etc.

## Question 6

- Postal code results matched 100% (20/20 matches). Postal codes are much more standardized than street addresses, and are province based, which lends to accuracy. Attributes like street prefixes, or numbered streets (5th St. for example) skew results more often than not.

## Question 7

- the result of both address and postal codes are very similar when viewed at a certain angle. Pictured below are street address points as <i>blue pins</i>, and postal code points as <i>green points</i>:

 ![Pasted image 20231024012514.png](../../attachments/Pasted%20image%2020231024012514.png)

But when zooming in, the accuracy of the actual place of interest (in our case the childhood centres), we see that the address pins are much clearer to the data we want:
![Pasted image 20231024012706.png](../../attachments/Pasted%20image%2020231024012706.png)

## Question 8

### Address Advantages

- Highly detailed - Includes information such as, street names, building numbers, direction.
- Validation - Suppose you needed to find out if a location/building still exists, or need to look at a specific location for a new office building.
###  Address Disadvantages 

- Input data can easily be prone to human error or be incomplete.
- Data volume - large amounts of data increases storage and processing times.
### Postal Advantages

- Simple - Only one field is required and that is the postal code itself, so less prone to human error.
- Data - Quicker processing times, less storage needed.
- Good for mapping large areas of interest if not interested in specific addresses.

### Postal Disadvantages

- Not as precise - The geocoded postal codes are mapped to the center of that area, so may increase difficulty finding many addresses in 1 area.
- Information - Does not include any other information, like street number, building number, intersection, etc. 

## Question 9

- The geocoded points inherit the projected coordinate system of the current project. In this case the coordinate system used is **NAD 1983 UTM Zone 10N**.

## Question 10

- The object type is POI (point of interest) according to the attribute table.

## Question 11

The groups are within the same network but are segregated by the type of grouping that they are. In this case both are transportation routes, but do not interact with each other, however we need them both within our network study area.

## Question 12

The topology connectivity must be established beforehand as it defines the spatial integrity of the network. without it routing, and spatial analysis could not be performed on the network. For example, the ferry schedule could change based on weather conditions, the network needs to be defined to allow the ferries new route to change based on the schedule.

## Question 13





 






