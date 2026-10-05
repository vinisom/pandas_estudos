select seller_id,sum(t1.price) as TotalRevenue,
                count(DISTINCT t1.order_id) as qtSalles
from tb_order_items as t1

GROUP BY seller_id

