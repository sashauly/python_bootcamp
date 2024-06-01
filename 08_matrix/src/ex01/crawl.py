import asyncio
import httpx
from typing import List, Dict


# Function to create a new task and submit URLs
async def submit_urls_to_task(urls: List[str]) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8888/api/v1/tasks/",
                                     json=urls)
        response_json = response.json()
        return response_json


# Function to continuously poll the task's status
async def check_task_status(task_id: str) -> Dict:
    async with httpx.AsyncClient() as client:
        while True:
            response = await client.get(f"http://localhost:8888/api/v1/tasks/{task_id}")
            response_json = response.json()
            if response_json["status"] == "ready":
                return response_json
            await asyncio.sleep(1)


# Function to print the task results
async def print_task_results(task_result: Dict) -> None:
    for status, url in zip(task_result["result"], task_result["url"]):
        print(f"URL: {url}, Status Code: {status}")


# The main function to run everything
async def main() -> None:
    urls_to_check = ["http://example.com", "http://example.org"]
    submitted_task = await submit_urls_to_task(urls_to_check)
    task_id = submitted_task["task_id"]

    completed_task = await check_task_status(task_id)
    await print_task_results(completed_task)

# Run the main function if this is the main script
if __name__ == "__main__":
    asyncio.run(main())
