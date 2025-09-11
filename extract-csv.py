import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_csv(csv_file):
    
    """Extract data from a CSV"""

    logging.info("Extracting data...")

    try:
        new_csv = pd.read_csv(csv_file, delimiter=';')
        return new_csv
    except Exception as e:
        logging.error(f'Extraction failed with error: {e}')
        raise


def main ():
    try:
        new_dataset = extract_csv('segmentation.csv')
        logging.info('Data successfully extracted!')
        print(new_dataset.head())
    except Exception as e:
        logging.error(f'Extraction failed on execution with error: {e}')

if __name__ == '__main__':
    main()