# Open the original file for reading in binary mode
with open('myapi/models.py', 'rb') as f:
    # Read the content of the file and decode it as UTF-8 while ignoring decoding errors
    content = f.read().decode('utf-8', errors='ignore')

# Remove null bytes from the content
content_cleaned = content.replace('\x00', '')

# Open the file again for writing the cleaned content
with open('myapi/models.py', 'w', encoding='utf-8') as f:
    # Write the cleaned content back to the file
    f.write(content_cleaned)