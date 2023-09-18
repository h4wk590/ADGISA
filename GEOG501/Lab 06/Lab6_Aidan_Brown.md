
# Aidan Brown
# GEOG 501 Fall 2023

## Deliverable 1

Screen capture(s) of the movement paths for Yana and Lena; include the original tracking points
and a basemap:


![Pasted image 20230915165349.png](../../attachments/Pasted%20image%2020230915165349.png)

![Pasted image 20230915165307.png](../../attachments/Pasted%20image%2020230915165307.png)

## Deliverable 2

Describe the seasonal movement pattern of each of the two bears for the time period
considered. What behavior could explain their movements? 

Many points of travel are observed on the landmasses, this could indicate the bears hibernating and producing cubs. During this time the sea is frozen over so they must stay on land during hibernation. When spring and summer approach and the ice melts, it opens up more opportunities for the bears to hunt. You can see the poly-lines that go from **Svalbard** to points on the ocean, as these points may indicate hunting sessions.

# Deliverable 3

What distance did each bear travel over the time period considered, from October 2002 to
February 2004?

- Yena traveled **3705 KM**.
- Yana traveled **1637 KM**.

## Deliverable 4

Based on the fields for the address components in the reference data, which geocoding style is
best to use? Explain your answer.

Using **US Street address dual ranges** (Street Address) would best suit the reference data for this example, as the reference data provides some information about address ranges along streets. Furthermore, there is specific **street direction**, and **street numbers** components, there will need to be geocoordinates for each side of a polyline to indicate where a specific address will be located.   


## Deliverable 5

Screen capture of your address locator settings. Make sure to show a screen capture of the
style (under About the locator) and the field map showing the fields (under Reference data tables):

![Pasted image 20230915164031.png](../../attachments/Pasted%20image%2020230915164031.png)

![Pasted image 20230915164636.png](../../attachments/Pasted%20image%2020230915164636.png)

## Deliverable 6

How many drug crime events were matched or tied using the default settings? How many remain
unmatched?

- ADDRESS, CITY, and STATE were matched (3).
- OID, CSEDAT, OFFENSE, and CRIME_TYPE where unmatched (4).

## Deliverable 7

Screen capture of your map with the centerlines and the geocoded drug crime locations:


![Pasted image 20230917145312.png](../../attachments/Pasted%20image%2020230917145312.png)

## Deliverable 8

For each of the following unmatched addresses, what was the reason no matches were found:

- **2700 TRAMWAY VISTA BLVD NE** - The Centerlines table did not include this address so it was not found by any matches when geocoding.
- **500 COLE LA SW** - This could be an error in the address number in the drug crimes data. As looking in the attribute table from the reference data, COLE LA starts at 6200, and ends at 6299.
- **7200 MIAMI ST NE** - Although MIAMI RD exists in the reference data table, there is no **MIAMI ST** anywhere found in the reference data.
- **100 KATHRYN AV SE** - There are 2 entries in the reference data table without any data, in the house number columns. These two could be where 100 KATHRYN AV SE would reside, but without the exact numbers it was unmatched.
- **2957 ARENAL ST SW** - Only ARENAL RD exists in the reference data, it was unmatched because ARENAL ST does not exist in the reference data.
- **444 LUNA AV** - LUNA AV does not exist in the reference data.

## Deliverable 9

How many drug crime events were matched or tied using the new settings? How many are still
unmatched:

- 1080 matched
- 1 tied
- 690 Unmatched 







