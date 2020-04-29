-- 1
SELECT * FROM orders;

 

-- 2 
SELECT onum, amt, odate, cnum, snum FROM orders;

 

-- 3
SELECT amt, odate FROM orders;

 

-- 4
SELECT DISTINCT odate FROM orders;

 

-- 5 
SELECT odate, amt FROM orders WHERE odate = '1990-04-10';

 

-- 6 
SET NAMES cp866;

 

-- Реляционные операторы или операторы сравнения
-- "=" равенство
-- ">" больше чем
-- "<" меньше чем
-- ">=" больше или равно
-- "<=" меньше или равно
-- "<>", "!=" неравенство

 

-- 7
SELECT amt FROM orders WHERE amt > 1000;

 

-- 8
SELECT sname, city FROM salers WHERE city <> 'London';

 

-- 9
SELECT sname, city FROM salers WHERE sname > 'Motika';

 

-- 0123ABCD...Zabcd...zА-Яа-я
-- A < D, A > 3, R < Rifkin
--- 3 > 2

 

-- 10
SELECT * FROM orders WHERE odate > '1990-04-10';

 

-- AND (И), OR (ИЛИ), NOT (НЕ)

 

-- 11
SELECT * FROM orders WHERE amt > 1000 AND odate = '1990-06-10';

 

-- 12
SELECT amt FROM orders WHERE amt > 1000 AND amt < 4000;

 

-- 13
SELECT * FROM salers WHERE city = 'London' AND comm > 0.11;

 

-- 14
SELECT * FROM salers WHERE city = 'London' OR comm > 0.11;

 

-- 15
SELECT * FROM customers WHERE NOT city = 'London';

 

-- 16
SELECT * FROM  orders 
        WHERE NOT ((odate = '1990-03-10' AND snum > 1002) OR amt > 2000.00);
-- инвертированный результат 3003, 3009, 3007, 3010
-- результат без инверсии (без учета NOT) 3001, 3002, 3006, 3005, 3008, 3011


-------------------------------------------------------------------------------

-- 1
SELECT sname, city FROM salers WHERE city = 'London' OR city = 'New York';

 

-- 2
SELECT sname, city FROM salers WHERE city IN ('London', 'New York', 'Barcelona');

 

-- 3
SELECT * FROM salers WHERE comm IN (0.11, 0.12, 0.13, 0.15);

 

-- 4
SELECT * FROM salers WHERE comm BETWEEN 0.11 AND 0.15;

 

-- 5
SELECT * FROM salers WHERE (comm BETWEEN 0.11 AND 0.15) AND comm NOT IN (0.11, 0.15);

 

-- 6
SELECT sname FROM salers WHERE sname BETWEEN 'A' AND 'N';

 

-- 7
SELECT * FROM salers WHERE sname IS NULL;

 

-- 8
SELECT sname FROM salers WHERE sname IS NOT NULL;

 

-- 9  "%" - любое кол-во любых символов
SELECT * FROM salers WHERE sname LIKE 'Mot%';

 

-- 10
SELECT * FROM salers WHERE sname LIKE '%kin';

 

-- 11  "_" - 1 любой символ
SELECT * FROM salers WHERE sname LIKE 'P__l';

 

-- 12
SELECT * FROM salers WHERE sname LIKE '\_';

 

-- 13
SELECT * FROM salers WHERE sname LIKE '\%';

 

-- 14
SELECT * FROM salers WHERE sname = "d\'Artanian";

 

-- 15
SELECT * FROM salers WHERE sname LIKE '%fk%';

 

-- 16
SELECT * FROM salers WHERE sname NOT LIKE '%fk%';

---------------------------------------------------

-- COUNT(), SUM(), AVG(), MIN(), MAX() || GROUP BY, HAVING

 

-- 1 
SELECT COUNT(sname) FROM salers;

 

-- 2 
SELECT COUNT(city) FROM salers;

 

-- 3
SELECT COUNT(*) FROM salers;

 

-- 4
SELECT COUNT(DISTINCT city) FROM salers;

 

-- 5
SELECT COUNT(*) AS res FROM salers;

 

-- 6
SELECT SUM(amt) AS res FROM orders;

 

-- 7
SELECT AVG(amt) AS res FROM orders;

 

-- 8
SELECT MIN(amt) AS res FROM orders;

 

-- 9
SELECT MAX(amt) AS res FROM orders;

 

-- 10
SELECT MIN(sname) FROM salers;

 

-- 11
SELECT MAX(sname) FROM salers;

 

-- 12
SELECT snum, MAX(amt) FROM orders WHERE snum = 1007;

 

-- 13
SELECT snum, MAX(amt) FROM orders GROUP BY snum;

 

-- 14
SELECT snum, MAX(amt) AS res FROM orders GROUP BY snum HAVING res > 2000;

 

-- 15
SELECT snum, MAX(amt) FROM orders GROUP BY snum HAVING COUNT(snum) > 2;
