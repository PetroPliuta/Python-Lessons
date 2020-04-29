-- 1. Напишите запрос, который выберет все ряды из таблицы заказов (orders) за март-апрель
SELECT * FROM orders WHERE odate BETWEEN "1990-03-00" AND "1990-05-00";

-- 2. Выберите всех клиентов (таблица customers) продавцов Peel и Motika.
select * from customers where snum in (1001, 1004);

-- 3. Составьте запрос, который выведет всех клиентов, чьи имена находятся в диапазоне A-G включительно.
select * from customers WHERE cname BETWEEN "A" AND "H";

-- 4. Выберите всех представителей, чьи имена начинаются с латинской литеры "C".
SELECT * FROM `customers` WHERE cname like "C%";

-- 5. Выберите всех представителей, чьи имена начинаются на латинскую литеру "D" и при этом заканчиваются на латинскую литеру "n". 
-- Выборка проведите 2-мя различными способами (2 различных запроса, дающих одинаковый результат).
SELECT * FROM salers WHERE sname like "D%" and sname like "%n";
SELECT * FROM salers WHERE sname like "D%n";

-- 6. Выберите всех представителей, чьи имена заканчиваются на латинскую литеру "n", но при этом не начинаются на латинскую литеру "D".
SELECT * FROM customers WHERE cname like "%n" and not cname like "D%";

-- 7. Выберите все ряды с NULL-значениями из таблицы продавцов
SELECT * FROM salers where sname is NULL or city is NULL or comm is NULL;
