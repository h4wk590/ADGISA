
## Aidan Brown
## GEOG 521 Fall 2023


## Deliverable 1

- The cell values indicate the visibility of each location, for example cell value of 1 would indicate that one location is visible from one of the observation points, etc.

## Deliverable 2

- Displaying the chart based on count of each of the 3 towers:

SUM - MAX / SUM 

229,508 - 185,196 / 229,508 x 100

= **19.3%**

## Deliverable 3

![Pasted image 20231108110644.png](../../attachments/Pasted%20image%2020231108110644.png)

## Deliverable 4

- The cell values depict visibility from each observer point. A value of 1 tells us that the point is visible from 1 other observer point.
## Deliverable 5

- Created a new viewshed using all of the summits.
- Used <i>Extract Values to Points</i> tool with all Summits as the input, and The newly created viewshed as the input raster.
- Examined resulting features attribute table with new RASTERVALUE field for results.

## Deliverable 6

- **Bear Den Mountain** is the most visible, from 9 total summits.

## Deliverable 7

- Anchor Hill
- Bear Den Mountain
- Crook Mountain 
- Itself
- Pillar Peak
- Whitewood Peak

## Deliverable 8

- Calculated the number of none visible cells by summarizing the statistics of the new visibility raster within the park boundary:

Number of cells not visible = 486,571 / 685,311 (total number of cells) x 100

= **71%** of the park cannot be seen from the road.

## Deliverable 9

- When the observer point is a polyline, visibility values are assigned to each part of the polyline based on whether they have line of sight to other cells.

## Deliverable 10


![Pasted image 20231110004121.png](../../attachments/Pasted%20image%2020231110004121.png)

## Deliverable 12

![Pasted image 20231110013737.png](../../attachments/Pasted%20image%2020231110013737.png)

## Deliverable 13

- The initial camera didn't quite cover the full street, so I added another camera on the street behind at a 90 degree angle to capture the remaining coverage. The second camera was added just before the finish line at a 30 degree angle. This is so it could capture runners coming in right before finish, which beyond the aesthetic purposes could provide more useful data, for example; speed performance of the runners crossing the finish line.
## Deliverable 14

![Pasted image 20231110020524.png](../../attachments/Pasted%20image%2020231110020524.png)

## Deliverable 15


- There are 225 sight lines because there are 15 total summit points. Each summit point has a LOS for each other, 15 summit points x 15 lines of sight is 225 sight lines.

## Deliverable 16

![Pasted image 20231110012707.png](../../attachments/Pasted%20image%2020231110012707.png)

## Deliverable 16

![Pasted image 20231110021301.png](../../attachments/Pasted%20image%2020231110021301.png)

## Deliverable 17


- Based on my selected line of sight and the elevation the obstruction points I initially thought there would be an even larger number of obstructions, based on comparing the first two parts of the graph screen capture below:

![Pasted image 20231110021930.png](../../attachments/Pasted%20image%2020231110021930.png)
- Profile Graph

![Pasted image 20231110021951.png](Pasted%20image%2020231110021951.png)
- LOS Graph

But I understand that the observer point is sitting at a higher elevation, so it does make sense that the LOS graph displays these obstructions. When the elevation height is greater than that of the observer it would obscure vision.

## Deliverable 18

- **15** total records in the attribute table.
- **OID** is the unique field for each object.
- **Shape** is the geometric shape of the line.
- **SourceOID** is the source of the LOS (in this case it's Pillar Peak).
- **VisCode** is the status of visibility if it is obstructed or not
- **TarIsVis** is a Boolean value of 0 or 1 of the targets visibility.
- **OBSTR_MPID** Identifies features of obstruction.
- **Shape_Length** - Length of the lines.













