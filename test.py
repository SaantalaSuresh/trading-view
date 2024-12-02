from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TradingView Chart</title>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    </head>
    <body>
        <div id="tradingview_widget"></div>

        <script>
            new TradingView.widget({
                container_id: "tradingview_widget",
                width: "100%",
                height: "500",
                symbol: "NASDAQ:AAPL", // Change to your desired symbol
                interval: "D",
                timezone: "Etc/UTC",
                theme: "light",
                style: "1",
                locale: "en",
                toolbar_bg: "#f1f3f6",
                enable_publishing: false,
                allow_symbol_change: true,
                details: true,
                hotlist: true,
                calendar: true,
                studies: [],
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
