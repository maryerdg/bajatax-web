import os
import glob

html_files = glob.glob('*.html')

url1 = "https://lh3.googleusercontent.com/aida/ADBb0ui_-Y9OnGkRmlj1W2U9myw7c-NgvciQcyEqy8Z_5fPtGm_OnMVx85jzHq-1JMgN64czlhGEw_m3kkpzdB6wM5gdTbCH5Z18TQsfDsXwOym0maSXPpvTMCN9nbYkxZua1bsnyayrnHu7c9ofX9PmAxqtTjvwTzmCUrYSIeLUcoiPIPmzUKTNWr-iNfti1pFRF6st7rviv0IiaAo46rzwfy_5sr0Dq2w67tar-Sq6V7Z1yFMe43QkSbjfMkuM4JCQRgjBo8WqHrI7xA"
url2 = "https://lh3.googleusercontent.com/aida/ADBb0ugu_lk3-7CNFZ0qU2zVYLRTgieI5UMshuQkOMT5nKEJM42--cgW1rwSKxuTYpn8AO9mSUvF02XCKzPZdvl9uFAo25_x7lFCjHOeOW8WTRv4EWY1XpoYr5YGfyk4NQfWShw733_yXy4s96k4ctKAtsvaMUavI0qiObpwpiVafvY7_Cb6MPaCWb1E2xMJU6i3z84PTw4adn_3g83P_aOqzOYZz4aYDmDuor9s7o_fmwXgDjjo70OumZvdXoVzbi_oBEmbaK8Kmxt46g"
url3 = "https://lh3.googleusercontent.com/aida/ADBb0uiiSJEwg0BUqjp01MND8Rp7F0m01AAnqvJIBP0V0ys06EtfjLp8wNyDSoxnrnc6w6QLrOLeGynUH6uDGzHH7iZPtE19myeEWGw7FzEBW6SCjIWOOJHWjg2cYMWvlvdq_vgqZ88_FLa0Fze7EcQi2LYoFz9QvTM7h3Tge-_5tRgPPsH828Xs60U0X7rbWYDCPo_i101cwzpCH_jP7wI4Q2wb66b7spPcIO0IKzWY98Ne2mdiEbkbDu1L2MizybQ7PWmY1F_SfUT39w"

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(url1, "assets/logo1.png")
    content = content.replace(url2, "assets/logo2.png")
    # For url3, I'll replace it with logo2 (white) because it's on a dark background. 
    # I can also remove the inline css filter if it exists:
    content = content.replace(f'style="filter: brightness(0) invert(1);" src="{url3}"', f'src="assets/logo2.png"')
    content = content.replace(url3, "assets/logo2.png")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
