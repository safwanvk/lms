import sqlite3 as sql

def main():
    try: 
        db = sql.connect('library.db')
        cur = db.cursor()
        tablequery1 = """CREATE TABLE `users` (
                    `id` int NOT NULL AUTO_INCREMENT,
                    `username` varchar(45) DEFAULT NULL,
                    `email` varchar(45) DEFAULT NULL,
                    `password` varchar(45) DEFAULT NULL,
                    PRIMARY KEY (`id`)
                )"""

        tablequery2 = """CREATE TABLE `authors` (
                      `id` int NOT NULL AUTO_INCREMENT,
                      `author` varchar(45) NOT NULL,
                      PRIMARY KEY (`id`)
                    )"""

        tablequery3 = """
        CREATE TABLE `books` (
        `id` int NOT NULL AUTO_INCREMENT,
        `title` varchar(255) DEFAULT NULL,
        `code` varchar(45) DEFAULT NULL,
        `description` varchar(255) DEFAULT NULL,
        `category` int DEFAULT NULL,
        `author` int DEFAULT NULL,
        `publisher` int DEFAULT NULL,
        `price` int DEFAULT NULL,
        PRIMARY KEY (`id`),
        KEY `category` (`category`),
        KEY `author` (`author`),
        KEY `publisher` (`publisher`),
        CONSTRAINT `books_ibfk_1` FOREIGN KEY (`category`) REFERENCES `categories` (`id`),
        CONSTRAINT `books_ibfk_2` FOREIGN KEY (`author`) REFERENCES `authors` (`id`),
        CONSTRAINT `books_ibfk_3` FOREIGN KEY (`publisher`) REFERENCES `publishers` (`id`)
        )"""
        
        tablequery4 = """
        CREATE TABLE `categories` (
        `id` int NOT NULL AUTO_INCREMENT,
        `category` varchar(45) NOT NULL,
        PRIMARY KEY (`id`)
        ) 
        """

        tablequery5 = """
        CREATE TABLE `clients` (
        `id` int NOT NULL AUTO_INCREMENT,
        `name` varchar(250) DEFAULT NULL,
        `email` varchar(250) DEFAULT NULL,
        `national_id` varchar(100) DEFAULT NULL,
        PRIMARY KEY (`id`)
        )
        """

        tablequery6 = """
        CREATE TABLE `day_operations` (
        `id` int NOT NULL AUTO_INCREMENT,
        `client_id` int DEFAULT NULL,
        `book_id` int DEFAULT NULL,
        `type` varchar(25) DEFAULT NULL,
        `days` int DEFAULT NULL,
        `date` datetime DEFAULT NULL,
        `to_date` datetime DEFAULT NULL,
        PRIMARY KEY (`id`),
        KEY `client_id` (`client_id`),
        KEY `book_id` (`book_id`),
        CONSTRAINT `day_operations_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`),
        CONSTRAINT `day_operations_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
        )
        """

        tablequery7 = """
        CREATE TABLE `publishers` (
        `id` int NOT NULL AUTO_INCREMENT,
        `publisher` varchar(45) NOT NULL,
        PRIMARY KEY (`id`)
        )
        """

        cur.execute(tablequery1, tablequery2, tablequery3, tablequery4, tablequery5, tablequery6, tablequery7)
        print("Tables Created Successfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()