import pandas as pd
from sqlalchemy import create_engine, text
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract(query,engine):
    """Extract data from a PostgreSQL database"""

    logging.info('Extracting data...')
    
    try:
        with engine.begin() as connection:
            df = pd.read_sql(text(query), connection)
            logging.info('Data successfully extracted!')
            return df
    except Exception as e:
        logging.error(f'Extraction failed with error: {e}')
        raise

def main():
    
    engine = create_engine('postgresql://postgres:423123@localhost:5433/stripe_db')
    query = 'SELECT * FROM product_usage'

    try:
        new_dataset = extract(query, engine)
        print(new_dataset.head())
    except Exception as e:
        logging.error(f'Data extraction failed on execution with error: {e}')

if __name__ == '__main__':
    main()