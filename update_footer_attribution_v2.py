import os
import re

def update_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_footer_content = """<div class="mt-8 flex justify-center">
        <a href="https://instagram.com/maryerdg" target="_blank" class="flex items-center gap-2 text-white/50 hover:text-white transition-colors group">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 1.366.062 2.633.332 3.608 1.308.975.975 1.245 2.242 1.308 3.608.058 1.266.07 1.646.07 4.85s-.012 3.584-.07 4.85c-.063 1.366-.333 2.633-1.308 3.608-.975.975-2.242 1.245-3.608 1.308-1.266.058-1.646.07-4.85.07s-3.584-.012-4.85-.07c-1.366-.063-2.633-.333-3.608-1.308-.975-.975-1.245-2.242-1.308-3.608-.058-1.266-.07-1.646-.07-4.85s.012-3.584.07-4.85c.062-1.366.332-2.633 1.308-3.608.975-.975 2.242-1.245 3.608-1.308 1.266-.058 1.646-.07 4.85-.07zm0-2.163c-3.259 0-3.667.014-4.947.072-1.373.063-2.674.343-3.664 1.332-.989.989-1.269 2.29-1.332 3.664-.058 1.28-.072 1.688-.072 4.947s.014 3.667.072 4.947c.063 1.373.343 2.674 1.332 3.664.989.989 2.29 1.269 3.664 1.332 1.28.058 1.688.072 4.947.072s3.667-.014 4.947-.072c1.374-.063 2.674-.343 3.664-1.332.989-.989 1.269-2.29 1.332-3.664.058-1.28.072-1.688.072-4.947s-.014-3.667-.072-4.947c-.063-1.373-.343-2.674-1.332-3.664-.989-.989-2.29-1.269-3.664-1.332-1.28-.058-1.688-.072-4.947-.072zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.791-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.209-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
          </svg>
          <span class="text-[10px] uppercase tracking-widest font-bold">Website by @maryerdg</span>
        </a>
      </div>"""

    # Check if already updated (to avoid double work or loops)
    if 'flex justify-center' in content and 'Website by @maryerdg' in content and 'instagram.com/maryerdg' in content:
        print(f"Already updated: {file_path}")
        return

    # Pattern 1: Replace existing attribution (even if vertical)
    # This matches the structure we just updated or the old one
    pattern_replace = r'<div class="mt-8 flex flex-col items-center gap-2">.*?Website by @maryerdg.*?instagram\.com/maryerdg.*?</div>'
    if re.search(pattern_replace, content, re.DOTALL):
        new_content = re.sub(pattern_replace, new_footer_content, content, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated (replaced): {file_path}")
        return

    # Pattern 2: Add if missing, but "Todos los derechos reservados" exists
    # We look for the paragraph containing "Todos los derechos reservados" inside the bottom div
    pattern_add = r'(<p class="text-center text-white/70 text-xs">\s*© 2026 Baja Tax\. Todos los derechos reservados\.\s*</p>)'
    if re.search(pattern_add, content):
        new_content = re.sub(pattern_add, r'\1\n      ' + new_footer_content, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated (added): {file_path}")
    else:
        print(f"Could not find target location in: {file_path}")

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                update_footer(os.path.join(root, file))

if __name__ == "__main__":
    main()
