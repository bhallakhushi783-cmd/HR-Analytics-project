SELECT * FROM employees;

SELECT Attrition, COUNT(*) 
FROM employees 
GROUP BY Attrition;

SELECT Department, Attrition, COUNT(*) 
FROM employees 
GROUP BY Department, Attrition;

SELECT Attrition, AVG(Salary) 
FROM employees 
GROUP BY Attrition;

SELECT Department, AVG(Salary) 
FROM employees 
GROUP BY Department;