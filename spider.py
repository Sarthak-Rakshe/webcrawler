from html.parser import HTMLParser  # for parsing HTML
from urllib.parse import urljoin  # for joining two URLs
from urllib.request import urlopen  # for GET request
from helper import clean, get_domain, valid, contain_static


class MyHTMLParser(HTMLParser):
    """
    HTML parser to fetch URLs and show assets.
    """

    def handle_starttag(self, tag, attrs):
        """
        Override the default function to handle <a> and asset tags.
        TODO: Update this comment when asset handling is done.
        """
        for key, val in attrs:
            if key == "href":
                if contain_static(val):  # handle static files
                    print("-", val)  # show the static file
                elif tag == "a":  # handle links
                    url = urljoin(self.url, val)  # append relative path to the root path
                    url = clean(url)  # clean up URL
                    if valid(url, self.domain):
                        self.urls.append(url)  # append URL to the return list
                else:
                    pass

    def run(self, url):
        """
        Run the parser and return links on this page.
        """
        self.url = url  # save root path
        self.domain = get_domain(url)  # get and save domain
        self.urls = []  # init return list

        try:
            response = urlopen(url)  # request and get response
            html = response.read().decode("utf-8")  # read and decode response
            self.feed(html)  # parse the HTML file in string format
        except KeyboardInterrupt:  # handle Ctrl-C
            exit()
        except Exception as e:
            print(f"Unexpected failure happened and the spider escapes: {e}")

        return self.urls


class Spider:
    def __init__(self):
        self.to_visit = []
        self.visited = set()
        self.parser = MyHTMLParser()

    def crawl(self, target_url):
        target_url = clean(target_url)  # clean target_url
        self.to_visit.append(target_url)  # put target_url in to_visit list

        while self.to_visit:
            url = self.to_visit.pop(0)  # get next URL
            print("The spider is visiting:", url)
            urls = self.parser.run(url)  # parse the URL
            self.visited.add(url)  # add this visited URL to visited list

            # Add URLs from the parser to to_visit list
            # When they are not visited or already in the to_visit list
            for url in urls:
                if url not in self.visited and url not in self.to_visit:
                    self.to_visit.append(url)

        print(f"The spider has finished crawling the web at {target_url}")


if __name__ == "__main__":
    print("I don't like snakes. Don't python me directly.")
