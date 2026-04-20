import glob
import re

def clean_social_links():
    html_files = glob.glob('*.html')
    
    # Regex to match the social media icon block in the footer
    footer_social_pattern = re.compile(
        r'<div class="mt-4 md:mt-0 md:absolute md:right-0 flex gap-6">\s*<a[^>]*href="/"[^>]*>.*?public.*?</a>\s*<a[^>]*href="/"[^>]*>.*?group.*?</a>\s*<a[^>]*href="/"[^>]*>.*?camera.*?</a>\s*</div>',
        re.DOTALL
    )

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Remove empty footer icons
        content = footer_social_pattern.sub('', content)
        
        # If it's recursos.html, remove empty text links
        if file == 'recursos.html':
            content = re.sub(r'<a[^>]*href="/"[^>]*>LinkedIn</a>\s*', '', content)
            content = re.sub(r'<a[^>]*href="/"[^>]*>Facebook</a>\s*', '', content)
            content = re.sub(r'<a[^>]*href="/"[^>]*>Instagram</a>\s*', '', content)

        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Cleaned {file}")

if __name__ == "__main__":
    clean_social_links()
    print("Done cleaning social links.")
