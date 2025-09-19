-- ==============================
-- Northwind – Solutions (SQL)
-- ==============================
-- Parametriza el esquema si lo necesitas (en psql):
-- \set schema 'public'
-- y usa :schema en los nombres cualificados.

-- Ejercicio 2.1: Empleados
SELECT e.employee_id, e.first_name, e.last_name, e.city, e.country
FROM :schema.employees e
ORDER BY e.employee_id;

-- Ejercicio 2.2: Productos (con stock y descontinuados)
SELECT p.product_id, p.supplier_id, p.product_name, p.unit_price, 
       p.units_in_stock, p.units_on_order, p.discontinued
FROM :schema.products p
ORDER BY p.product_id;

-- Ejercicio 2.3: Productos descontinuados (1 = descontinuado)
SELECT p.product_name, p.units_in_stock
FROM :schema.products p
WHERE p.discontinued = 1
ORDER BY p.units_in_stock DESC NULLS LAST, p.product_name;

-- Ejercicio 2.4: Proveedores
SELECT s.supplier_id, s.company_name, s.city, s.country
FROM :schema.suppliers s
ORDER BY s.supplier_id;

-- Ejercicio 2.5: Pedidos
SELECT o.order_id, o.customer_id, o.ship_via, o.order_date, o.required_date, o.shipped_date
FROM :schema.orders o
ORDER BY o.order_id;

-- Ejercicio 2.6: Número de pedidos
SELECT COUNT(*) AS num_pedidos FROM :schema.orders;

-- Ejercicio 2.7: Clientes
SELECT c.customer_id, c.company_name, c.city, c.country
FROM :schema.customers c
ORDER BY c.customer_id;

-- Ejercicio 2.8: Transportistas
SELECT sh.shipper_id, sh.company_name
FROM :schema.shippers sh
ORDER BY sh.shipper_id;

-- Ejercicio 2.9: Relaciones de reporte entre empleados
SELECT e.employee_id, e.first_name || ' ' || e.last_name AS empleado,
       e.reports_to AS manager_id,
       m.first_name || ' ' || m.last_name AS manager
FROM :schema.employees e
LEFT JOIN :schema.employees m ON m.employee_id = e.reports_to
ORDER BY e.employee_id;

-- ==============================
-- Ejercicio 4: Queries avanzadas
-- ==============================

-- 4.1: Última vez que se pidió un producto de cada categoría
SELECT c.category_id, c.category_name, MAX(o.order_date) AS last_order_date
FROM :schema.categories c
JOIN :schema.products p ON p.category_id = c.category_id
JOIN :schema.order_details od ON od.product_id = p.product_id
JOIN :schema.orders o ON o.order_id = od.order_id
GROUP BY c.category_id, c.category_name
ORDER BY c.category_id;

-- 4.2: Productos que nunca se vendieron a su precio original (orders con unit_price <> products.unit_price)
-- Nota: en Northwind, el precio aplicado al pedido (od.unit_price) puede diferir del precio de catálogo (p.unit_price).
SELECT p.product_id, p.product_name
FROM :schema.products p
WHERE NOT EXISTS (
  SELECT 1
  FROM :schema.order_details od
  WHERE od.product_id = p.product_id
    AND od.unit_price = p.unit_price
);

-- 4.3: Productos con categoría "Confections" (ID y nombre)
SELECT p.product_id, p.product_name, p.category_id
FROM :schema.products p
JOIN :schema.categories c ON c.category_id = p.category_id
WHERE c.category_name = 'Confections'
ORDER BY p.product_id;

-- 4.4: Proveedores prescindibles (todos sus productos descontinuados)
SELECT s.supplier_id, s.company_name
FROM :schema.suppliers s
WHERE NOT EXISTS (
  SELECT 1
  FROM :schema.products p
  WHERE p.supplier_id = s.supplier_id
    AND p.discontinued = 0
);

-- 4.5: Clientes que compraron > 30 artículos "Chai" en un único pedido
SELECT o.customer_id, o.order_id, SUM(od.quantity) AS qty_chai
FROM :schema.orders o
JOIN :schema.order_details od ON od.order_id = o.order_id
JOIN :schema.products p ON p.product_id = od.product_id
WHERE p.product_name = 'Chai'
GROUP BY o.customer_id, o.order_id
HAVING SUM(od.quantity) > 30
ORDER BY qty_chai DESC;

-- 4.6: Clientes con suma total de "freight" > 1000
SELECT o.customer_id, SUM(o.freight) AS total_freight
FROM :schema.orders o
GROUP BY o.customer_id
HAVING SUM(o.freight) > 1000
ORDER BY total_freight DESC;

-- 4.7: Ciudades con 5 o más empleados
SELECT COALESCE(city,'(sin ciudad)') AS city, COUNT(*) AS num_empleados
FROM :schema.employees
GROUP BY COALESCE(city,'(sin ciudad)')
HAVING COUNT(*) >= 5
ORDER BY num_empleados DESC, city;
