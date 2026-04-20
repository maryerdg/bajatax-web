import os

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Modal Flex Centering
if "hidden items-center justify-center" in content:
    pass

# We can fix the JS directly to add 'flex' instead of just removing 'hidden'
old_open = """    overlay.classList.remove('hidden');"""
new_open = """    overlay.classList.remove('hidden');
    overlay.classList.add('flex');"""
content = content.replace(old_open, new_open)

old_close = """    setTimeout(() => {
      overlay.classList.add('hidden');
    }, 300);"""
new_close = """    setTimeout(() => {
      overlay.classList.remove('flex');
      overlay.classList.add('hidden');
    }, 300);"""
content = content.replace(old_close, new_close)

# Replace the Lada part
old_phone_div = """<span class="inline-flex items-center px-4 rounded-l-xl border border-r-0 border-outline-variant/30 bg-surface-container-low text-on-surface-variant text-sm font-bold">
            +52
          </span>"""

new_phone_div = """<select id="leadLada" class="outline-none appearance-none cursor-pointer pl-3 pr-2 lg:px-4 rounded-l-xl border border-r-0 border-outline-variant/30 bg-surface-container-low text-on-surface-variant text-sm font-bold focus:outline-none focus:border-secondary transition-colors">
            <option value="+52">🇲🇽 +52</option>
            <option value="+1">🇺🇸 +1</option>
            <option value="+57">🇨🇴 +57</option>
            <option value="+54">🇦🇷 +54</option>
            <option value="+56">🇨🇱 +56</option>
            <option value="+51">🇵🇪 +51</option>
          </select>"""

content = content.replace(old_phone_div, new_phone_div)

# Update the JS reading the phone
old_js_phone = """const phone = document.getElementById('leadPhone').value;"""
new_js_phone = """const phone = document.getElementById('leadLada').value + ' ' + document.getElementById('leadPhone').value;"""
content = content.replace(old_js_phone, new_js_phone)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated recursos.html to fix centering and add lada select.')
