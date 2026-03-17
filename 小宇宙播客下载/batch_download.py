import json
import os
import requests
import re

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename).strip()

def download_file(url, filename):
    print(f"正在下载: {filename}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"下载完成: {filename}")
    except Exception as e:
        print(f"下载失败 {filename}: {e}")

def main():
    # 从环境变量读取工作目录，默认为 ~/Downloads/podcasts
    base_dir = os.environ.get('PODCAST_DOWNLOAD_DIR', os.path.expanduser('~/Downloads/podcasts'))
    json_path = os.path.join(base_dir, 'episodes.json')

    if not os.path.exists(json_path):
        print(f"找不到配置文件: {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        episodes = json.load(f)

    for ep in episodes:
        podcast_name = ep.get('podcast', '未分类')
        title = ep['title']
        url = ep['audio_url']

        # 为每个播客创建独立的子文件夹
        podcast_dir = os.path.join(base_dir, 'downloads', sanitize_filename(podcast_name))
        if not os.path.exists(podcast_dir):
            os.makedirs(podcast_dir)

        ext = os.path.splitext(url.split('?')[0])[1] or '.m4a'
        filename = os.path.join(podcast_dir, sanitize_filename(title) + ext)

        if os.path.exists(filename):
            print(f"文件已存在，跳过: {filename}")
            continue

        download_file(url, filename)

if __name__ == "__main__":
    main()
