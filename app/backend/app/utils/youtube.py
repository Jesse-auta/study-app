import re


def is_valid_youtube_url(url):
    """
    Validates YouTube video URLs.
    Returns the video ID if valid, otherwise None.
    """
    # Regular expression for both long and short YouTube URLs
    pattern = (
        r'(?:https?:\/\/)?(?:www\.)?'
        r'(?:youtube\.com\/(?:watch\?v=|embed\/|v\/)|youtu\.be\/)'
        r'([A-Za-z0-9_-]{11})'
    )

    match = re.match(pattern, url)
    if match:
        return match.group(1)
    return None