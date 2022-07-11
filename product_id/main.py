from hashlib import sha256
from pydantic import BaseModel, Field

class PacBioWell(BaseModel):

    run_name: str
    well_label: str
    tags: str = Field(default=None)

    def get_json(self):
        strs = []
        for key, value in self.dict().items():
            if value is not None:
                strs.append(f"\"{key}\":\"{value}\"")
                
        return "{" + ",".join(strs) + "}" 
    
    def hash_product_id(self):
        return sha256(self.get_json().encode()).hexdigest()

