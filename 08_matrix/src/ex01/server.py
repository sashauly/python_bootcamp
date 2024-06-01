from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel
from typing import Dict, List
import uuid

app = FastAPI()


# Define the Task model
class Task(BaseModel):
    status: str
    result: List[int]
    url: List[str] = []


# Initialize the tasks dictionary
tasks: Dict[str, Task] = {}


# Define the task creation endpoint
@app.post("/api/v1/tasks/")
async def create_task(urls: List[str]) -> Dict[str, str]:
    # Generate a unique task_id
    task_id = str(uuid.uuid4())
    # Create a new task with initial status and empty results
    task = Task(status="running", result=[], url=urls)
    # Store the new task in the tasks dictionary
    tasks[task_id] = task

    # Make http requests to the provided URLs
    async with httpx.AsyncClient() as client:
        for url in urls:
            try:
                response = await client.get(url)
                task.result.append(response.status_code)
            except httpx.HTTPError:
                task.result.append(0)

    # Update the task's status to 'ready'
    task.status = "ready"
    return {"task_id": task_id}


# Define the task status endpoint
@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: str) -> Dict:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "task_id": task_id,
        "status": tasks[task_id].status,
        "result": tasks[task_id].result,
        "url": tasks[task_id].url
    }


# Run the server if this file is run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)
