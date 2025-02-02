# import os
# import pandas as pd

# def combine_files(input_folder, output_file):
#     all_data = []
    
#     # Loop through all files in the input folder
#     for file in os.listdir(input_folder):
#         if file.endswith(".csv"):
#             df = pd.read_csv(os.path.join(input_folder, file))
#             df["Source File"] = file  # Add column to track source file
#             all_data.append(df)
#         elif file.endswith(".xlsx"):
#             df = pd.read_excel(os.path.join(input_folder, file))
#             df["Source File"] = file  # Add column to track source file
#             all_data.append(df)
    
#     # Combine all data into a single DataFrame
#     if all_data:
#         combined_df = pd.concat(all_data, ignore_index=True)
#         combined_df.to_excel(output_file, index=False)
#         print(f"Data combined successfully into {output_file}")
#     else:
#         print("No CSV or Excel files found in the folder.")

# # Example usage
# input_folder = "D:\\Final data"  # Change this to your folder path
# output_file = "combined_data.xlsx"
# combine_files(input_folder, output_file)

import os
import shutil

def concatenate_and_zip(master_folder, output_zip):
    temp_folder = "temp_data"
    os.makedirs(temp_folder, exist_ok=True)
    
    for root, dirs, files in os.walk(master_folder):
        for file in files:
            # Extract folder names from root path
            relative_path = os.path.relpath(root, master_folder)
            folder_parts = relative_path.split(os.sep)
            
            if folder_parts:  # Ensure there are folder names
                new_file_name = "".join(folder_parts) + file  # Concatenate folder names with file name
                source_file = os.path.join(root, file)
                destination_file = os.path.join(temp_folder, new_file_name)
                
                shutil.copy(source_file, destination_file)
    
    # Create zip file
    shutil.make_archive(output_zip, 'zip', temp_folder)
    shutil.rmtree(temp_folder)  # Clean up temporary folder
    print(f"Zipped files saved as {output_zip}.zip")

# Example usage
master_folder = "CU_External_Jan2025-20250128T042316Z-001_zipped"  # Change as needed
output_zip = "MasterData"
concatenate_and_zip(master_folder, output_zip)
