# from Fastapi import Fastapi
# from Fastapi.responses import JSONResponse

# app=FastAPI()

# @app.get("\health")
# def health_c():
#     return JSONResponse(content={"success":True})






@app.put("/tasks/{task_id}")
def create(task:tasks)
    return tasks


@app.put("/tasks/{task_id}")
def read_all():
    return task

@app.put("/tasks/{task_id}")
def update(task_id: int,new_task: Task):
    for i ,t in enumerate(tasks):

if t.id==task.id:
    tasks[i]=new_task
    return new_task

@app.put("/tasks/{task_id}")
def delete(task_id: int,new_task: Task):
    for i ,t in enumerate(tasks):
        if t.id==task_id:
             tasks[i]=new_task
    return new_task

          
