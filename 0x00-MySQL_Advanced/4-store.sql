-- SQL query to create a trigger


CREATE TRIGGER update_stock
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
