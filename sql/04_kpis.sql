-- KPI queries for Retail Sales (monthly dataset)
-- Uses stg_sales view

-- 1) Overall totals
SELECT
  'overall_totals' AS section,
  SUM(retail_sales)      AS total_retail_sales,
  SUM(retail_transfers)  AS total_retail_transfers,
  SUM(warehouse_sales)   AS total_warehouse_sales,
  SUM(total_movement)    AS total_movement
FROM stg_sales;

-- 2) Trend by month
SELECT
  month_date,
  SUM(retail_sales)     AS retail_sales,
  SUM(retail_transfers) AS retail_transfers,
  SUM(warehouse_sales)  AS warehouse_sales,
  SUM(total_movement)   AS total_movement
FROM stg_sales
GROUP BY month_date
ORDER BY month_date;

-- 3) Top 10 items by retail sales
SELECT
  item_code,
  item_description,
  SUM(retail_sales) AS retail_sales
FROM stg_sales
GROUP BY item_code, item_description
ORDER BY retail_sales DESC
LIMIT 10;

-- 4) Item type performance
SELECT
  item_type,
  SUM(retail_sales)     AS retail_sales,
  SUM(warehouse_sales)  AS warehouse_sales,
  SUM(total_movement)   AS total_movement
FROM stg_sales
GROUP BY item_type
ORDER BY total_movement DESC;

-- 5) Top 10 suppliers by total movement
SELECT
  supplier,
  SUM(total_movement) AS total_movement
FROM stg_sales
GROUP BY supplier
ORDER BY total_movement DESC
LIMIT 10;
