-- 1 Получите идентификаторы имена и города клиентов/продавцов из Лондона
    SELECT sname as name, city
    FROM salers
    WHERE city = 'London'
UNION
    SELECT cname, city
    FROM customers
    WHERE city = 'London'

-- 2 Используя оператор EXISTS получите идентификаторы и имена продавцов, имеющих продажи с суммой более 2000
SELECT snum, sname
FROM salers
WHERE EXISTS(
SELECT *
FROM orders
WHERE salers.snum = orders.snum AND orders.amt>2000
)