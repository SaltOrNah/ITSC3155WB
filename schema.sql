DROP TYPE IF EXISTS part_type;
CREATE TYPE part_type AS ENUM('motherboard', 'cpu', 'storage', 'power', 'graphics', 'cooling', 'memory', 'casing');

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
    user_id         SERIAL          NOT NULL,
    username        VARCHAR(255)    UNIQUE NOT NULL,
    email           VARCHAR(255)    UNIQUE NOT NULL,
    hashed_password VARCHAR(255)    NOT NULL,
    is_admin        BOOLEAN         NOT NULL,
    PRIMARY KEY (user_id)
);

DROP TABLE IF EXISTS parts;
CREATE TABLE IF NOT EXISTS parts(
    part_id         SERIAL          NOT NULL,
    part_name       VARCHAR(255)    NOT NULL,
    part_type       part_type       NOT NULL,
    part_image      VARCHAR(255),
    part_url        VARCHAR(255)    NOT NULL,
    brand           VARCHAR(255),
    price           DECIMAL(10,2)   NOT NULL,
    rating          DECIMAL(5,1),
    PRIMARY KEY (part_id)
);

DROP TABLE IF EXISTS builds;
CREATE TABLE IF NOT EXISTS builds(
    build_id        SERIAL          NOT NULL,
    build_name      VARCHAR(255)    NOT NULL,
    build_timestamp TIMESTAMP       NOT NULL,
    is_private      BOOLEAN         NOT NULL,
    user_id         INT             NOT NULL,
    PRIMARY KEY (build_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

DROP TABLE IF EXISTS components;
CREATE TABLE IF NOT EXISTS components(
    part_id         INT             NOT NULL,
    build_id        INT             NOT NULL,
    quantity        INT             NOT NULL,
    FOREIGN KEY (build_id) REFERENCES builds(build_id),
    FOREIGN KEY (part_id) REFERENCES parts(part_id)
);

DROP TABLE IF EXISTS conflicts;
CREATE TABLE IF NOT EXISTS conflicts(
    part_id_A       INT             NOT NULL,
    part_id_B       INT             NOT NULL,
    PRIMARY KEY (part_id_A, part_id_B),
    FOREIGN KEY (part_id_A) REFERENCES parts(part_id),
    FOREIGN KEY (part_id_B) REFERENCES parts(part_id)
);

-- Inserting dummy data into the users table
INSERT INTO users (username, email, hashed_password, is_admin) VALUES
('user1', 'user1@example.com', 'hashed_password_1', FALSE),
('user2', 'user2@example.com', 'hashed_password_2', FALSE),
('admin', 'admin@example.com', 'hashed_password_admin', TRUE);

-- Inserting dummy data into the parts table
INSERT INTO parts (part_name, part_type, part_image, part_url, brand, price, rating) VALUES
('Motherboard 1', 'motherboard', 'motherboard_image_1.jpg', 'https://example.com/motherboard1', 'Brand A', 150.00, 4.5),
('CPU 1', 'cpu', 'cpu_image_1.jpg', 'https://example.com/cpu1', 'Brand B', 300.00, 4.8),
('Storage 1', 'storage', 'storage_image_1.jpg', 'https://example.com/storage1', 'Brand C', 100.00, 4.3),
('Power Supply 1', 'power', 'power_image_1.jpg', 'https://example.com/power1', 'Brand D', 80.00, 4.7),
('Graphics Card 1', 'graphics', 'graphics_image_1.jpg', 'https://example.com/graphics1', 'Brand E', 400.00, 4.9),
('Cooling 1', 'cooling', 'cooling_image_1.jpg', 'https://example.com/cooling1', 'Brand F', 50.00, 4.4),
('Memory 1', 'memory', 'memory_image_1.jpg', 'https://example.com/memory1', 'Brand G', 120.00, 4.6),
('Casing 1', 'casing', 'casing_image_1.jpg', 'https://example.com/casing1', 'Brand H', 70.00, 4.2);

-- Inserting dummy data into the builds table
INSERT INTO builds (build_name, build_timestamp, is_private, user_id) VALUES
('Gaming PC', '2024-04-07 00:27:54.898471', FALSE, 1),
('Workstation', '2024-04-07 00:29:33.521232', FALSE, 2),
('Server Build', '2024-04-07 00:33:07.744844', TRUE, 1);

-- Inserting dummy data into the components table
INSERT INTO components (part_id, build_id, quantity) VALUES
(1, 1, 1),
(2, 1, 1),
(3, 1, 2),
(4, 1, 1),
(5, 1, 1),
(6, 1, 1),
(7, 1, 4),
(8, 1, 1),
(2, 2, 1),
(3, 2, 1),
(7, 2, 2),
(8, 2, 1);

-- Inserting dummy data into the conflicts table
INSERT INTO conflicts (part_id_A, part_id_B) VALUES
(1, 5),
(2, 3),
(4, 6);
-- If we need this for some type of forum
-- CREATE TABLE IF NOT EXIST post(
--     post_id         SERIAL          NOT NULL,
--     user_id         INT             NOT NULL,
--     build_id        INT NULL,
--     body_text       TEXT,

--     PRIMARY KEY (post_id),
--     FOREIGN KEY (user_id) REFERENCES users(user_id),
--     FOREIGN KEY (build_id) REFERENCES builds(user_id)
-- );

-- CREATE TABLE IF NOT EXIST comment(
--     user_id         INT             NOT NULL,
--     post_id         INT             NOT NULL,
--     comment_txt     TEXT, 

--     FOREIGN KEY (user_id) REFERENCES users(user_id),
--     FOREIGN KEY (post_id) REFERENCES post(post_id)
-- );
