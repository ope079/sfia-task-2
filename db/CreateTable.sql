CREATE DATABASE flask-db;


CREATE TABLE IF NOT EXISTS predictions
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          final_result VARCHAR(100) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;