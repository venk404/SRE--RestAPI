from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,EmailStr
from Models import insertstudent,get_all_students,get_student_by_Id,delete_student,Update_student,healthcheck
import uvicorn



class Student(BaseModel):
    name: str
    email: str
    age: float
    phone: float



app = FastAPI()

@app.post("/AddStudent",status_code=200)
async def create_student(student: Student) -> Student:
    res = insertstudent(data=student)
    if res['status'] == "success":
        return {"message": "Student data added", "student_id": res["student_id"]}
    else:
        raise HTTPException(status_code=400, detail=res['message'])



@app.get("/GetAllStudents",status_code=200)
async def get_students():
    res = get_all_students()
    if res['status'] == "success":
        return {"Students":res['students']}
    else:
        raise HTTPException(status_code=400, detail=res['message'])
    

@app.get("/GetStudent",status_code=200)
async def get_student(id:int):
    res = get_student_by_Id(id)
    if res['status'] == "success":
        return {"Students":res['students']}
    elif res['status'] == "error":
         return {"Students":res['message']}
    else:
        raise HTTPException(status_code=400, detail=res['message'])

@app.patch("/UpdateStudent",status_code=200)
async def Update(id,email):
    res = Update_student(id)
    if res['status'] == "success":
        return {"Students":res['students']}
    else:
        raise HTTPException(status_code=400, detail=res['message'])
    
@app.delete("/DeleteStudent",status_code=200)
async def delete(id:int):
    res = delete_student(id)
    if res['status'] == "success":
        return {"Students":res}
    else:
        raise HTTPException(status_code=400, detail=res['message'])

@app.get("/HealthCheck",status_code=200)
async def health():
    
    

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
