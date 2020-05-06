-- 2 Из таблицы salers выберите все города, состоящие из двух слов.
SELECT *
FROM salers
WHERE city
REGEXP " "

-- 3 Из таблицы salers получите все ряды, где имена продавцов и названия городов не превышают 6 символов
SELECT *
FROM salers
WHERE `sname`
REGEXP "^.{0,6}$" AND city REGEXP "^.{0,6}$"