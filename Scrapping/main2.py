from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
import uvicorn

app = FastAPI()

def fetch_and_parse():
    target = "https://news.ycombinator.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(target, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        articles = []
  
        for item in soup.find_all(class_="athing"):
            try:
                title_line = item.find(class_="titleline")
                link = title_line.find("a")
                
                articles.append({
                    "rank": item.find(class_="rank").get_text().strip("."),
                    "title": link.get_text(),
                    "url": link.get("href")
                })
            except AttributeError:
                continue
                
        return articles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/scrape")
async def get_articles():
    """
    Trigger the scraper and return the latest Hacker News articles as JSON.
    """
    data = fetch_and_parse()
    return {
        "status": "success",
        "count": len(data),
        "data": data
    }




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
