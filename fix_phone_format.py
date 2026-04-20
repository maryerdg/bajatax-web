import os

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_js = "document.getElementById('leadTelefonoCompleto').value = lada + \" \" + phone;"
# Adding a single quote (apostrophe) at the beginning of the string prevents Google Sheets from interpreting the '+' as a formula.
new_js = "document.getElementById('leadTelefonoCompleto').value = \"'\" + lada + \" \" + phone;"

if old_js in content:
    content = content.replace(old_js, new_js)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated phone number formatting for Google Sheets.")
else:
    print("Could not find the target code.")
