import scraper
import analyzer
import reporter

def main(args: list):
    scraper.RetrievePostings()
    analyzer.Analyze()
    reporter.Report()
    return 0