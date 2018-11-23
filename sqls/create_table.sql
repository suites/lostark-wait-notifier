CREATE DATABASE db;
USE db;

CREATE TABLE server (
  server_id INT(100) unsigned NOT NULL AUTO_INCREMENT,
  server_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (server_id)
);
CREATE INDEX IDX_SERVER_ID ON server(server_id);

CREATE TABLE queue (
  date_time DATETIME NOT NULL,
  server_id INT(100) NOT NULL,
  queue INT(100) NOT NULL,
  PRIMARY KEY (date_time, server_id)
);
CREATE INDEX IDX_SERVER_ID ON queue(server_id);
CREATE INDEX IDX_DATE_TIME ON queue(date_time desc);