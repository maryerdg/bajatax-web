import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace logo1.png with favicon.png for the favicons
    content = content.replace('href="assets/logo1.png"', 'href="assets/favicon.png"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated favicons to use favicon.png in {file}')
