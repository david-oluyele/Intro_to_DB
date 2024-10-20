-- Use the information_schema database
USE information_schema;

-- Query to get full description of the 'books' table
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH AS MAX_LENGTH,
    IS_NULLABLE,
    COLUMN_DEFAULT
FROM 
    COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'books';
