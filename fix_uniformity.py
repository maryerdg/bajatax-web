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
    
    # 1. Cleanup the corrupted literals: '\n' that were written verbatim into the files
    content = content.replace("<style>\\n", "<style>\n")
    content = content.replace("\\n</style>\\n</head>", "\n</style>\n</head>")
    content = content.replace("<style>\\\\n", "<style>\n")
    
    # Also if the standard_css is prepended with 'n ', that was the broken parse, but replacing \n fixes it.
    
    # Because my previous script failed to strip tailwind text-Xxl from other files:
    # I will do it here carefully. Without raw string \b issues.
    
    def strip_text_classes(match):
        pre = match.group(1)
        classes = match.group(2)
        post = match.group(3)
        # Using string split to safely remove any class that starts with text- or md:text- or lg:text-
        # specifying sizes:
        tokenized = classes.split()
        filtered = []
        for token in tokenized:
            if 'text-' in token and ('xl' in token or 'base' in token or 'sm' in token or 'lg' in token):
                continue
            filtered.append(token)
            
        clean_classes = " ".join(filtered)
        return f'{pre}class="{clean_classes}"{post}'

    # We match <h1 ... class="...">
    content = re.sub(r'(<h[123]\b[^>]*?)class="([^"]*)"([^>]*>)', strip_text_classes, content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Fixed CSS corruption and properly standardized headings.")
