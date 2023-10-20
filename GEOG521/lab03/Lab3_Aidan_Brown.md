
## Aidan Brown
## GEOG 521 Fall 2023

## Deliverable 1

- Cell values are larger numbers when father away from the data source as the source point was the input data source when performing analysis using the **Distance Accumulation** tool. To conclude this, I viewed the attribute information of individual cell values around the **source** data point, and the **destination** data point.

## Deliverable 2

Carefully examine the back direction raster. What do the cell values represent? What are the
units, if any? Why is this raster needed for further analysis?

- Each cell value represents the angle of the slopes elevation in degrees. The data has been classified categorize the pixel values by compass direction.

## Deliverable 3

Brief description of your analysis steps (only for the step to determine the locations of the
crossings).

- Using the **Intersect** tool I was able to perform the analysis to determine where the least-cost path crosses the river, by specifying the inputs as the optimal distance raster intersected with the **river.shp.**

## Deliverable 4

How many river crossings are there for the least-cost path solution for scenario 1?

- 9 total river crossings.

## Deliverable 5

![Pasted image 20231012144744.png](../../attachments/Pasted%20image%2020231012144744.png)

## Deliverable 6

How many river crossings are there for the least-cost path solution for scenario 2?

- 2 River crossings in scenario 2.

## Deliverable 7

![Pasted image 20231019093900.png](../../attachments/Pasted%20image%2020231019093900.png)

## Deliverable 8

- 1 river crossing for scenario 3
## Deliverable 9

![Pasted image 20231019094830.png](../../attachments/Pasted%20image%2020231019094830.png)

## Deliverable 10

![Pasted image 20231019103042.png](../../attachments/Pasted%20image%2020231019103042.png)

## Deliverable 12


Brief description of your analysis steps for your corridor analysis.


- Used the **re-classify** tool to input the suitability values as stated in the assignment.
- Used the **Weighted Overlay** tool to combine all new suitability raster.
- Used the **Polygon to Raster** tool to convert both park polygons to raster.
- Used **Raster Calculator** tool with the input 11 - "WeightedOverlayRaster" to invert results.
- Created a cost surface using the **Distance Accumulation** tool. I used the weighted overlay as the input source.
- Created two **Distance Accumulation** raster's with both converted Park raster's, specifying the cost surface as the one created as above.
- From there I created corridor using both cost accumulation raster's as inputs.

## Deliverable 13

![Pasted image 20231019142314.png](../../attachments/Pasted%20image%2020231019142314.png)

## Deliverable 14

Consider the factors that were used in the analysis. Can you think of other factors to consider
when trying to model the best corridors to connect the two protected area? Briefly justify each factor.

- **Water/Rivers**

Rivers can be a barrier for different wildlife species as some species won't cross a rapid river. While rivers also act as a source of water, or movement for a lot of different species. Rivers could effect the populations of some species hence why a corridor would support this claim.

