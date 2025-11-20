import re

def build_drive_read_code(drive_url: str) -> str:
    match = re.search(r"/file/d/([^/]+)/", drive_url)
    if not match:
        raise ValueError("Could not extract file_id from the given URL.")

    file_id = match.group(1)

    code = f'''import pandas as pd

file_id = "{file_id}"
url = f"https://drive.google.com/uc?id={{file_id}}"

df = pd.read_csv(url)
'''
    return code


if __name__ == "__main__":
    drive_link = input("Enter Google Drive file link: ").strip()
    try:
        snippet = build_drive_read_code(drive_link)
        print("\nGenerated code:\n")
        print(snippet)
    except ValueError as e:
        print("Error:", e)