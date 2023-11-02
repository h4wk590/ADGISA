
## Aidan Brown
## GEOG 511 Fall 2023


## Question 1

- SELECT COUNT(ASTERISK) from Orders
- 830 records

## Question 2

- SELECT AVG(UnitPrice) FROM Products
- 28,8663

## Question 3

- SELECT MAX(UnitPrice) FROM Products
- 263.50

## Question 4

- SELECT MAX(UnitPrice * 1.12) FROM Products
- 295.120000

## Question 5


- SELECT COUNT(*) FROM Customers
   WHERE City = 'London'
- 6

## Question 6

- SELECT SUM(UnitsInStock) FROM Products
  WHERE Discontinued = 1
- 101

## Question 7

- SELECT COUNT(*) FROM Orders
  WHERE OrderDate = '1998-01-13'
- 3

## Question 8

- SELECT COUNT(*) FROM Products
  WHERE UnitPrice < 10.00
- 11

## Question 9

- SELECT COUNT(*) FROM Products
  WHERE UnitPrice >= 50.00 AND UnitPrice <= 75.00
- 3

## Question 10

- SELECT COUNT(*) FROM Orders
  WHERE ShipCountry = 'Portugal'
- 13

## Question 11

- SELECT AVG(UnitPrice * 1.12) FROM Products
  WHERE Discontinued = 1
- 52.925600

## Question 12

- SELECT HomePhone FROM Employees
  WHERE FirstName = 'Robert' AND LastName = 'King'
- (71)555-5598

## Question 13

- SELECT COUNT(ASTERISK) FROM Products
  JOIN Categories ON Products.CategoryID = Categories.CategoryID
  WHERE Categories.CategoryName = 'Beverages'
- 12

## Question 14

- SELECT AVG(Products.UnitPrice) FROM Products
  JOIN Categories ON Products.CategoryID = Categories.CategoryID
  WHERE Categories.CategoryName = 'Beverages'
- 37.9791

## Question 15

- SELECT COUNT(*) FROM Orders
  JOIN Shippers ON Orders.ShipVia = Shippers.ShipperID
  WHERE Shippers.CompanyName = 'Speedy Express'
- 249


## Question 17

- SELECT Products.ProductName FROM Products
  JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
  WHERE Suppliers.CompanyName = 'Bigfoot Breweries'
-  Sasquatch Ale
- Steeleye Stout
- Laughing Lumberjack Lager

## Question 18

- SELECT MIN(Orders.OrderDate) FROM Orders
  JOIN [Order Details] ON Orders.OrderID = [Order Details].OrderID
  JOIN Products ON [Order Details].ProductID = Products.ProductID
  WHERE Products.ProductName = 'Sasquatch Ale'
- 1996-08-22 00:00:00.000

## Question 19

- SELECT COUNTRIES_2002.Shape.STArea() FROM sde.COUNTRIES_2002
  WHERE sde.COUNTRIES_2002.CNTRY_NAME = 'Finland'
- 335312871766.902 

## Question 20

- SELECT sde.COUNTRIES_2002.CNTRY_NAME FROM sde.COUNTRIES_2002, sde.CITIES
	WHERE sde.CITIES.CITY_NAME = 'Plzen' AND Cities.Shape.STIntersects(sde.COUNTRIES_2002.Shape) = 1
- Czech Republic

## Question 21

- SELECT COUNT(*) FROM sde.CITIES
  JOIN sde.COUNTRIES_2002 ON sde.Cities.CITY_NAME = sde.COUNTRIES_2002.CNTRY_NAME
  WHERE sde.COUNTRIES_2002.CNTRY_NAME = 'Germany'
  AND sde.Cities.POP_CLASS BETWEEN 100000 AND 250000








