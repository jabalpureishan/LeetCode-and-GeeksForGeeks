SELECT * 
FROM Users
WHERE mail LIKE '%@leetcode.com'
AND SUBSTRING(mail, 1, 1) REGEXP '^[A-Za-z]'
AND mail REGEXP '^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$';