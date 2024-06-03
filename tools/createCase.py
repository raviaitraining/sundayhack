import ./mybase.py as MyBase
# Import pydentic
from pydantic import BaseModel



class CreateCase(MyBase):
    name: str = "Create Case"
    description: str = "Create a new case in the database."

    def execute(self, argument: str):
        # Execute the tool's logic
        # Create a new record in case table in postgress Database

        # Create a new case
        case = Case(customerId=1, description="This is a test case", status="Open")   
        print(case)


        pass
    def save(self, case):
        # Save the tool's state

        pass
    