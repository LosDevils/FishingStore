from inventory.infrastructure.database.models.category import CategoryOrm
from inventory.infrastructure.database.models.characteristic import \
    CharacteristicOrm
from inventory.infrastructure.database.models.characteristic_type import \
    CharacteristicTypeOrm
from inventory.infrastructure.database.models.product import ProductOrm
from inventory.infrastructure.database.models.subcategory import SubCategoryOrm
from inventory.infrastructure.database.repository import Repository
from inventory.infrastructure.utils.adapters import ProductAdapter, \
    CategoryAdapter, CharacteristicAdapter, CharacteristicTypeAdapter, \
    SubCategoryAdapter


class ProductRepository(Repository):
    model = ProductOrm
    adapter = ProductAdapter


class CategoryRepository(Repository):
    model = CategoryOrm
    adapter = CategoryAdapter


class CharacteristicRepository(Repository):
    model = CharacteristicOrm
    adapter = CharacteristicAdapter


class CharacteristicTypeRepository(Repository):
    model = CharacteristicTypeOrm
    adapter = CharacteristicTypeAdapter


class SubCategoryRepository(Repository):
    model = SubCategoryOrm
    adapter = SubCategoryAdapter
