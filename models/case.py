# create case model from pydantic
# import postgress client sqlalchemy just to save record in database
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL(
    drivername="postgresql",
    username="doadmin",
    password="AVNS_bMGFjnoQzyxk96lM7wH",
    host="ravipost-do-user-721507-0.b.db.ondigitalocean.com",
    port="25060",
    database="defaultdb",
    sslmode="require"
)

engine = create_engine(url)


class Case(BaseModel):
    id: int
    customerId: int
    description: str
    status: str