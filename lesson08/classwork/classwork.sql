-- 1
SELECT sname, comm FROM salers;

 

-- 2
SELECT sname, comm*100 FROM salers;

 

-- 3
SELECT sname, comm*100, '%' FROM salers;

 

-- 4
SELECT * FROM orders ORDER BY onum;

 

-- 5
SELECT * FROM salers ORDER BY sname ASC;

 

-- 6
SELECT * FROM salers ORDER BY sname DESC;

 

-- 7
SELECT snum, amt, odate FROM orders ORDER BY snum, amt;

 

-- 8
SELECT snum, amt, odate FROM orders ORDER BY snum DESC, amt DESC;

 

-- 9
SELECT snum, MAX(amt), odate FROM orders GROUP BY snum;

 

-- 10
SELECT snum, odate, MAX(amt) FROM orders GROUP BY snum ORDER BY 3;

 

-- 11
SELECT * FROM salers LIMIT 2;

 

-- 12
SELECT * FROM salers LIMIT 0, 2;

 

-- 13
SELECT * FROM salers ORDER BY snum DESC LIMIT 1;

 

-- 14
SELECT sname, cname FROM salers, customers;

 

-- 15
SELECT salers.sname, customers.cname, salers.city FROM salers, customers;

 

-- 16
SELECT salers.sname, customers.cname, salers.city FROM salers, customers WHERE salers.snum = customers.snum;

 

-- 17
SELECT salers.sname, customers.cname, salers.city FROM salers, customers WHERE salers.snum = customers.snum ORDER BY salers.sname;

 

-- 18
SELECT s.sname, c.cname, s.city FROM salers s, customers c WHERE s.snum = c.snum ORDER BY s.sname;
