import pandas as pd
from sklearn.model_selection import train_test_split
import os , sys

def load_dataset(filename):
    try:
        path = os.path.join(sys.path[0] , filename)
        data = pd.read_csv(path)
        print(f"File loaded successfully: {filename}")
        print(f"Data shape: {data.shape}")
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in the current directory.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def simple_random_sampling(data, sample_size=50, random_state=42):
    print("Simple Random Sampling (50 students):")
    if len(data) < sample_size:
        print(f"Not enough rows to sample {sample_size} rows. Total rows: {len(data)}")
        return None
    else:
        sample = data.sample(n=sample_size, random_state=random_state)
        print(sample.head())
        return sample

def stratified_sampling(data, stratify_column='Gender', test_size=0.2, random_state=42):
    print("Stratified Sampling (by Gender):")
    if stratify_column not in data.columns:
        print(f"Column '{stratify_column}' not found in dataset. Cannot perform stratified sampling.")
        return None
    else:
        try:
            train, test = train_test_split(
                data, 
                test_size=test_size, 
                stratify=data[stratify_column], 
                random_state=random_state
            )
            print(train.head())
            return train, test
        except Exception as e:
            print(f"Stratified sampling failed: {e}")
            return None

def systematic_sampling(data, step=10):
    print("Systematic Sampling (every 10th student):")
    if len(data) < step:
        print(f"Dataset too small for systematic sampling with step {step}. Total rows: {len(data)}")
        return None
    else:
        sample = data.iloc[::step]
        print(sample.head())
        return sample

def main():
    filename = input().strip()
    
    data = load_dataset(filename)
    
    if data is not None:
        print("Preview of Loaded Data:")
        print(data.head())
        
        simple_random_sampling(data, sample_size=50, random_state=42)
        
        stratified_sampling(data, stratify_column='Gender', test_size=0.2, random_state=42)
        
        systematic_sampling(data, step=10)

if __name__ == "__main__":
    main()