-- View all records
SELECT * FROM business_data;

-- Total sales by region
SELECT region, SUM(sales) AS total_sales
FROM business_data
GROUP BY region;

-- Filter records with higher sales
SELECT *
FROM business_data
WHERE sales > 13000;
