from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,EmailStr,Field
from .Models import insertstudent,get_all_students,get_student_by_Id,delete_student,Update_student
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse



class Student(BaseModel):
    name: str
    email: EmailStr
    age: float
    phone: float


class StudentUpdate(BaseModel):
    name: str  | None = Field(default=None,examples=["Ganesh Gaitonde"])
    email: EmailStr | None = Field(default=None, examples=["Gopalmat@gmail.com"])
    age: float | None = Field(default=None, examples=[0],min_length=2, max_length=3)
    phone: float | None = Field(default=None, examples=[0], min_length=10,max_length=10)





app = FastAPI()

@app.post("/AddStudent",status_code=200)
async def create_student(student: Student) -> Student:
    res = jsonable_encoder(insertstudent(data=student))
    
    if res['status'] == "success":
        return JSONResponse(content={"message": "Student data added", "student_id": res["student_id"]})  

    else:
        raise HTTPException(status_code=400, detail=res['message'])



@app.get("/GetAllStudents",status_code=200)
async def get_students()  -> list[Student]:
    res = jsonable_encoder(get_all_students())
    if res['status'] == "success":
        return JSONResponse(content=res['students'])
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
async def Update(id:int,student:StudentUpdate):
    res = Update_student(id, student)
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

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
