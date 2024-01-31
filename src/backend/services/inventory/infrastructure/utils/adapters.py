from inventory.domain.interfaces.i_adapter import IAdapter
from inventory.domain.models.category import Category
from inventory.domain.models.characteristic import Characteristic
from inventory.domain.models.characteristic_type import CharacteristicType
from inventory.domain.models.product import Product
from inventory.domain.models.subcategory import SubCategory

from inventory.infrastructure.database.models.category import CategoryOrm
from inventory.infrastructure.database.models.characteristic import \
    CharacteristicOrm
from inventory.infrastructure.database.models.characteristic_type import \
    CharacteristicTypeOrm
from inventory.infrastructure.database.models.product import ProductOrm
from inventory.infrastructure.database.models.subcategory import SubCategoryOrm


class ProductAdapter(IAdapter):

    @classmethod
    async def to_domain_model(cls, orm_model: ProductOrm):
        return Product(uuid=orm_model.uuid,
                       name=orm_model.name,
                       price=orm_model.price,
                       quantity=orm_model.quantity,
                       description=orm_model.description,
                       picture=orm_model.picture,
                       rating=orm_model.rating,
                       discount=orm_model.discount,
                       manufacturer=orm_model.manufacturer,
                       category_id=orm_model.category_id,
                       category=orm_model.category,
                       subcategory_id=orm_model.subcategory_id,
                       subcategory=orm_model.subcategory,
                       characteristics=orm_model.characteristics)

    @classmethod
    async def to_orm_model(cls, domain_model: Product):
        return ProductOrm(uuid=domain_model.uuid,
                          name=domain_model.name,
                          price=domain_model.price,
                          quantity=domain_model.quantity,
                          description=domain_model.description,
                          picture=domain_model.picture,
                          rating=domain_model.rating,
                          discount=domain_model.discount,
                          manufacturer=domain_model.manufacturer,
                          category_id=domain_model.category_id,
                          category=domain_model.category,
                          subcategory_id=domain_model.subcategory_id,
                          subcategory=domain_model.subcategory,
                          characteristics=domain_model.characteristics)


class CategoryAdapter(IAdapter):
    @classmethod
    async def to_domain_model(cls, orm_model: CategoryOrm):
        return Category(id=orm_model.id,
                        name=orm_model.name,
                        products=orm_model.products,
                        subcategories=orm_model.subcategories)

    @classmethod
    async def to_orm_model(cls, domain_model: Category):
        return CategoryOrm(id=domain_model.id,
                           name=domain_model.name,
                           products=domain_model.products,
                           subcategories=domain_model.subcategories)


class CharacteristicAdapter(IAdapter):
    @classmethod
    async def to_domain_model(cls, orm_model: CharacteristicOrm):
        return Characteristic(id=orm_model.id,
                              value=orm_model.value,
                              product_id=orm_model.product_id,
                              characteristic_type_id=orm_model.characteristic_type_id,
                              characteristic_type=orm_model.characteristic_type)

    @classmethod
    async def to_orm_model(cls, domain_model: Characteristic):
        return CharacteristicOrm(id=domain_model.id,
                                 value=domain_model.value,
                                 product_id=domain_model.product_id,
                                 characteristic_type_id=domain_model.characteristic_type_id,
                                 characteristic_type=domain_model.characteristic_type)


class CharacteristicTypeAdapter(IAdapter):
    @classmethod
    async def to_domain_model(cls, orm_model: CharacteristicTypeOrm):
        return CharacteristicType(id=orm_model.id,
                                  characteristic_name=orm_model.characteristic_name,
                                  characteristic_instance=orm_model.characteristic_instance)

    @classmethod
    async def to_orm_model(cls, domain_model: CharacteristicType):
        return CharacteristicOrm(id=domain_model.id,
                                 characteristic_name=domain_model.characteristic_name,
                                 characteristic_instance=domain_model.characteristic_instance)


class SubCategoryAdapter(IAdapter):
    @classmethod
    async def to_domain_model(cls, orm_model: SubCategoryOrm):
        return SubCategory(id=orm_model.id,
                           name=orm_model.name,
                           characteristic_type_id=orm_model.characteristic_type_id,
                           characteristic_types=orm_model.characteristic_types,
                           category_id=orm_model.category_id,
                           category=orm_model.category,
                           products=orm_model.products)

    @classmethod
    async def to_orm_model(cls, domain_model: SubCategory):
        return SubCategoryOrm(id=domain_model.id,
                              name=domain_model.name,
                              characteristic_type_id=domain_model.characteristic_type_id,
                              characteristic_types=domain_model.characteristic_types,
                              category_id=domain_model.category_id,
                              category=domain_model.category,
                              products=domain_model.products)
