from typing import Any, Dict, Type
import pandas as pd
from pydantic import BaseModel, ValidationError

def validate_dataframe(df: pd.DataFrame, schema: Type[BaseModel]) -> Dict[str, Any]:
    errors = []
    valid = 0
    invalid = 0
    for i, row in df.iterrows():
        try:
            schema.model_validate(row.to_dict())
            valid += 1
        except ValidationError as e:
            invalid += 1
            for err in e.errors():
                errors.append({"row": i+1, "field": err["loc"][0], "msg": err["msg"]})
    return {"summary": {"valid": valid, "invalid": invalid}, "errors": errors}
