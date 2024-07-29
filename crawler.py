import sys  # for handling arguments
from spider import Spider
from test import Test

HELPMSG = ("----------------- Usage ----------------\n"
           "1. Crawl a website:\n"
           "    python crawler.py -c [target_website]\n"
           "2. Run tests:\n"
           "    python crawler.py -test\n"
           "3. Help:\n"
           "    python crawler.py -help\n"
           "----------------------------------------\n")


def print_help(warning=False):
    if warning:
        print("---------------- Warning ---------------")
        print("Arguments unrecognized, please check usage")
    else:
        print("----------------------------------------")
        print("Welcome to this web crawler coded by Kai")
    print(HELPMSG)


def main():
    # Fetch the arguments; the first element in sys.argv is this python file itself - so ignore
    args = sys.argv[1:]

    # Execute function depending on arguments
    if len(args) == 1:
        if args[0] == "-test":      # test
            test = Test()
            test.test_all()
        elif args[0] == "-help":    # help
            print_help()
        else:
            print_help(True)
    elif len(args) == 2:
        if args[0] == "-c":         # crawl
            url = args[1]
            print("[crawler.py] start crawling")
            spider = Spider()
            try:
                spider.crawl(url)
                print("[crawler.py] crawling done")
            except Exception as e:
                print(f"[crawler.py] an error occurred: {e}")
        else:
            print_help(True)
    else:
        print_help(True)


if __name__ == "__main__":
    main()
