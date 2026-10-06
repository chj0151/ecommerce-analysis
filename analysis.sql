-- ============================================
-- 电商销售数据分析 SQL 脚本
-- 数据源：sales 表（5万行）
-- 作者：chj
-- 日期：2026-10-6
-- ============================================

USE ecomerece_db;

-- 1. 总订单数和总销售额
SELECT 
    COUNT(*) AS 订单数,
    ROUND(SUM(amount), 2) AS 总销售额
FROM sales;

-- 2. 按类别看销售额
SELECT 
    category AS 类别,
    COUNT(*) AS 订单数,
    ROUND(SUM(amount), 2) AS 销售额
FROM sales
GROUP BY category
ORDER BY 销售额 DESC;

-- 3. 按地区看销售额
SELECT 
    region AS 地区,
    COUNT(*) AS 订单数,
    ROUND(SUM(amount), 2) AS 销售额
FROM sales
GROUP BY region
ORDER BY 销售额 DESC;

-- 4. 按渠道看销售额和客单价
SELECT 
    channel AS 渠道,
    COUNT(*) AS 订单数,
    ROUND(SUM(amount), 2) AS 销售额,
    ROUND(AVG(amount), 2) AS 客单价
FROM sales
GROUP BY channel
ORDER BY 销售额 DESC;

-- 5. Top 10 热销商品（按销量）
SELECT 
    product_name AS 商品,
    category AS 类别,
    SUM(quantity) AS 总销量,
    ROUND(SUM(amount), 2) AS 销售额
FROM sales
GROUP BY product_name, category
ORDER BY 总销量 DESC
LIMIT 10;

-- 6. 月度销售趋势
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS 月份,
    COUNT(*) AS 订单数,
    ROUND(SUM(amount), 2) AS 销售额
FROM sales
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY 月份;

-- 7. 复购分析（CTE 版）
WITH user_order_cnt AS (
    SELECT user_id, COUNT(*) AS 订单数
    FROM sales
    GROUP BY user_id
)
SELECT 
    CASE 
        WHEN 订单数 = 1 THEN '仅1单'
        WHEN 订单数 BETWEEN 2 AND 3 THEN '2-3单'
        WHEN 订单数 BETWEEN 4 AND 5 THEN '4-5单'
        ELSE '5单以上'
    END AS 用户分层,
    COUNT(*) AS 用户数
FROM user_order_cnt
GROUP BY 用户分层;

-- 8. 每个类别 Top 3 商品（窗口函数）
SELECT 类别, 商品, 销售额, 排名
FROM (
    SELECT 
        category AS 类别,
        product_name AS 商品,
        ROUND(SUM(amount), 2) AS 销售额,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY SUM(amount) DESC) AS 排名
    FROM sales
    GROUP BY category, product_name
) t
WHERE 排名 <= 3;