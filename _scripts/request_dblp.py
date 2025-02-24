import requests
from bs4 import BeautifulSoup
import re
import datetime

# 获取当前年份
current_year = datetime.datetime.now().year
start_year = current_year - 5

# 多个老师的 DBLP 页面 URL 列表
teacher_urls = [
    'https://dblp.org/pid/23/1695.html?view=bibtex',
    'https://dblp.org/pid/18/5099-3.html?view=bibtex',
    'https://dblp.org/pid/199/2729.html?view=bibtex',
    'https://dblp.org/pid/166/6045.html?view=bibtex',
    'https://dblp.org/pid/33/7597.html?view=bibtex',
    'https://dblp.org/pid/289/3851.html?view=bibtex',
    'https://dblp.org/pid/12/5927-14.html?view=bibtex'


    # 可以添加更多老师的 DBLP 页面 URL
]

all_bibtex_entries = []

for url in teacher_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有 BibTeX 条目
    bibtex_entries = soup.find_all('pre')

    for entry in bibtex_entries:
        bibtex = entry.get_text()
        # 提取年份
        year_match = re.search(r'year\s*=\s*{(\d{4})}', bibtex)
        if year_match:
            year = int(year_match.group(1))
            if start_year <= year <= current_year:
                all_bibtex_entries.append(bibtex)

# 将所有 BibTeX 条目合并为一个字符串
bibtex_data = '\n\n'.join(all_bibtex_entries)

# 保存到文件
with open('_bibliography/papers.bib', 'w', encoding='utf-8') as f:
    f.write(bibtex_data)