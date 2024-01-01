from feedgen.feed import FeedGenerator
import datetime
import json

def generate_rss(json_file, rss_file):
    # Load JSON data from file
    with open(json_file, "r", encoding="utf-8") as json_file:
        json_data = json_file.read()

    # Parse JSON data
    entries = json.loads(json_data)

    fg = FeedGenerator()
    fg.id('https://prints.graic.net')
    fg.title('Graic\'s Prints')
    fg.author(name = 'Graic')
    fg.link( href='https://prints.graic.net', rel='alternate' )
    fg.logo('https://prints.graic.net/logo.png')
    fg.subtitle('Prints by Graic')
    fg.link( href='https://prints.graic.net', rel='self' )
    fg.language('en')

    for entry in entries:
        fe = fg.add_entry()
        fe.guid(entry['link'], permalink=True)
        fe.title('Graic\'s Prints')
        fe.description(entry['description'] + '<br>' + f'<img src="{entry["media_link"]}" alt="{entry["media_alt"]}" />')
        # if entry['media_link'] != '':
        #     # get file type
        #     file_type = entry['media_link'].split('.')[-1]
        #     if file_type == 'jpg':
        #         file_type = 'jpeg'
        #     fe.link(href=entry['media_link'], rel='enclosure', type=f'image/{file_type}', title=entry['media_alt'])

        pub_date = datetime.datetime.strptime(entry['pubdate'], "%a, %d %b %Y %H:%M:%S %z")
        fe.pubDate(pub_date)

    fg.rss_file(rss_file, pretty=True)

if __name__ == "__main__":
    # Get the feed URL and JSON file name from the command line
    import sys
    json_file = sys.argv[1]
    rss_file = sys.argv[2]

    generate_rss(json_file, rss_file)
