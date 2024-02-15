from fastapi import FastAPI
from starlette_admin.contrib.sqla import Admin, ModelView

from inventory.config import ProjectConfig, DataBaseConfig
from inventory.infrastructure.database.models.product import ProductOrm
from inventory.services.database import DataBaseService

app = FastAPI()

config = ProjectConfig(database=DataBaseConfig())
db_service = DataBaseService(config=config.database)

# Create admin
admin = Admin(db_service.create_engine(), title="Example: SQLAlchemy")
# Add view
admin.add_view(ModelView(ProductOrm))

# Mount admin to your app
admin.mount_to(app)

# uvicorn inventory.app:app uvicorn app:app
