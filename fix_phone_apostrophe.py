import os

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the dot to an apostrophe
old_js = "document.getElementById('leadTelefonoCompleto').value = \".\" + lada + \" \" + phone;"
new_js = "document.getElementById('leadTelefonoCompleto').value = \"'\" + lada + \" \" + phone;"

if old_js in content:
    content = content.replace(old_js, new_js)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated phone number formatting to use apostrophe.")
else:
    print("Could not find the target code.")
