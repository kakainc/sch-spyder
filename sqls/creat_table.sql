CREATE TABLE IF NOT EXISTS news_data(
   new_id     INT UNSIGNED AUTO_INCREMENT,
   new_title  VARCHAR(100) NOT NULL,
   new_author VARCHAR(40) NOT NULL,
   new_web    VARCHAR(100) NOT NULL,
   sub_date   DATE,
   PRIMARY KEY (new_id)
) DEFAULT CHARSET=utf8;