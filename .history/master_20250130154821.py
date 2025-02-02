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
input_folder = "D:\OUTPUT_CU_External_Jan2025-20250128T042316Z"  # Change this to your folder path
output_file = "combined_data.xlsx"
combine_files(input_folder, output_file)

# import os
# import shutil

# # Define input and output folder paths
# source_dir = r"D:\CU_External_Jan2025-20250128T042316Z"  
# destination_dir = r"D:\OUTPUT_CU_External_Jan2025-20250128T042316Z"

# Ensure the terminal uses UTF-8 encoding
# import sys
# sys.stdout.reconfigure(encoding='utf-8')

# def concatenate_folder_with_filename(src_root, dest_root):
#     for dirpath, dirnames, filenames in os.walk(src_root):
#         # Get the relative path from the source directory
#         relative_path = os.path.relpath(dirpath, src_root)
        
#         # Extract the last two folder names if possible
#         path_parts = relative_path.split(os.sep)
        
#         if len(path_parts) >= 2:
#             folder_prefix = path_parts[-2] + path_parts[-1]  # e.g., "BA EnglishSem 1"
#         else:
#             folder_prefix = path_parts[-1] if path_parts else ""

#         # Create the corresponding directory in the destination
#         new_dest_path = os.path.join(dest_root, relative_path)
#         os.makedirs(new_dest_path, exist_ok=True)

#         for filename in filenames:
#             old_file_path = os.path.join(dirpath, filename)
            
#             # Construct new filename
#             new_filename = f"{folder_prefix}{filename}"
#             new_file_path = os.path.join(new_dest_path, new_filename)

#             # Copy file to new location with the modified name
#             shutil.copy2(old_file_path, new_file_path)
            
#             # Print using ASCII-friendly arrow
#             print(f"Renamed & Copied: {old_file_path} -> {new_file_path}")

# # Run the function
# concatenate_folder_with_filename(source_dir, destination_dir)



