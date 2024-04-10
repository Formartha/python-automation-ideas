from pydantic import BaseModel
from typing import Optional
from faker import Faker

fake = Faker()


from pydantic import BaseModel
from typing import Optional
from faker import Faker
from typing import get_type_hints

fake = Faker()


class ApiModel(BaseModel):
    name: str
    age: int
    is_active: bool
    email: Optional[str] = None

    @classmethod
    def generate_random(cls):
        random_data = {}
        type_hints = get_type_hints(cls)
        for field, field_type in type_hints.items():
            if field_type == str:
                random_data[field] = fake.name()
            elif field_type == int:
                random_data[field] = fake.random_int(min=18, max=65)
            elif field_type == bool:
                random_data[field] = fake.boolean()
            # Add more conditions for other types as needed

        return cls(**random_data)


# Generate a random instance of ApiModel
random_model = ApiModel.generate_random()

# Get the JSON payload
json_payload = random_model.dict()
print(json_payload)
