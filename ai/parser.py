from pydantic import BaseModel



class CropAdvice(BaseModel):

    crop_name:str

    fertilizer_plan:str

    watering_schedule:str

    pest_risk:str

    govt_scheme_tip:str