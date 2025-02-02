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

# Define source and destination directories
source_dir = "D:\\CU_External_Jan2025-20250128T042316Z"  # Replace with your actual path
destination_dir = "D:\CU_External_Jan2025-20250128T042316Z"  # Replace with your actual path

def concatenate_folder_with_filename(src_root, dest_root):
    for dirpath, dirnames, filenames in os.walk(src_root):
        # Get the relative path from the source directory
        relative_path = os.path.relpath(dirpath, src_root)
        
        # Extract necessary parts of the folder path for renaming files
        path_parts = relative_path.split(os.sep)
        
        if len(path_parts) >= 2:  # Ensure at least two-level hierarchy exists
            folder_prefix = path_parts[-2] + path_parts[-1]  # e.g., "BA EnglishSem 1"
        else:
            folder_prefix = path_parts[-1] if path_parts else ""

        # Create the corresponding directory in the destination
        new_dest_path = os.path.join(dest_root, relative_path)
        os.makedirs(new_dest_path, exist_ok=True)

        for filename in filenames:
            old_file_path = os.path.join(dirpath, filename)
            
            # Construct new filename
            new_filename = f"{folder_prefix}{filename}"
            new_file_path = os.path.join(new_dest_path, new_filename)

            # Copy file to new location with the modified name
            shutil.copy2(old_file_path, new_file_path)
            print(f"Renamed & Copied: {old_file_path} → {new_file_path}")

# Run the function
concatenate_folder_with_filename(source_dir, destination_dir)

