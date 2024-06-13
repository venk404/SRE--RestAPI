from fastapi import FastAPI, HTTPException,APIRouter
from pydantic import BaseModel,EmailStr,Field,field_validator
from .Models import insertstudent,get_all_students,get_student_by_Id,delete_student,Update_student
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse



class Student(BaseModel):
    name: str = Field(default=None,examples=["Ganesh Gaitonde"])
    email: EmailStr = Field(default=None, examples=["Gopalmat@gmail.com"])
    age: int = Field(default=None, examples=[0],min_length=2, max_length=2)
    phone: int = Field(default=None, examples=[0],min_length=10, max_length=10)


class StudentUpdate(BaseModel):
    name: str  | None = Field(default=None,examples=["Ganesh Gaitonde"])
    email: EmailStr | None = Field(default=None, examples=["Gopalmat@gmail.com"])
    age: str | None = Field(default=None, examples=[22],min_length=2, max_length=2)
    phone: str | None = Field(default=None, examples=[1234567890], min_length=10,max_length=10)




app = FastAPI()
version_v1 = APIRouter()
version_v2 = APIRouter()

@version_v1.post("/AddStudent",status_code=200)
async def create_student(student: Student) -> Student:
    res = jsonable_encoder(insertstudent(data=student))
    
    if res['status'] == "success":
        return JSONResponse(content={"message": "Student data added", "student_id": res["student_id"]})  

    else:
        raise HTTPException(status_code=400, detail=res['message'])



@version_v1.get("/GetAllStudents",status_code=200)
async def get_students()  -> list[Student]:
    res = jsonable_encoder(get_all_students())
    if res['status'] == "success":
        return JSONResponse(content=res['students'])
    else:
        raise HTTPException(status_code=400, detail=res['message'])
    

@version_v1.get("/GetStudent",status_code=200)
async def get_student(id:int) -> Student:
    res = get_student_by_Id(id)
    if res['status'] == "success":
        return JSONResponse(content=res['students'])
    elif res['status'] == "error":
         return {"Students":res['message']}
    else:
        raise HTTPException(status_code=400, detail=res['message'])

@version_v2.patch("/UpdateStudent",status_code=200)
async def Update(id:int,student:StudentUpdate) -> StudentUpdate:
    res = Update_student(id, student)
    if res['status'] == "success":
        return JSONResponse(content=res['students'])
    else:
        raise HTTPException(status_code=400, detail=res['message'])
    
@version_v2.delete("/DeleteStudent",status_code=200)
async def delete(id:int) -> str:
    res = delete_student(id)
    if res['status'] == "success":
        return {"Students":res}
    else:
        raise HTTPException(status_code=400, detail=res['message'])    



app.include_router(version_v1)
app.include_router(version_v2,prefix='/v2')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
   
