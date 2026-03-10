-- images.sql

-- Create table for images
CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    filepath VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample INSERT statements
INSERT INTO images (filename, filepath) VALUES
('product1.png', '/home/codio/storage/uploads/product1.png'),
('product2.png', '/home/codio/storage/uploads/product2.png');
