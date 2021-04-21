import sqlite3 as sql

def main():
    try: 
        db = sql.connect('library.db')
        cur = db.cursor()
        tablequery1 = """CREATE TABLE IF NOT EXISTS `users` (
                    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    `username` varchar(45) DEFAULT NULL,
                    `email` varchar(45) DEFAULT NULL,
                    `password` varchar(45) DEFAULT NULL
                )"""

        tablequery2 = """CREATE TABLE IF NOT EXISTS `authors` (
                      `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      `author` varchar(45) NOT NULL
                    )"""

        tablequery3 = """
        CREATE TABLE IF NOT EXISTS `books` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `title` varchar(255) DEFAULT NULL,
        `code` varchar(45) DEFAULT NULL,
        `description` varchar(255) DEFAULT NULL,
        `category` int DEFAULT NULL,
        `author` int DEFAULT NULL,
        `publisher` int DEFAULT NULL,
        `price` int DEFAULT NULL,
        CONSTRAINT `books_ibfk_1` FOREIGN KEY (`category`) REFERENCES `categories` (`id`),
        CONSTRAINT `books_ibfk_2` FOREIGN KEY (`author`) REFERENCES `authors` (`id`),
        CONSTRAINT `books_ibfk_3` FOREIGN KEY (`publisher`) REFERENCES `publishers` (`id`)
        )"""
        
        tablequery4 = """
        CREATE TABLE IF NOT EXISTS `categories` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `category` varchar(45) NOT NULL
        ) 
        """

        tablequery5 = """
        CREATE TABLE IF NOT EXISTS `clients` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `name` varchar(250) DEFAULT NULL,
        `email` varchar(250) DEFAULT NULL,
        `national_id` varchar(100) DEFAULT NULL
        )
        """

        tablequery6 = """
        CREATE TABLE IF NOT EXISTS `day_operations` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `client_id` int DEFAULT NULL,
        `book_id` int DEFAULT NULL,
        `type` varchar(25) DEFAULT NULL,
        `days` int DEFAULT NULL,
        `date` datetime DEFAULT NULL,
        `to_date` datetime DEFAULT NULL,
        CONSTRAINT `day_operations_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`),
        CONSTRAINT `day_operations_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
        )
        """

        tablequery7 = """
        CREATE TABLE IF NOT EXISTS `publishers` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `publisher` varchar(45) NOT NULL
        )
        """

        cur.execute(tablequery1)
        cur.execute(tablequery2)
        cur.execute(tablequery3)
        cur.execute(tablequery4)
        cur.execute(tablequery4)
        cur.execute(tablequery5)
        cur.execute(tablequery6)
        cur.execute(tablequery7)
        print("Tables Created Successfully")

    except sql.Error as e:
        print(e)
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()