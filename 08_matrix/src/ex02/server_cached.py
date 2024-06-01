from typing import List, Dict
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import aioredis
import tldextract

app = FastAPI()
redis = None


class Task(BaseModel):
    status: str
    result: List[int]
    url: List[str] = []


tasks: Dict[str, Task] = {}  # to store tasks

CACHE_TIMEOUT = 60 * 60  # cache timeout in seconds (1 hour)


async def set_up_redis():
    global redis
    redis = await aioredis.create_redis_pool("redis://localhost")


@app.on_event("startup")
async def on_startup():
    await set_up_redis()


@app.post("/api/v1/tasks/")
async def create_task(urls: List[str]):
    task_id = str(uuid.uuid4())
    task = Task(status="running", result=[], url=urls)
    tasks[task_id] = task

    async with httpx.AsyncClient() as client:
        for url in urls:
            domain = tldextract.extract(url).registered_domain
            status_code = await get_cached_status_code(url)
            if status_code is None:
                try:
                    response = await client.get(url, timeout=5.0)
                    status_code = response.status_code
                    await cache_status_code(url, status_code)
                except (httpx.HTTPError, httpx.TimeoutException):
                    status_code = 0
            else:
                # Convert status code from redis cache (bytes) into int
                status_code = int(status_code)
            task.result.append(status_code)
            await increment_domain_counter(domain)

    task.status = "ready"
    return {"task_id": task_id}


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "task_id": task_id,
        "status": tasks[task_id].status,
        "result": tasks[task_id].result,
        "url": tasks[task_id].url
    }


async def get_cached_status_code(url: str) -> str:
    global redis
    return await redis.execute('get', url)


async def cache_status_code(url: str, status_code: int):
    global redis
    await redis.execute('set', url, status_code, 'ex', CACHE_TIMEOUT)


async def increment_domain_counter(domain: str):
    global redis
    await redis.execute('incr', domain)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)
