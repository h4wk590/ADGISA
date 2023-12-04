
## Aidan Brown
## GEOG 521 Fall 2023


## Deliverable 1

![Pasted image 20231122203653.png](../../attachments/Pasted%20image%2020231122203653.png)

## Deliverable 2

![Pasted image 20231122215251.png](../../attachments/Pasted%20image%2020231122215251.png)

## Deliverable 3

![Pasted image 20231123085008.png](../../attachments/Pasted%20image%2020231123085008.png)

## Deliverable 4

- **Lower Bound Estimate** - Using a **select by location** with the fl_blockgroups as the input and manatee_basin as the selecting features, and choosing the "Have their center in" Relationship to estimate the minimum population. This estimated population count came to: **103,831**.
- **Upper Bound Estimate** - Using Select by location with fl_blockgroups as input, and manatee_basin as the selecting features, but choosing the "Within a distance" relationship of 2 KM to include the polygons in and around manatee_basin. This estimated population count came to: **228,572**.
- **Intermediate Estimate** - Using the Select by location tool again, and selecting the intersect relationship to define the intermediate population count: **155,969**.

## Deliverable 5

- After performing the clip and viewing statistics, the population count came to the same result as the **Intermediate Estimate** option (Select By Attribute intersect relationship): **155,969**.

## Deliverable 6

- After performing ariel weighting, the estimated population is: **106,040**.

## Deliverable 7

- Results from ariel weighting are close to that of the previous estimates because of the boundary adjustment that ariel weighting achieved, apposed to the spatial query, where the boundary was chosen based on the intersection between the polygons (boundaries are not adjusted and the population is considered to be within the basin polygon).

## Deliverable 11

- Minimum precipitation: 150.3 mm
- Maximum precipitation: 6711.7 mm
- Mean precipitation: 1126.3 mm

- Used the Zonal statistics as Table tool with the Counties as the input zone data, with the STATE_NAME field as the zone field, and the Precipitation raster as the input value. This output a new table containing the values of MIN, MAX, and MEAN.
## Deliverable 12


- Jefferson county has the highest average (MEAN) precipitation at 2966.7 mm.

## Deliverable 13

- It is meaningful in this case as it greatly reveals how certain elevation zones differ from land cover types. It wouldn't be as meaningful however, if the elevation did not have much significance or in common with the land cover dataset. In short, it greatly depends on the data being used to when a DEM is a meaningful choice as a zonal statistic dataset.

## Deliverable 14

- Vector or raster layers can technically be used as a zone dataset. The context and the data surrounding the zone datasets is what needs to be taken into consideration. For example, scale and the spatial resolution should be consistent across all layers, or when using a vector layer, it should have well defined boundaries or a study area. 

## Deliverable 16

- The created map represents land cover variety in tree species within a cell, so in each cell the focal statistics tool calculated the variance of the input data based on the 3x3 cell grid. Ecologically/biologically this information can provide some insights on types of species and their growth patterns, for example, areas of land with larger amounts of variety could represent lusher areas, or multiple different co-habitant ecosystems, whereas areas with low land variety would indicate that the areas are more human disturbed.

## Deliverable 17


- **Boundary Clean** - No noticeable difference when changes the options to sort from ascending or descending. Boundary did seem to generalize smaller smaller regions quite effectively.
- **Expand** - Expand did not do a great job at generalizing smaller regions, trying different cell values only seemed to skew it further (tried 1, 5, 20 cell sizes), and increasing the value count.
- **Majority Filter** - Generalized most smaller contiguous areas fairly well, in fact this tool in my eyes does the best job out of the bunch at visualizing the generalization. Although it still left out small white areas near the bottom.
- **Shrink** - Smaller values are fairly distinguishable on the map.
- **Thin** - In the most absolute way, it did indeed generalize the majority of values, so much so that it basically consumed the whole map. 



## Deliverable 18

Boundary:

![Pasted image 20231123152326.png](../../attachments/Pasted%20image%2020231123152326.png)

Expand:

![Pasted image 20231123152542.png](../../attachments/Pasted%20image%2020231123152542.png)

## Majority Filter:

![Pasted image 20231123153041.png](../../attachments/Pasted%20image%2020231123153041.png)

Shrink:
![Pasted image 20231123153905.png](../../attachments/Pasted%20image%2020231123153905.png)

Thin:

![Pasted image 20231123154250.png](../../attachments/Pasted%20image%2020231123154250.png)