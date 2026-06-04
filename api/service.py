import bentoml
import pandas as pd
from pydantic import BaseModel, Field


MODEL_TAG = "building_energy_model:buwe3fc7d6v7ldef"

model_ref = bentoml.sklearn.get(MODEL_TAG)
model = model_ref.load_model()

feature_names = model_ref.custom_objects["feature_names"]


class BuildingInput(BaseModel):
    BuildingType: str
    PrimaryPropertyType: str

    Latitude: float = Field(..., ge=47.0, le=48.0)
    Longitude: float = Field(..., ge=-123.0, le=-121.0)

    NumberofBuildings: float = Field(..., ge=1)
    NumberofFloors: float = Field(..., ge=0)

    PropertyGFATotal: float = Field(..., gt=0)
    PropertyGFAParking: float = Field(..., ge=0)

    LargestPropertyUseType: str
    LargestPropertyUseTypeGFA: float = Field(..., gt=0)

    SecondLargestPropertyUseType: str
    SecondLargestPropertyUseTypeGFA: float = Field(..., ge=0)

    Agebuilding: float = Field(..., ge=0, le=150)


@bentoml.service
class BuildingEnergyService:

    @bentoml.api
    def predict_energy(self, input_data: BuildingInput) -> dict:
        input_df = pd.DataFrame([input_data.model_dump()])

        input_df = input_df[feature_names]

        prediction = model.predict(input_df)[0]

        return {
            "prediction_SiteEnergyUse_kBtu": float(prediction),
            "model": MODEL_TAG
        }