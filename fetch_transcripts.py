"""
fetch_transcripts.py

Fetches YouTube video transcripts and saves them as markdown files.
"""

import os
import re
from datetime import date
from youtube_transcript_api import YouTubeTranscriptApi

VIDEOS = [
    {
        "author_slug": "ross-simmonds",
        "title": "Content Distribution in the Age of AI",
        "video_id": "VXxFJAg7YJw",
        "date": "2025-10-08",
        "url": "https://www.youtube.com/watch?v=VXxFJAg7YJw",
    },
    {
        "author_slug": "aleyda-solis",
        "title": "The AI Search Optimization Roadmap",
        "video_id": "BjyF_4UhoOM",
        "date": "2025-09-09",
        "url": "https://www.youtube.com/watch?v=BjyF_4UhoOM",
    },
    {
        "author_slug": "mike-king",
        "title": "Mike King on Relevance Engineering, AI Search and the Query Fan Out Technique",
        "video_id": "pQLivtcqCZs",
        "date": "2025-05-27",
        "url": "https://www.youtube.com/watch?v=pQLivtcqCZs",
    },
    {
        "author_slug": "cyrus-shepard",
        "title": "Agents are early, visibility is urgent - Cyrus Shepard on 2025 AI SEO",
        "video_id": "ce_4AR5cx8A",
        "date": "2025-10-07",
        "url": "https://www.youtube.com/watch?v=ce_4AR5cx8A",
    },
    {
        "author_slug": "glenn-gabe",
        "title": "Google's December 2025 Broad Core Update - Core Update Notes with Glenn Gabe of GSQi",
        "video_id": "8hWV3DVSRf0",
        "date": "2025-12-23",
        "url": "https://www.youtube.com/watch?v=8hWV3DVSRf0",
    },
    {
        "author_slug": "garrett-sussman",
        "title": "Garrett Sussman - What Google Isn't Telling You About AI Search and Rankings",
        "video_id": "UMHaeT6Ou94",
        "date": "2025-08-29",
        "url": "https://www.youtube.com/watch?v=UMHaeT6Ou94",
    },
    {
        "author_slug": "eli-schwartz",
        "title": "Stop Chasing AI Citations - Eli Schwartz on SEO, Google AI Mode and Product-Led SEO",
        "video_id": "QPm1GA_5CZA",
        "date": "2026-04-28",
        "url": "https://www.youtube.com/watch?v=QPm1GA_5CZA",
    },{
        "author_slug": "kevin-indig",
        "title": "SEO in the Age of AI - Kevin Indig on Google Overviews, E-Commerce and The Future of Search",
        "video_id": "qujABKOAThA",
        "date": "2025-09-15",
        "url": "https://www.youtube.com/watch?v=qujABKOAThA",
    },
    {
        "author_slug": "lily-ray",
        "title": "The Future of SEO - Lily Ray on Google Updates, AI Search and GEO Spam",
        "video_id": "2htSIT0HLjs",
        "date": "2026-03-18",
        "url": "https://www.youtube.com/watch?v=2htSIT0HLjs",
    },
    {
        "author_slug": "britney-muller",
        "title": "Breaking Down AI & Search changes in 2025 with Britney Muller",
        "video_id": "l4fIHPtjIMY",
        "date": "2025-11-23",
        "url": "https://www.youtube.com/watch?v=l4fIHPtjIMY",
    },
]

OUTPUT_ROOT = "research/youtube-transcripts"


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text).strip("-")
    return text[:60]


def fetch_transcript(video_id):
    transcript_list = YouTubeTranscriptApi().fetch(video_id)
    lines = [entry.text for entry in transcript_list]
    return " ".join(lines)


def save_transcript(video):
    author = video["author_slug"]
    slug = slugify(video["title"])
    out_dir = os.path.join(OUTPUT_ROOT, author)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{video['date']}-{slug}.md")

    try:
        transcript_text = fetch_transcript(video["video_id"])
    except Exception as e:
        print(f"  ERROR fetching transcript for {video['title']}: {e}")
        return

    content = f"""# {video['title']}

**Author:** {author.replace('-', ' ').title()}
**Date published:** {video['date']}
**URL:** {video['url']}
**Collected on:** {date.today().isoformat()}

## Transcript

{transcript_text}
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  Saved: {out_path}")


def main():
    for video in VIDEOS:
        print(f"Fetching: {video['title']}")
        save_transcript(video)


if __name__ == "__main__":
    main()