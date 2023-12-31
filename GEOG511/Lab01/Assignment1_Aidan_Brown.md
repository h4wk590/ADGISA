
## Aidan Brown
## GEOG 511 Fall 2023


## Part A

1.  Give an example of an object class, other than those used in the lecture.

| **Product** |
| ----- |
| Product_ID |
| Product_Name |
| Price |
| Quantity |


2.  Using the above answer, give an example of an instance within this class.

| **Paper Towel** |
| ---------- |
| Product_ID: 1 |
| Product_Name: Paper Towel |
| Price: $5.99 |
| Quantity: 1 |


3.  Using this answer again, what is an example of an attribute for this class?

- **Product_Name** is an attribute in this class that specifies the name of the product associated with the Product_ID.


4.  Describe or sketch an example of an Inheritance relationship, not already discussed in class.

- A **car** is the parent and **engine**, **wheels**, **breaks**, would all be examples of the inheritance relationship or the child tables.


5.   Describe or sketch an example of a Composition relationship, not already discussed in class.

![Pasted image 20230927110617.png](../../attachments/Pasted%20image%2020230927110617.png)


6.  Sketch a Class Diagram for the classes DEPARTMENT and EMPLOYEE, which have a 1:M relationship.  Assume a department can have zero employees and that every employee must be in a department.  Include classes and the multiplicity of the relationship. No attributes are necessary for this question.

![Pasted image 20230927111917.png](../../attachments/Pasted%20image%2020230927111917.png)

7. Construct a Class Diagram for a car-insurance company that has a set of customers, each of whom owns one or more cars. Each car has associated with it zero or more recorded accidents. Use the classes ACCIDENT, CAR and CUSTOMER. No attributes are necessary for this question.

![Pasted image 20230927121809.png](../../attachments/Pasted%20image%2020230927121809.png)

- A Customer can have multiple cars, or have zero.
- Cars can be involved in multiple accidents, or none at all.
- Individual cars are owned by 1 customer.

## PART B


8.  Construct a Class Diagram for the relationship between Continents and Countries, adding at least two attributes to the diagram. Document any assumptions which governed your mode.

![Pasted image 20231003121817.png](../../attachments/Pasted%20image%2020231003121817.png)

- Each country and each continent have a name, therefore a relationship
- Each country and each continent also have boundaries(borders), each country has to have a boundary, and each continent can have a boundary.


9.  Create a Class Diagram for a database to schedule classrooms for final exams, including object classes, attributes, associations and multiplicity. State any assumptions which guided your design.

![Pasted image 20231003143847.png](../../attachments/Pasted%20image%2020231003143847.png)

- The exam table is the focal point for this database design.
- It needs the course that will be taken, as well as what room the exam will take place.
- There can only be one exam per course, but there is multiple courses that have exams.
- There can be multiple rooms for exams, but only 1 exam per room.

10. 10. Design a database which could allow us to examine issues relating to health and employment. Such a database is central to understanding how and why employment and health problems are different for women and men.

![Pasted image 20231003150927.png](../../attachments/Pasted%20image%2020231003150927.png)

People can have many jobs over time, and can have many health problems. There are also many health problems that a person could have so I chose to use many to many for both **Health Problems** and **Jobs** I created a new table called **Health Record** to store the health problem issue, and the persons name for the record. I added a new attribute called **Province** within the **People** table to store the current province that they are living in.
 
11. 

![Pasted image 20231003152655.png](../../attachments/Pasted%20image%2020231003152655.png)


- **Park** is one to many with Facilities as 1 park can have many facilities within it.
- There can be many staff performing maintenance on many facilities.
- There can be many staff per park, but 1 park for many staff.








