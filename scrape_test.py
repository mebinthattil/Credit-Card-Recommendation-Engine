import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
    config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator()
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://www.hdfcbank.com/personal/pay/cards/credit-cards", config=config)

        if result.success:
            print("Raw Markdown Output:\n")
            with open ("deleteme.txt" ,"w")as f:
                f.write(result.markdown)  # The unfiltered markdown from the page
        else:
            print("Crawl failed:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())