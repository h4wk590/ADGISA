


# Spatial Data

## Scale

Unit scale matters to the size of the map versus the real world.

- Need to be able to make simple metric conversions
- unitless, 1 unit is equal to whatever the scale is ie: 1:250,000
- Will always be a 1 on the left hand side of the ratio.
- 1 dimension (linear) is captured.

### Representing Scale

- Absolute Fraction (1:500,000).
- Verbal Scale ("one inch to one mile").
- Bar scale - graphical scale

## Large vs Small Scale

- Smaller scale number = large scale map (1:5000) (large detailed)
- Large scale number = small scale map (1:300,000,000) (small detailed)

## Vector and Raster

- Vector data is discrete data that can be absolutely measured and labeled.
- Raster data is continuous data that measures continuous change gradually over a landscape.(elevation, rainfall, etc.)

### Vector

- Lines (sometimes called polylines)
- Points
- Polygons

Every feature will have a record in an attribute table.

#### Feature Class

Vector features are always managed by feature classes to associated features to an attribute table.
Feature class is a grouping of features, their coordinates, and the associated attributes ie:

- Features Class: City_Schools.
- Features: Points on a map to all city schools.
- Attribute table: associated point on the map to record in the table.

Feature class is the raw data, until it is added to a map. It then becomes a ***feature layer***.



### Raster

- Cells to be populated by continuous data.
- whole numbers and numbers with decimals.
- Single Attribute (cell value).
- Stores all details in the cell to database.

## File Formats




