import os
import pandas as pd

def combine_files(input_folder, output_file):
    all_data = []
    
    # Loop through all files in the input folder
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        
        if file.endswith(".csv"):
            df = pd.read_csv(file_path)
            df["Source File"] = file  # Add column to track source file
            all_data.append(df)
            
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file_path, engine="openpyxl")  # Specify engine explicitly
            df["Source File"] = file  # Add column to track source file
            all_data.append(df)
            
        elif file.endswith(".xls"):  # Handle older Excel files
            df = pd.read_excel(file_path, engine="xlrd")
            df["Source File"] = file
            all_data.append(df)
    
    # Combine all data into a single DataFrame
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df.to_excel(output_file, index=False, engine="openpyxl")
        print(f"Data combined successfully into {output_file}")
    else:
        print("No CSV or Excel files found in the folder.")

# Example usage
input_folder = r"D:\OUTPUT_CU_External_Jan2025"  # Use raw string (r"") to avoid escape issues
output_file = "OUTPUT_CU_External_Jan2025_combined_data.xlsx"
combine_files(input_folder, output_file)
