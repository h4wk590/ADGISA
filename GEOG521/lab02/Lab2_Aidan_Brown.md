
## Aidan Brown
## GEOG 521 Fall 2023

## Deliverable 1

Deliverable 1: When running the Buffer tool, should you dissolve overlapping features or not? Does this matter for the final result? Briefly explain your answer.

Yes, it does matter, and I did choose to dissolve all features when using the buffer tool. When converting from a raster to polygon, the new polygon will have all cell values as individual parts of the polygon. In this case, for rivers, and roads should be displayed as continuous data.

## Deliverable 2

When running the Union tool, does the order of inputs matter? How would the result be different
if the order were altered?

Yes. If the feature classes that were buffered are put first in priority, they do not retain the buffer within the study area. They need to be the last priority in order to retain the clip to the study area when the union happens.

## Deliverable 3

When running a Union using an input that does not cover the entire study area (e.g. one of the
buffers), what are the attributes for the missing area in the result of the union (e.g. the area outside of the buffer but within the study area.

Below the screen capture shows the attribute values of the rivers buffer outside of the study area:

![Pasted image 20231011110636.png](../../attachments/Pasted%20image%2020231011110636.png)

## Deliverable 4

What SQL query did you perform to obtain the result?

gridcode = 1 And FID_study_area = 0 And FID_study_area_Clip = 1

## Deliverable 5

Screen capture of the final result. This should include only the following: 1) study area boundary
polygon with the symbology set to hollow (i.e. only showing the outline); and 2) the polygons representing the areas that meet all four criteria (regular fill, any color):

![Pasted image 20231011110841.png](../../attachments/Pasted%20image%2020231011110841.png)

## Deliverable 6: 

What % of the study area meets all four criteria? Report your result using one decimal

## Deliverable 7


What do the cell values of the distance grid represent? Carefully consider the type of number,
the units of the number and what the number represents. Briefly explain your answer.

After outputting the new boolean grid, any pixel outside of the specified 2500 or greater area from the rivers is a sum of all pixels using the reclassify tool, whereas the 0 boolean value pixels represents the sum of all pixel grids within the specific 0 to 2500 range of values.

## Deliverable 8

Which expression did you use in the Raster Calculator?

![Pasted image 20231012020232.png](../../attachments/Pasted%20image%2020231012020232.png)

## Deliverable 9

![Pasted image 20231012020348.png](../../attachments/Pasted%20image%2020231012020348.png)

## Deliverable 12

Conceptually, which vector tool is most similar to the Combine tool in raster? What are some
of the similarities and what are some of the differences?

- The **Union** tool seems like the vector version of the Combine tool for raster data. They both take multiple layers, and both output the relevant combined attribute data while still maintaining the integrity of the attributes. The most obvious difference is that the combine tool only works for raster data. Another difference is the fact that the combine tool deals with continuous data, like the data in this lab (elevation, area), while the union tool deals with discrete vector data like points, lines, and polygons.

## Deliverable 13

Rounding is applied up. Looking at the re-classified raster data and then back to the weighted overlay, any value in the re-classified data is rounded up to the next whole number (1.8 = 2 in the weighted overlay).

## Deliverable 14


| Suitability Category | Equal-weight Scenario Total Area KM2 | Alternative Scenario Total Area KM2 |
| ---------- | -------- | -------- | 
| 1 (Least Suited) | 4.658 KM2 | 12.126 KM2|
| 2 | 126.7058 KM2 | 110.023 KM2 |
| 3 | 67.683 KM2 | 69.188 |
| 4 | 2.014 KM2 | 11.643 |

