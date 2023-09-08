

# Aidan Brown
# GEOG 501 Fall 2023


## Deliverable 1

| From | To | Distance (Planer) in km | Distance (geodesic) in km |
| ---- | -- | ----------------------- | ------------------------- |
| Quito, Ecuador | Nairobi, Kenya | 12,842 KM | 12,844 KM |
| Miami, USA | Barcelona, Spain | 9,408 KM | 7,569 KM |
| Vancouver, Canada | Amsterdam, the Netherlands | 14,245 KM | 7,710 KM |

## Deliverable 2

What is the relationship between latitude and the magnitude of distortion (based on distance)
for the Mercator projection? Briefly explain your answer:

Because the first comparison of the two cities (Quito, and Nairobi) are essentially on or near the equator, the measurements are less distorted and more accurate when using the World Mercator. While the other two comparisons are further away from the equator, the measurements become more distorted as a result.

## Deliverables 3 and 4:


**A. Mercator (World) projection:**

![Pasted image 20230908105919.png](../../attachments/Pasted%20image%2020230908105919.png)
This projection clearly shows that anything on and around the equator is more accurately depicted, while towards the poles the map is more distorted and therefore less accurate.

**B. Robinson (World) projection:**

![Pasted image 20230908110140.png](../../attachments/Pasted%20image%2020230908110140.png)

This projection doesn't have the most equal area, but provides a greater detail of accuracy everywhere on the Earth besides the Poles, where the points of the poles are stretched and extremely distorted.

**C.  Times (World):**

Almost a fully cylindrical projection, but bulges out noticeably at the equator. Similarly to Mercator world distortion happens at the extreme level towards each of the poles, notice the size of Greenland in this projection and how large and distorted it is.

![Pasted image 20230908110456.png](../../attachments/Pasted%20image%2020230908110456.png)


**D. Cylindrical Equal Area (World):**

This is a cylindrical projection that maintains consistency as all the cells are equal in size which only causes distortion towards the very top and bottom of the map extent. 

![Pasted image 20230908111854.png](../../attachments/Pasted%20image%2020230908111854.png)

## Deliverable 5

Report the following details about the coordinate system:

• official name in ArcGIS: **USA Contiguous Albers Equal Area Conic.**
• central meridian: **-96.0**
• standard parallel 1: **29.5**
• standard parallel 2: **45.5**

## Deliverable 6

Do these projection parameters follow the rules for conic projections? Explain your answer in
detail (i.e. including any necessary calculations).

- RULES 

The central meridian should run through the middle of the region of interest
• The reference latitude should be placed wherever you think the center of a coordinate system should be
(usually either at the center or below the bottom of the extent of the geographic features).
• As a general rule, the two standard parallels should be located approximately 1/6 from the bottom and 1/6
from the top of the geographic extent of the mapped features. This is known as the “One-Sixth Rule” for conic
projections.

## Deliverable 7

Screen capture of Canada in the Lambert projection, including meaningful symbology as
described above:

![Pasted image 20230908135725.png](../../attachments/Pasted%20image%2020230908135725.png)

## Deliverable 8

State your chosen area of interest and report the name and complete details of your selected
coordinate system (copied from ArcGIS):

- Area of Interest: **British Columbia**


![Pasted image 20230908142057.png](../../attachments/Pasted%20image%2020230908142057.png)

## Deliverable 9

Separate from the complete technical details, report the following about the coordinate system:
geodetic datum, family (e.g. conic, cylindrical, planar) and type (e.g. Albers, Lambert, Mercator etc.):

- Geodetic datum: **NAD 1983**.
- Family: **Conic**.
- Type: **Albers**.

## Deliverable 10

 Take a clean screen capture of your resulting data view, similar to the one above:

![Pasted image 20230908150247.png](../../attachments/Pasted%20image%2020230908150247.png)
