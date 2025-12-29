SELECT * FROM business_data;

SELECT region, SUM(sales) AS total_sales
FROM business_data
GROUP BY region;

SELECT category, AVG(sales) AS avg_sales
FROM business_data
GROUP BY category;

SELECT *
FROM business_data
WHERE sales > 13000;
