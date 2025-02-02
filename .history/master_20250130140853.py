import os
import pandas as pd

def compile_files_to_master(source_folder, output_file, file_extension='csv'):
    """
    Compile data from multiple files into a master sheet.
    
    Parameters:
    source_folder (str): Folder containing the source files.
    output_file (str): Path to save the compiled master sheet.
    file_extension (str): Extension of files to compile ('csv' or 'xlsx').
    """
    all_data = []
    
    for file in os.listdir(source_folder):
        if file.endswith(file_extension):
            file_path = os.path.join(source_folder, file)
            
            if file_extension == 'csv':
                df = pd.read_csv(file_path)
            elif file_extension == 'xlsx':
                df = pd.read_excel(file_path)
            else:
                continue
            
            df['Source_File'] = file  # Add source file name column
            all_data.append(df)
    
    if all_data:
        master_df = pd.concat(all_data, ignore_index=True)
        
        if file_extension == 'csv':
            master_df.to_csv(output_file, index=False)
        else:
            master_df.to_excel(output_file, index=False)
        
        print(f"Master sheet saved to {output_file}")
    else:
        print("No matching files found in the source folder.")

# Example usage
source_folder = "./D:/Final data"  # Update with your folder path
output_file = "./master_sheet.csv"  # Change to .xlsx for Excel output
compile_files_to_master(source_folder, output_file, file_extension='csv')