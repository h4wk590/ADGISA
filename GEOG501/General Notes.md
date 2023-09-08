

## What is GIS?

- A way to analyze, and Visualize spatial data computationally, usually via maps.
- A way to communicate data for anyone to see. (hard to visualize a database as is.)
- Helps organizations, and governments, and people solve complex geographical issues.

##  Why GIS?

- Specific needs of the individual/organization

**Think about how to visualize a problem using GIS..**

- Emergency response systems that show the quickest way to get to a destination
- Wanting to know where parks benches and picnic tables are in a specific park, or all parks in a city?
- Using business intelligence to track customer spending trends based on store locations.
- Mapping tree density and managing tree growth status within forestry.

## ArcGIS Tips

- Right click attribute table and select **statistics** for quick sums of selected objects. 

### Creating Feature Class from CSV Coordinate System

- Right click csv file from the catalog view:

![Pasted image 20230907143217.png](../attachments/Pasted%20image%2020230907143217.png)

- Hover over **export** and select either line, polygon, or ellipse feature class.

![Pasted image 20230907143414.png](../attachments/Pasted%20image%2020230907143414.png)



## Discrete vs Continuous 

Why is soil discrete and not continuous?

- Different types of soils
- Soil levels and elevation types

## Key Differences Between Raster and Vector Data

### Vector Data

- Vector Data is real world data
- Geometry can be polygons, lines, points. (map scale matters for each of these)
- Attribute tables provide info about the features (like a building, roads, telephone pole.)

### Raster Data

- Raster data is a grid of equally sized cells 
- Each cell can contain different information such as
- Elevation
- Temperature
- air pressure
- Raster data does not have an attribute table


## Metadata

 Metadata describes GIS content by providing:

- Description of the content and intended use
- Author
- Date that data was made and was modified
- Descriptive tags

The more complete metadata from datasets generally means that the data is 'clean' and is better quality.


## Coordinates

### The shape of the Earth

- The Earth is an ellipsoid, or more importantly a spheroid.
- It bulges out at the equator so it isn't a perfect sphere.

### Geographical Coordinate Systems

- 3 dimensional model that identifies points on the earth.
- Latitude (**parallels**)
- Longitude (**meridians**)

> If a map only contains 2 spatial properties 1 of them will always be direction.


### Datum

- Is a frame of reference to define the position of the spheroid of the earth relative to the center of the datums position.

![Pasted image 20230907142357.png](../attachments/Pasted%20image%2020230907142357.png)


### Longitude and Latitude

- Angular unit of measure
- can use long and lat angles to describe where a point on the map is.

#### Graticule 

- The grid that is defined by the lines of latitude and longitude.

#### Recording Long/Lat Coordinate 

#### DMS notation - Degrees, Minutes, Seconds (°, ',")

This is based on a base 60 system and is an out dated but still used. Degrees is used instead of hours.

ex. 142° 32' 23" = 142 **degrees**, 32 **minutes**, 23 **seconds**. (1 degree = 60 minutes, 1 minute = 60 seconds.)

### DD notation - decimal based 

- Latitude and Longitudes are displayed in a decimal format:

-2.293756, 48.498675 

These are coordinates based on the quadrants of the meridian and equator:

![Pasted image 20230907182302.png](../attachments/Pasted%20image%2020230907182302.png)

based on this system, we would know that the above coordinates would belong somewhere in the top left quadrant.

#### Converting DMS - DD Coordinates

Add the degrees to the minutes, and divide by 60, then add the seconds and divide by 3600 to get the total.

| 121° | 8' | 6" |
| ---- | --- | --- |
| = D  | + (M/60) | + (S/3600) |
| = 121.135 |

#### Converting DD - DMS Coordinates

Basically just do the opposite.

```
121.135

.135 # Take the numbers after the decimal point.

.135 x 60 = 8.1 # the 8 is the minutes.

.1 x 60 = 6 # Take the last number after the decimal and multiply it by 60.

= 121, 8, 6

```


### Datums

Datums are used to specify an ellipsoids locations.

In North America there are two main **Datum Elements**:

- North American Datum 1927 (NAD 27)

NAD 27 uses the Clarke 1866 Ellipsoid.

- North American Datum 1986 (NAD 83)

NAD 86 uses the GRS 80 Ellipsoid.

### Geographic Coordinate System

Consists of:

- Angular unit of measure
- Prime meridian
- Datum that specifies an ellipsoid











