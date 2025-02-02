import os
import pandas as pd

def combine_files(input_folder, output_file):
    all_data = []
    
    # Loop through all files in the input folder
    for file in os.listdir(input_folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(input_folder, file))
            df["Source File"] = file  # Add column to track source file
            all_data.append(df)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(input_folder, file))
            df["Source File"] = file  # Add column to track source file
            all_data.append(df)
    
    # Combine all data into a single DataFrame
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df.to_excel(output_file, index=False)
        print(f"Data combined successfully into {output_file}")
    else:
        print("No CSV or Excel files found in the folder.")

# Example usage
input_folder = "D/"  # Change this to your folder path
output_file = "combined_data.xlsx"
combine_files(input_folder, output_file)