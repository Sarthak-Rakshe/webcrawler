from urllib.parse import urlparse  # for domain extraction
import re  # for regular expressions


def clean(url):
    """
    Clean up URL by:
        - Ensuring it starts with "http://" or "https://"
        - Removing element jumping (fragment identifiers)
        - Removing trailing '/'
    @input:
        url (str): The URL to be processed
    @output:
        url (str): The cleaned URL
    """
    if not url:
        return ""

    # Deal with "http(s)://"
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    # Deal with fragment identifiers ("#")
    url = url.split('#')[0]

    # Remove trailing '/'
    if url.endswith('/'):
        url = url[:-1]

    return url


def get_domain(url):
    """
    Get the domain of a given URL
    @input:
        url (str): The URL to be processed
    @output:
        domain (str): The domain of the URL
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc


def valid(url, domain):
    """
    Check if the given URL is valid (e.g., within a specific domain)
    @input:
        url (str): The URL to be checked
        domain (str): The domain to be matched against
    @output:
        valid (bool): True if the URL is valid, False otherwise
    """
    return bool(re.match(rf'^https?://([\w-]*\.)?{re.escape(domain)}.*$', url, re.IGNORECASE))


def contain_static(val):
    """
    Check if a given value (relative path or URL) contains static files
    @input:
        val (str): Relative path or URL
    @output:
        contain (bool): True if the value contains a static file, False otherwise
    """
    return bool(re.match(r'^.*\.(jpg|jpeg|gif|png|css|js|ico|xml|rss|txt).*$', val, re.IGNORECASE))


if __name__ == "__main__":
    print("I don't like snakes. Don't python me directly.")
