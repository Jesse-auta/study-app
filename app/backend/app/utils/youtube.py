import re
def extract_youtube_id(url):
    """
    Extracts the video ID from a YouTube URL.
    Supports various YouTube URL formats.
    """
    pattern = (
        r'(?:https?:\/\/)?(?:www\.)?'
        r'(?:youtube\.com\/(?:watch\?v=|embed\/|v\/)|youtu\.be\/)'
        r'([a-zA-Z0-9_-]{11})'
    )
    match = re.match(pattern, url)
    return match.group(1) if match else None

def generate_youtube_thumbnail(url):
    video_id = extract_youtube_id(url)
    if not video_id:
        return None
    return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"