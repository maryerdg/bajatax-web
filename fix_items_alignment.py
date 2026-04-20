import glob

html_files = glob.glob('*.html')

for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Revert all items-start back to items-center (except for index)
        if f != 'index.html':
            content = content.replace('items-start', 'items-center')
            
            # Now carefully apply items-start ONLY to the hero grid
            content = content.replace(
                '<div class="grid lg:grid-cols-2 gap-10 md:gap-24 items-center">',
                '<div class="grid lg:grid-cols-2 gap-10 md:gap-24 items-start">'
            )
            
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            
    except Exception as e:
        print(f"Error {f}: {e}")

print("Fixed catastrophic items-start global replacement.")
