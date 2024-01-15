import json
from datetime import datetime
import xml.etree.ElementTree as ET
import requests

def parse_feed_and_append_to_json(feed_url, json_file):
    # Create a list to store entries with media
    entries_with_media = []

    response = requests.get(feed_url)
    rss_content = response.text
    root = ET.fromstring(rss_content)
    
    # Iterate through entries and filter those with media
    # Iterate through each 'item' element in the RSS feed
    for item in root.findall('.//item'):
        item_dict = {}

        # Extract information from the 'item' element
        item_dict['link'] = item.find('link').text
        item_dict['pubdate'] = item.find('pubDate').text

        description = item.find('description').text

        # remove the p tags from the summary
        description = description.replace('<p>', '')
        description = description.replace('</p>', '')

        # remove script tags from the summary
        # This doesn't really prevent XSS attacks,
        # but the account being followed should be trusted
        description = description.replace('<script>', '')
        description = description.replace('</script>', '')
        item_dict['description'] = description

        # Extract information from 'media:content' elements if available
        media_list = []
        for media_content in item.findall('.//media:content', namespaces={'media': 'http://search.yahoo.com/mrss/'}):
            media_dict = {}
            media_dict['link'] = media_content.attrib['url']
            media_dict['alt'] = media_content.find('media:description', namespaces={'media': 'http://search.yahoo.com/mrss/'}).text
            media_list.append(media_dict)

        if len(media_list) == 0:
            continue

        item_dict['media'] = media_list
        entries_with_media.append(item_dict)

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
