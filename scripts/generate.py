import json
from datetime import datetime
import feedparser

def parse_feed_and_append_to_json(feed_url, json_file):
    # Parse the feed
    feed = feedparser.parse(feed_url)

    # Create a list to store entries with media
    entries_with_media = []

    # Iterate through entries and filter those with media
    for entry in feed.entries:
        # check if there is media and it is an image
        if 'media_content' in entry and entry.media_content and 'image' in entry.media_content[0]['type']:
            # remove the p tags from the summary
            entry.summary = entry.summary.replace('<p>', '')
            entry.summary = entry.summary.replace('</p>', '')

            # remove script tags from the summary
            # This doesn't really prevent XSS attacks,
            # but the account being followed should be trusted
            entry.summary = entry.summary.replace('<script>', '')
            entry.summary = entry.summary.replace('</script>', '')

            # Extract relevant information
            entry_data = {
                'link': entry.link,
                'pubdate': entry.published,
                'description': entry.summary,
                'media_link': entry.media_content[0]['url'],
                'media_alt': entry.content[0]['value'] if entry.content else "The print"
            }
            entries_with_media.append(entry_data)

    # If there are entries with media, append them to the JSON file
    if entries_with_media:
        # Load existing data from the JSON file, if any
        existing_data = []
        try:
            with open(json_file, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            pass

        # Remove duplicates based on the link and keep the latest version
        unique_entries = {entry['link']: entry for entry in existing_data}
        unique_entries.update({entry['link']: entry for entry in entries_with_media})

        # Sort entries by date with more recent entries first
        sorted_entries = sorted(unique_entries.values(), key=lambda x: datetime.strptime(x['pubdate'], "%a, %d %b %Y %H:%M:%S %z"), reverse=True)

        # Write the sorted and unique entries back to the JSON file
        with open(json_file, 'w') as file:
            json.dump(sorted_entries, file, indent=2)

if __name__ == "__main__":
    # Get the feed URL and JSON file name from the command line
    import sys
    feed_url = sys.argv[1]
    json_file = sys.argv[2]

    parse_feed_and_append_to_json(feed_url, json_file)
