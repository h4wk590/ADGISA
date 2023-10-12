
## Aidan Brown
## GEOG 511 Fall 2023

1. Give an example of two attributes that have a functional dependency not discussed in class.

- **Social Security Number** and **Person's Name.** 

A Person's name has a functional dependency with a social security number, as a SIN number is unique to each person.

2.  Give an example of two attributes that do not have a functional dependency not discussed in class

- **Name** and **Favourite Meal**.

People can have the same name, but can have different favourite meals, therefore do not have a functional dependency on each other.

3. True
4. False
5. True
6. False
7. False

8. Given the dependencies you indicated are True above, what is the key of the PROJECT relation?

A and B are the keys for the PROJECT table, as each can determine all other attributes. PROJECTID can determine EmployeeName, and EmployeeSalary, and EmployeeName can determine ProjectID and EmployeeSalary.


9. B
10. B
11. B
12. AC
13. A

14. True - Each description is unique to a part number
15. False - There are multiple suppliers for a single part number.
16. False - There are multiple supplier addresses for a single part number.
17. False - The part number has multiple prices depending on the location.
18. True - Each description is unique to the supplier.
19. False - PartNumber does not determine all other attributes.


 21. In a relation R(A, B, C) with functional dependencies and keys:  AB --> C  Key: AB  What normal form is this relation in, and why?

- It passes 1NF as it has a relation.
- C is functionally dependent on the AB key so it also passes 2NF
- C does have a transitive relationship so it passes 3NF
- Fails BCNF because B is not a candidate key.

= 3NF








