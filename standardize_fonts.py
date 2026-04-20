import glob
import re

html_files = glob.glob('*.html')

standard_css = """
    /* Uniformidad Tipográfica Global */
    h1 { font-size: clamp(32px, 6vw, 56px) !important; font-weight: 800 !important; letter-spacing: -0.03em !important; line-height: 1.1 !important; }
    h2 { font-size: clamp(26px, 4.5vw, 40px) !important; font-weight: 700 !important; letter-spacing: -0.02em !important; line-height: 1.2 !important; }
    h3 { font-size: clamp(20px, 3vw, 28px) !important; font-weight: 700 !important; letter-spacing: -0.01em !important; line-height: 1.3 !important; }
"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove existing h1, h2, h3 rules from previous style blocks
    content = re.sub(r'h1\s*\{[^}]+\}', '', content)
    content = re.sub(r'h2\s*\{[^}]+\}', '', content)
    content = re.sub(r'h3\s*\{[^}]+\}', '', content)
    content = re.sub(r'/\* Uniformidad Tipográfica Global \*/', '', content)
    
    # Inject standard css into the style tags
    if '<style>' in content:
        content = content.replace('<style>', '<style>\\n' + standard_css)
    else:
        # If no style block exists, create one in head
        content = content.replace('</head>', '<style>\\n' + standard_css + '\\n</style>\\n</head>')

    # Strip competing text size classes from headings just to be extra clean
    # Finds <h1 class="..."> and removes text-Xxl and md:text-Xxl
    
    def strip_text_classes(match):
        pre = match.group(1)
        classes = match.group(2)
        post = match.group(3)
        # remove words matching text-\S+ or md:text-\S+
        clean_classes = re.sub(r'\\b(md:)?text-[0-9]+xl\\b', '', classes)
        clean_classes = re.sub(r'\\b(md:)?text-(sm|base|lg)\\b', '', clean_classes)
        # cleanup extra spaces
        clean_classes = re.sub(r'\\s+', ' ', clean_classes).strip()
        return f'{pre}class="{clean_classes}"{post}'

    content = re.sub(r'(<h[123]\b[^>]*?)class="([^"]*)"([^>]*>)', strip_text_classes, content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Standardized all headings successfully.")
