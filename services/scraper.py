
import asyncio
from curl_cffi.requests import AsyncSession


class PriceScraper:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    async def fetch_page(self, url: str) -> str | None:
        """Скачивает одну страницу c имитацией браузера через curl_cffi."""
        async with AsyncSession(impersonate="chrome") as session:
            try:
                response = await session.get(url, timeout=self.timeout)
                
                if response.status_code != 200:
                    print(f"[!] Ошибка: сервер вернул статус {response.status_code} для {url}")
                    return None

                return response.text

            except Exception as e:
                print(f"[!] Ошибка сети при запросе к {url}: {e}")
                return None

    async def fetch_all(self, urls: list[str]) -> dict[str, str | None]:
        """Параллельно скачивает список URL c защитой пачки через return_exceptions=True."""
        async with AsyncSession(impersonate="chrome") as session:
            # Создаем задачи для каждого URL
            tasks = [session.get(url, timeout=self.timeout) for url in urls]
            
            # Запускаем всё разом, защищаясь от падения всей пачки
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            results = {}
            for url, response in zip(urls, responses):
                if isinstance(response, Exception):
                    print(f"[!] Задача для {url} упала c исключением: {response}")
                    results[url] = None
                    continue
                
                if response.status_code == 200:
                    results[url] = response.text
                else:
                    results[url] = None
                    
            return results
        