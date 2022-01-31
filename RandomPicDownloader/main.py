from icrawler.builtin import GoogleImageCrawler
google_crawler = GoogleImageCrawler(storage={'root_dir':'...\Image'})
count = int(input('How much image do u want parse?'))
count1 = str(input('Enter what do u want parse?'))
google_crawler.crawl(keyword=count1, max_num=count)
