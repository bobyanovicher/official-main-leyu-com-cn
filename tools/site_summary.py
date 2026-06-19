import json
from datetime import datetime

# 内置站点资料
SITE_DATA = [
    {
        "name": "乐鱼体育主站",
        "url": "https://official-main-leyu.com.cn",
        "tags": ["体育", "娱乐", "在线平台"],
        "keywords": ["乐鱼体育", "体育赛事", "娱乐平台"],
        "description": "提供多元化体育赛事与娱乐服务的综合性在线平台。"
    },
    {
        "name": "乐鱼体育备用入口",
        "url": "https://official-main-leyu.com.cn/backup",
        "tags": ["备用", "镜像", "体育"],
        "keywords": ["乐鱼体育", "备用入口", "镜像站点"],
        "description": "主站无法访问时的备用访问入口，确保服务连续性。"
    },
    {
        "name": "乐鱼体育帮助中心",
        "url": "https://official-main-leyu.com.cn/help",
        "tags": ["帮助", "FAQ", "支持"],
        "keywords": ["乐鱼体育", "帮助中心", "常见问题"],
        "description": "用户常见问题解答与技术支持信息汇总。"
    }
]

# 用于生成摘要的模板
SUMMARY_TEMPLATE = """
## 站点摘要 - {generated_at}

### 总览
共收录 {count} 个站点，覆盖以下标签：{all_tags}

### 详细条目
{entries}

---
*摘要由系统自动生成*
"""

ENTRY_TEMPLATE = """
#### {index}. {name}
- **URL**: {url}
- **标签**: {tags}
- **关键词**: {keywords}
- **说明**: {description}
"""

def collect_all_tags(data):
    """收集所有站点标签，去重后返回排序列表"""
    tag_set = set()
    for site in data:
        for tag in site["tags"]:
            tag_set.add(tag)
    return sorted(tag_set)

def build_entry(index, site):
    """根据索引和站点数据构建单条条目文本"""
    tags_str = ", ".join(site["tags"])
    keywords_str = ", ".join(site["keywords"])
    return ENTRY_TEMPLATE.format(
        index=index,
        name=site["name"],
        url=site["url"],
        tags=tags_str,
        keywords=keywords_str,
        description=site["description"]
    )

def build_entries(data):
    """构建所有条目的拼接文本"""
    entries_list = []
    for i, site in enumerate(data, start=1):
        entry = build_entry(i, site)
        entries_list.append(entry)
    return "".join(entries_list)

def generate_summary(data):
    """生成完整摘要文本"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    count = len(data)
    all_tags = collect_all_tags(data)
    all_tags_str = ", ".join(all_tags)
    entries = build_entries(data)
    return SUMMARY_TEMPLATE.format(
        generated_at=now,
        count=count,
        all_tags=all_tags_str,
        entries=entries
    )

def print_summary(summary_text):
    """打印摘要到控制台"""
    print(summary_text.strip())

def save_summary_to_file(summary_text, filepath="site_summary_output.txt"):
    """将摘要保存到文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(summary_text.strip())
    print(f"摘要已保存至: {filepath}")

def main():
    summary = generate_summary(SITE_DATA)
    print_summary(summary)
    save_summary_to_file(summary)

if __name__ == "__main__":
    main()