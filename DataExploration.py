import pandas as pd
import numpy as np

# Read the CSV file with explicit data type handling
try:
    # First, read the file without any type conversion
    data = pd.read_csv('SPU_Solid_Waste_Tons_and_Trips_Data_20250428.csv', dtype=str)
    
    # Display basic information about the dataset
    print("Dataset shape:", data.shape)
    print("\nFirst few rows of the dataset:")
    print(data.head())
    
    # Check for missing values
    missing_values = data.isnull().sum()
    print("\nMissing values:")
    print(missing_values)
    
    # Check data types
    print("\nData types:")
    print(data.dtypes)
    
    # Convert numeric columns
    for column in data.columns:
        try:
            # Try to convert to numeric, coercing errors to NaN
            data[column] = pd.to_numeric(data[column], errors='coerce')
        except Exception as e:
            print(f"Could not convert column '{column}' to numeric: {str(e)}")
    
    # Summary statistics for numeric columns
    print("\nSummary statistics for numeric columns:")
    numeric_data = data.select_dtypes(include=[np.number])
    print(numeric_data.describe())
    
except Exception as e:
    print(f"Error occurred: {str(e)}")
    print("\nTrying alternative approach...")
    
    # Alternative approach: read the file in chunks
    try:
        chunks = pd.read_csv('SPU_Solid_Waste_Tons_and_Trips_Data_20250428.csv', chunksize=1000)
        data = pd.concat(chunks)
        print("\nSuccessfully read data in chunks")
        print("Dataset shape:", data.shape)
    except Exception as e:
        print(f"Alternative approach also failed: {str(e)}")

# Check for any problematic columns
print("\nChecking for problematic columns:")
for column in data.columns:
    try:
        # Try to convert to numeric if possible
        pd.to_numeric(data[column], errors='raise')
        print(f"{column}: OK")
    except Exception as e:
        print(f"{column}: {str(e)}")

# Summary statistics for numeric columns only
print("\nSummary statistics for numeric columns:")
print(data.select_dtypes(include=[np.number]).describe())


