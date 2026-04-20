import glob
import re

html_files = glob.glob('*.html')

hamburger_script = """
<!-- Mobile Menu Script -->
<script>
function toggleMobileMenu() {
    const menu = document.getElementById('mobile-menu');
    const isHidden = menu.classList.contains('translate-x-full');
    if (isHidden) {
        menu.classList.remove('translate-x-full');
        document.body.style.overflow = 'hidden';
    } else {
        menu.classList.add('translate-x-full');
        document.body.style.overflow = '';
    }
}
</script>
"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Inject missing script
    if '<script>\\nfunction toggleMobileMenu' not in content:
        content = content.replace('</body>', hamburger_script + '\\n</body>')

    # 2. Fix Card paddings globally (index, recursos, servicios)
    content = content.replace('p-12 ', 'p-8 md:p-12 ')
    content = content.replace('p-10 ', 'p-6 md:p-10 ')
    content = content.replace('p-8 ', 'p-6 md:p-8 ')

    # 3. Fix text sizes that might still be too big
    content = content.replace('text-lg', 'text-base md:text-lg')
    content = content.replace('text-xl', 'text-lg md:text-xl')
    content = content.replace('text-2xl', 'text-xl md:text-2xl')

    # 4. Clean up overlapping replacements just in case
    content = content.replace('text-base md:text-base md:text-lg', 'text-base md:text-lg')
    content = content.replace('text-lg md:text-lg md:text-xl', 'text-lg md:text-xl')
    content = content.replace('p-6 md:p-8 md:p-12', 'p-8 md:p-12')
    content = content.replace('p-6 md:p-6 md:p-10', 'p-6 md:p-10')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Fixed mobile inconsistencies and script.")
