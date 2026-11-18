
import os
from datetime import datetime
from longbridge.openapi import Config, ContentContext


def _format_articles(items: list[dict]):
    out = ""
    for item in items:
        out += f"### {item.title}\n"
        if item.description:
            out += f"{item.description}\n"
        out += f"Link: {item.url}\n"
        out += "\n"
    return out


def get_news_longbridge(ticker: str,
                        start_date: str,
                        end_date: str):
    config = Config.from_apikey(
        os.getenv("LONGBRIDGE_APP_KEY"),
        os.getenv("LONGBRIDGE_APP_SECRET"),
        os.getenv("LONGBRIDGE_ACCESS_TOKEN"))

    ctx = ContentContext(config)
    items = ctx.news(ticker + ".US")
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    if items:
        out = f"## {ticker} News, from {start_date} to {end_date}:\n\n{_format_articles(items)}"
    else:
        out = f"No news found for {ticker} between {start_date} and {end_date}"

    #print("get_news_longbridge:", out)
    return out

