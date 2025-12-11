SELECT 
    s.seller_id,
    SUM(oi.price) AS total_revenue
FROM olist_sellers s
JOIN olist_order_items oi ON s.seller_id = oi.seller_id
JOIN olist_orders o ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY s.seller_id
ORDER BY total_revenue DESC
LIMIT 10;
