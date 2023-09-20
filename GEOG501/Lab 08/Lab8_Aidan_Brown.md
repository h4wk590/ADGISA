
# Aidan Brown
# GEOG 501


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
- **Bennet Clarkson Hospital** - 88,677 people served.
- **Saint Lukes Hospital** - 51,284 people served.
-  **Saint Ann Hospital** - 35,072 - people served.
- **Canton-Inwood Hospital** - 25,396 people served.

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






