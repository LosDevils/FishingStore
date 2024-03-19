import uvicorn
from fastapi import FastAPI
from sqladmin import Admin, ModelView
from inventory.config import ProjectConfig, DataBaseConfig
from inventory.infrastructure.database.models.category import CategoryOrm
from inventory.infrastructure.database.models.characteristic import CharacteristicOrm
from inventory.infrastructure.database.models.characteristic_type import CharacteristicTypeOrm
from inventory.infrastructure.database.models.product import ProductOrm
from inventory.infrastructure.database.models.subcategory import SubCategoryOrm
from inventory.services.database import DataBaseService
from inventory.infrastructure.database.database_deploy import create_db

config = ProjectConfig(database=DataBaseConfig())
db_service = DataBaseService(config=config.database)


app = FastAPI()


admin = Admin(app, db_service.create_psycopg2_engine())


class ProductAdmin(ModelView, model=ProductOrm):
    column_list = [ProductOrm.uuid, ProductOrm.name]


class CategoryAdmin(ModelView, model=CategoryOrm):
    pass


class SubCategoryAdmin(ModelView, model=SubCategoryOrm):
    pass


class CharacteristicAdmin(ModelView, model=CharacteristicOrm):
    pass

class CharacteristicTypeAdmin(ModelView, model=CharacteristicTypeOrm):
    pass



admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(SubCategoryAdmin)
admin.add_view(CharacteristicAdmin)
admin.add_view(CharacteristicTypeAdmin)

# uvicorn inventory.app:app --reload
# uvicornuvicorn inventory.app:app


if __name__ == "__main__":
    # create_db(db_service.create_psycopg2_engine())
    uvicorn.run("app:app", reload=False)