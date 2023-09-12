
## Coordinate Systems 

- A way to reference where we are to the world relevant to a point on the Earth.
- Light on the math
- Heavy on concepts

## Why?

- Without a coordinate system it isn't really GIS.
- No decimal degrees on a scaled map as it's a measurement for angles, not distance.

## From 3D Globe to 2D Map

- approximating the surface of the earth.
- projecting the 3D object to 2D

## Shape of the Earth

- The earth is a spheroid because a spinning mass compresses slightly out at it's equator.

## Ellipsoidal Earth

- Geoid - mean sea level (approximating the sea as if it were a flat surface.)

It isn't a perfect measurement, but using an ellipsoid we can more accurately describe and measure the surface of the Earth.

## Geoid vs. Ellipsoid 

- Ellipsoids are region based. 
- There are efforts to set a standard Ellipsoid for the global level but region based ellipsoids are still used.
- Earth's surface is very complex and is not a perfect shape. Therefore the Geoid is an approximated measurement to take into account Earth's changes topography.

## Geodetic Datum

- Is a datum for the world
- A specific ellipsoid and a point of origin (center of the world or the surface of the world.)
- Typically no more than two numbers.

## North American Datums


- NAD 27 - Great for it's time.
- NAD 83 - Most widely used.
- WGS 1984 - GPS data uses this datum.


## Earth Coordinate Geometry

"How do we know where we are in the world with coordinates?"

### Coordinate System

- Spherical Coordinate System - coordinates describe locations on the world (lat, long).
- Planar Coordinate System - Need a projection for two dimensional objects.

## Coordinate System vs Projection

- Planer must have a projection
- geometric = coordinate system

## Types of projections

- Projection family - shape of the developable surface.
- Projection Properties - nature of distortions created.

### Projection Families

- Cylindrical Projection.
- Conical Projection surface.
- Planar projection surface.

### Projections and Distortions

Projections will distort one or more of the following map properties:

- Shape
- Area
- Distance
- Direction

- No projections preserves all properties

## Commonly Used Coordinate Systems

- **Albers Equal Area-Conic** - 2 standard parallels, typically scales at 1:8,000,000
- **Lambert Conformal Conic** - Conformal, but not equal area, used for continental USA or Canada
- **Transverse Mercator** - Transverse cylindrical projection, conformal, and shapes and angles within any small area are essentially true. 1:24,000 to 1:250,000

## UTM - Universal Transverse Mercator System

- Universal, works across the globe.
- Uses Meters as units of measurement.
- Consists of 60 zones.
- Only used between 84 north and 80 south
- Each zone has a central meridian which acts as the longitude of origin.
- Useful for small areas.
- Widely used to topographic maps and satellite images.

## Choosing a projection

- Knowing the use case - geometric features
- Where in the world?
- Orientation. Some countries are longer than other.
- How large is it? - Does it fit within the zone of interest?





