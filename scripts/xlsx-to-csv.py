import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    try:
        df = pd.read_excel(xlsx_file)
        df.to_csv(csv_file, index=False)

        print(f"Conversion successful. CSV file saved as {csv_file}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
convert_xlsx_to_csv("/content/100_random_comments_sports.xlsx", "output.csv")
