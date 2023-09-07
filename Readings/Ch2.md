
## Data in GIS

- Data depends on the use case and is subjective by the GIS developer/analyst.
- Can be used to Represent a simplistic view of physical locations and objects.
- Using polygons instead of satellite imagery increases system performance.


## Spatial Data Model

Also referred to as **thematic layers**

- Spatial database containing objects and (most of the time) sets of layers to describe the data presented.
- Provides GIS-level abstraction from the real world, which is then converted to data structures and binary data to be read at a computational level.

Example Spatial Data model (**thematic layers**) could be:

- Soils data layer - Includes only soil data.
- Population data layer - Includes information about population.
- Elevation data layer - Elevated zones that will be presented on a map.
- Roads data layer - Only roads will be presented in this layer.



## Attribute Data and Types


Attribute data are just **variables** or **items** that are:

- Often Stored in a table.
- Columns associate the attribute.
- rows associate the spatial object.

Attribute tables are managed and organized using a Database Management System (**DBMS**). 

Attributes are used to describe features or *characteristics* of a spatial object.
For example, a fire hydrant could have the following attributes:

- Colour.
- number of hose connections.
- water pressure rating.

These are all attributes that can be used within the attribute table to associate the different fire hydrant objects on a map.

### Nominal Attributes

The ***Colour*** attribute from the fire hydrant is also a ***nominal attribute***. This is because it's descriptive information about the object. Other examples of ***nominal attributes*** could be:

- City names.
- Owner of a package.
- Soil series.
- Tree species.
- Images/film clips - mostly referred to as  '**BLOBS**' (Binary Large Objects).
- Audio recordings - Also considered as a '**BLOB**'.


### Ordinal Attributes

An ordinal attribute is an attribute that has a ranking such as:

- Ranking high to low values.
- Scale from 1 to 10

Ordinal attributes are a ranking of values only, and does not imply scale.


### Interval/Ratio Attributes

Interval/Ratio attributes refer to attributes that have scale and rank represented.

The items have a ***domain*** (range of values) they are able to take. For example:

- The fire hydrant could be restricted to certain colours of red, orange, yellow, green.


## Common Spatial Data Models


The two common types of data models for digital spatial data are **Vector** and **Raster** data models.


### Vector 

This is the data model used to define discrete objects as **lines**, **points**, and **polygons**. It uses sets of coordinates and attribute table data to define objects on a map.

- **Points** can be used to represent small objects on a map, or a large object like a city if the maps scale is large enough.
- **Lines** are often used to represent linear objects like, roads, and rivers.
- **Polygons** are used for large objects in an area (think buildings).

#### Some Vector Terminology


- **Nodes** are used to define the start and end points of a line.
- **Vertices** are used to define the points in between a line.

### Raster

A raster data model uses the entire canvas of equally sized cells to reference continuous change in data. For example:

- Elevation of an area over time.
- Rainfall percentage.
- Ozone Exposure.
- Growth stages of trees.

Usually a raster data model is used when representing maps of vegetations, or political units.

### Raster Data Models

- Cell location formula:

![Pasted image 20230906224520.png](../attachments/Pasted%20image%2020230906224520.png)

### Single-Part & Multi-Part Features

This image with figure makes more sense than I can explain. It's a whole page for this diagram so I consider it important..

![Pasted image 20230906220347.png](../attachments/Pasted%20image%2020230906220347.png)

Figure 2-23: Example of multi-part and single-part features. Here, counties for Rhode Island, a state in the Eastern U.S.A., are shown with one table entry for each county (top), with multi-part features in a layer, and with one table entry for each distinct polygon (bottom), with only single-part features in the layer. Note that calculations, analysis, and interpretation may differ for multi-part vs.. single-part features.

