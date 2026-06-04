curl -X POST "http://localhost:3000/predict_energy" \
-H "Content-Type: application/json" \
-d '{
  "input_data": {
    "BuildingType": "NonResidential",
    "PrimaryPropertyType": "Small- and Mid-Sized Office",
    "Latitude": 47.61,
    "Longitude": -122.33,
    "NumberofBuildings": 1,
    "NumberofFloors": 3,
    "PropertyGFATotal": 50000,
    "PropertyGFAParking": 0,
    "LargestPropertyUseType": "Office",
    "LargestPropertyUseTypeGFA": 45000,
    "SecondLargestPropertyUseType": "None",
    "SecondLargestPropertyUseTypeGFA": 0,
    "Agebuilding": 40
  }
}'