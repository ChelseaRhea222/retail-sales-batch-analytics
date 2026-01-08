-- Staging view for retail sales dataset
-- Input table: raw_sales

DROP VIEW IF EXISTS stg_sales;

CREATE VIEW stg_sales AS
SELECT
  CAST(year AS INTEGER)  AS year,
  CAST(month AS INTEGER) AS month,

  -- Create a real month date like 2024-03-01
  date(printf('%04d-%02d-01', CAST(year AS INTEGER), CAST(month AS INTEGER))) AS month_date,

  TRIM(supplier)          AS supplier,
  TRIM(item_code)         AS item_code,
  TRIM(item_description)  AS item_description,
  TRIM(item_type)         AS item_type,

  -- Numeric measures (coerce to REAL)
  CAST(retail_sales AS REAL)      AS retail_sales,
  CAST(retail_transfers AS REAL)  AS retail_transfers,
  CAST(warehouse_sales AS REAL)   AS warehouse_sales,

  -- Helpful derived metrics
  (CAST(retail_sales AS REAL) + CAST(retail_transfers AS REAL) + CAST(warehouse_sales AS REAL)) AS total_movement
FROM raw_sales;
