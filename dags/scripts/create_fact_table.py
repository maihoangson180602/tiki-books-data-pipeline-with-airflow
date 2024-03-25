import pandas as pd
from sqlalchemy import create_engine
import psycopg2


drop_fact_table = """
            DROP TABLE IF EXISTS FACT_TABLE;
"""
create_fact_table = """
    CREATE TABLE FACT_TABLE (
        id INT GENERATED BY DEFAULT AS IDENTITY (START WITH 1 INCREMENT BY 1),
        product_id VARCHAR(20), -- REFERENCES DIMBOOK(product_id), 
        category_id INT, -- REFERENCES DIMCATEGORY(category_id),
        sku VARCHAR(50),
        quantity_sold INT,
        price REAL,
        original_price REAL,
        discount REAL,
        discount_rate REAL,
        PRIMARY KEY(id)
    );
"""


def main():
    alchemyEngine = create_engine(
        "postgresql+psycopg2://hoangson:11111@localhost/airflow"
    )

    conn = psycopg2.connect(
        database="airflow",
        user="hoangson",
        password="1111",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()
    cur.execute(drop_fact_table)
    cur.execute(create_fact_table)

    conn.commit()
    conn.close()
    cur.close()


if __name__ == "__main__":
    main()