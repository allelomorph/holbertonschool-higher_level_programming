-- 0x0D. SQL - Introduction, task 17. Go to UTF8
-- Converts DB `hbtn_0c_0`, table `first_table`, and field `name` to UTF-8.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4
      COLLATE utf8mb4_unicode_ci;
/* ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256)
   CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; */
