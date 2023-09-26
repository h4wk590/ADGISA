
# Aidan Brown
# GEOG 501 Fall 2023


## Deliverable 1

How many tourist attractions are located in Custer County? Briefly explain how you obtained his
answer.

- 35 tourist attractions are located in Custer county.

I first used the Spatial join geo-processing tool, chose the **within** relationship. I then selected the **NAME**
Field (the names of the counties) by attribute to find all attributes named **Custer**. This displayed the resulting number of tourist attractions.


## Deliverable 2

- **Todd county** is the furthest county from a hospital at **176 KM** away.

I used the spatial join geo-processing tool. I used **counties** as the input feature and **hospital** as the join feature as we want to calculate the distance from the counties themselves. I used a one-to-one table join and used the **closest** match option to find the closest hospital and then sorted the attribute table by descending to find the highest value.

## Deliverable 3

Which five hospitals serve the largest number of people based on the results from the distance
spatial join? Report the names of these five hospitals and the number of people they serve. Briefly explain how you obtained your answer:

Five largest hospitals based off the distance results:

- **McKennan Hospital** - 144,713 people served.
- **Saint Ann Hospital** - 89,099 people served.
- **Bennett Clarkson Hospital** - 88,677 people served.
-  **Saint Joseph Hospital** - 73,862 people served.
- **Canton-Inwood Hospital** - 69,946 people served.

To get this data I first sorted the distance spatial join attributes from the previous deliverable in the population field to descending in order to get the most people per county. Then going to the hospital field to get the names of the top 5. two entries for Saint Luke's hospital were in the top 5 so I added both population fields together.


## Deliverable 4

The use of the distance spatial join between hospitals and counties makes several assumptions
about how people would travel to a hospital. Identify at least three of these assumptions.

- Time

Because some hospitals are so far away from some counties, people would have to allocated large amounts of time and planning ahead for regular appointments at the hospitals.

- Transportation

The distance between all these hospitals assumes people have valid means of transportation to get to and from these hospitals. If people don't have any means of transportation then they would have to use public transportation, but we can assume that that could take even longer than having their own means to travel.

- Hospital Services

Assuming that only a certain amount of hospitals are well equipped for certain medical examinations, surgeries, etc. 


## Deliverable 5



| Catchment | Name | Total Length of Stream (in km, rounded to one decimal.) |
| --------| ---- | ---------------| 
| 1 | Alder | 80.0 KM |
| 2 | Lower Big wall | 68.0 KM |
| 3 | Middle Big wall |49.0 KM |
| 4 | Swale | 44.0 KM |
| 5 | Upper Skookum | 68.0 KM |
| 6 | Upper Wilson |76.0 KM |


## Deliverable 6

| Catchment | Name | Total Area (in square km, rounded to one decimal) | 
| -------- | --------| --------------------------| ---------| ---------| -------- | ---------| -------- |
| | | Non-forest | Ponderosa Pine | Douglas Fir (mixed) | Douglas Fir (pure) | Oregon White Oak | Western Larch |
| 1. | Alder | 17.0 km2 | 14.1 km2 | 13.1 km2 | 0 km2 | 13.1 km2 | 33.3 km2 |
| 2. | Lower Big wall | 0 km2 | 5.0 km2 | 61.0 km2 | 0 km2 |  35.4 km2 |0 km2
| 3. | Middle Big wall | 0.5 km2 | 14.0 km2 | 0 km2 | 0 km2 | 0 km2 | 9.0 km2 |
| 4. | Swale | 0 km2 | 30.6 km2 | 10.0 km2 | 0 km2 | 3.0 km2 | 10.0 km2 | 
| 5. | Upper Skookum |12.0 km2 | 71.0 km2 | 0 km2 | 0 km2 | 7.0 km2 | 0 km2 |
| 6. | Upper Wilson | 1.0 km2 | 79.0 km2 | 6.0 km2 | 0 km2 | 0 km2 | 22.0 km2 |


## Deliverable 7

Describe how you carried out your analysis for Deliverable 6:

- Used the Intersect tool with the input values being the **forest** and **basins** feature classes.
- Created a new double numerical field in the new feature classes attribute table called **length_km2**.
- Used the **Calculate Geometry** tool on the empty field and specified the inputs to be the new feature class, using the current maps coordinate system, and selecting the **Area** option for units.
- Now that the values were in the correct units, I used the **Summarize** tool to put all individual values into a summarized field by the **SUBWAT_NAM** field.
- In the new exported summarized table I could **select by attribute** the subwat name and search within the attribute table to find the number code associated to the tree species.

## Deliverable 8

The buffer zone of 150 meters around the streams in the Wall Creek watershed is  4807.8 square km (one decimal)
in size and contains 23.8 % (one decimal) forest cover