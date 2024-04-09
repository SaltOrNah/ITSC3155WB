DROP DATABASE IF EXIST PartsComp;
CREATE DATABASE IF NOT EXIST PartsComp;

DROP TYPE IF EXISTS part_type;
CREATE TYPE part_type AS ENUM('motherboard', 'cpu', 'storage', 'power', 'graphics', 'cooling', 'memory', 'casing');

CREATE TABLE IF NOT EXIST users(
    user_id         SERIAL          NOT NULL,
    username        VARCHAR(255)    NOT NULL,
    email           VARCHAR(255)    UNIQUE NOT NULL,
    hashed_password VARCHAR(255)    NOT NULL,
    is_admin        BOOLEAN         NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXIST parts(
    part_id         SERIAL          NOT NULL,
    part_name       VARCHAR(255)    NOT NULL,
    part_type       part_type       NOT NULL,
    brand           VARCHAR(255),
    price           DECIMAL(10,2)   NOT NULL,
    rating          DECIMAL(5,1),
    PRIMARY KEY (part_id)
);

CREATE TABLE IF NOT EXIST builds(
    build_id        SERIAL          NOT NULL,
    build_name      VARCHAR(255)    NOT NULL,
    refer_url       VARCHAR(255)    NOT NULL,
    time_created    TIMESTAMP       NOT NULL,
    is_private      BOOLEAN         NOT NULL,
    total_price     DECIMAL(10,2)   NOT NULL,
    user_id         INT             NOT NULL,
    PRIMARY KEY (build_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXIST components(
    part_id         INT             NOT NULL,
    build_id        INT             NOT NULL,
    quantity        INT             NOT NULL,
    FOREIGN KEY (build_id) REFERENCES builds(build_id),
    FOREIGN KEY (part_id) REFERENCES parts(part_id)
);

CREATE TABLE IF NOT EXIST conflicts(
    part_id_A       INT             NOT NULL,
    part_id_B       INT             NOT NULL,
    PRIMARY KEY (part_id_A, part_id_B),
    FOREIGN KEY (part_id_A) REFERENCES parts(part_id),
    FOREIGN KEY (part_id_B) REFERENCES parts(part_is)
);

-- If we need this for some type of forum
CREATE TABLE IF NOT EXIST post(
    post_id         SERIAL          NOT NULL,
    user_id         INT             NOT NULL,
    build_id        INT NULL,
    body_text       TEXT,

    PRIMARY KEY (post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (build_id) REFERENCES builds(user_id)
);

CREATE TABLE IF NOT EXIST comment(
    user_id         INT             NOT NULL,
    post_id         INT             NOT NULL,
    comment_txt     TEXT, 

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);