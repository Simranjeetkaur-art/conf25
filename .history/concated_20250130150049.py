import os
import shutil

def rename_files(master_folder):
    for root, dirs, files in os.walk(master_folder):
        for file in files:
            file_path = os.path.join(root, file)
            parent_folder = os.path.basename(os.path.dirname(file_path))
            
            # Concatenate folder name with file name
            new_file_name = f"{parent_folder}{file}"
            new_file_path = os.path.join(root, new_file_name)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {file} -> {new_file_name}")
    
    # Create a zip folder after renaming
    zip_folder = os.path.join(os.path.dirname(master_folder), os.path.basename(master_folder) + "_zipped")
    shutil.make_archive(zip_folder, 'zip', master_folder)
    print(f"Zip folder created: {zip_folder}.zip")

# Example usage
master_folder = "D:\\CU_External_Jan2025-20250128T042316Z-001"
rename_files(master_folder)





# import os
# import zipfile

# def concatenate_and_zip(master_folder, output_zip):
#     with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for root, dirs, files in os.walk(master_folder):
#             for file in files:
#                 relative_path = os.path.relpath(root, master_folder)
#                 folder_parts = relative_path.split(os.sep)
#                 new_file_name = "".join(folder_parts) + file  # Concatenate folder names with file name
#                 original_file_path = os.path.join(root, file)
#                 zipf.write(original_file_path, new_file_name)
#                 print(f"Added {original_file_path} as {new_file_name} to ZIP")
#     print(f"ZIP file created: {output_zip}")

# # Example usage
# master_folder = "D:\\CU_External_Jan2025-20250128T042316Z-001"  # Change this to your master data folder path
# output_zip = "master_data.zip"
# concatenate_and_zip(master_folder, output_zip)
