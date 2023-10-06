
## Aidan Brown
## GEOG 521 Fall 2023


## Part A: Snail Habitat Analysis


## Deliverable 1

Is this grid an integer or floating point grid? And what does the count field indicate?

- The new grid is an integer grid. The count field represents all cells of the converted feature classes.

## Deliverable 2

What is the total area of the Madison Limestone (unit 7) in the new grid? Briefly explain how you
obtained your answer.

- 56951 M2

	I got the above answer by first selecting only Madison Limestone by the count attribute, going into the symbology of the **Limegrid** raster, changing the **Primary symbology** to **classify**, normalizing the data by **count**, going to the **more** option and there was where I found the total count.


## Deliverable 3

I used **Raster Calculator** with the inputs as:

elevation >= 1200 & <=1600, Conifers == 1, Limegrid == 1.

Because Conifers and Limegrid are both Boolean values, any potential snail habitat should theoretically be within the elevation range where each of these conditions is true.

## Deliverable 4

![Pasted image 20231005135527.png](../../attachments/Pasted%20image%2020231005135527.png)



