-- SQL query to create a trigger


DELIMITER $$

CREATE TRIGGER changed_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        UPDATE users SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;

    
