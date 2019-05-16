from inventory_allocator import InventoryAllocator
import pytest


@pytest.mark.parametrize("order,warehouses,expected", [({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}],
                                                        [{'owd': {'apple': 1}}]),
                                                       ({'pear': 5}, [{'name': 'owd', 'inventory': {'pear': 10}}],
                                                        [{'owd': {'pear': 5}}]),
                                                       ({'apple': 10}, [{'name': 'owd', 'inventory': {'pear': 100}}, {'name': 'dm', 'inventory': {'apple': 100}}],
                                                        [{'dm': {'apple': 10}}])
                                                       ])
def test_enough_inventory_case(order, warehouses, expected):
    assert expected == InventoryAllocator().make_order(order, warehouses)


@pytest.mark.parametrize("order,warehouses,expected", [({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 0}}],
                                                        []),
                                                       ({'pear': 10}, [{'name': 'owd', 'inventory': {'pear': 5}}],
                                                        []),
                                                       ({'apple': 20}, [{'name': 'owd', 'inventory': {'pear': 10}}],
                                                        []),
                                                       ({'pear': 30}, [{'name': 'owd', 'inventory': {'pear': 29}}],
                                                        []),
                                                       ({'apple': 0}, [{'name': 'owd', 'inventory': {'apple': 5}}],
                                                        []),
                                                       ({'pear': 0}, [{'name': 'owd', 'inventory': {'pear': 0}}],
                                                        []),
                                                       ])
def test_not_enough_inventory_case(order, warehouses, expected):
    assert expected == InventoryAllocator().make_order(order, warehouses)


@pytest.mark.parametrize("order,warehouses,expected", [({'apple': 10}, [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}],
                                                        [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]),
                                                       ({'pear': 3}, [{'name': 'owd', 'inventory': {'pear': 1}}, {'name': 'dm', 'inventory': {'pear': 2}}],
                                                        [{'owd': {'pear': 1}}, {'dm': {'pear': 2}}]),
                                                       ({'apple': 100}, [{'name': 'owd', 'inventory': {'apple': 99}}, {'name': 'dm', 'inventory': {'apple': 1}}],
                                                        [{'owd': {'apple': 99}}, {'dm': {'apple': 1}}]),
                                                       ({'apple': 1000, 'pear': 500}, [{'name': 'owd', 'inventory': {'apple': 1000}}, {'name': 'dm', 'inventory': {'pear': 500}}],
                                                        [{'owd': {'apple': 1000}}, {'dm': {'pear': 500}}]),
                                                       ({'apple': 200, 'pear': 100}, [{'name': 'owd', 'inventory': {'apple': 100, 'pear': 75}}, {'name': 'dm', 'inventory': {'pear': 25, 'apple': 100}}],
                                                        [{'owd': {'apple': 100, 'pear': 75}}, {'dm': {'pear': 25, 'apple': 100}}]),
                                                       ({'apple': 200, 'pear': 100}, [{'name': 'dm', 'inventory': {'pear': 100, 'apple': 100}}, {'name': 'aws', 'inventory': {'pear': 100, 'apple': 200}}],
                                                        [{'dm': {'apple': 100, 'pear': 100}}, {'aws': {'apple': 100}}])
                                                       ])
def test_split_inventory_case(order, warehouses, expected):
    assert expected == InventoryAllocator().make_order(order, warehouses)


@pytest.mark.parametrize("order,warehouses,expected", [({'apple': 0}, [{'name': 'owd', 'inventory': {'apple': 5}}],
                                                        []),
                                                       ({'pear': 0}, [{'name': 'owd', 'inventory': {'pear': 0}}],
                                                        [])
                                                       ])
def test_no_order_or_inventory(order, warehouses, expected):
    assert expected == InventoryAllocator().make_order(order, warehouses)


@pytest.mark.parametrize("order,warehouses,expected", [({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': -1}}],
                                                        [])
                                                       ])
def test_negative_inventory_case(order, warehouses, expected):
    assert expected == InventoryAllocator().make_order(order, warehouses)


@pytest.mark.parametrize("order,warehouses,expected", [({'apple': -1}, [{'name': 'owd', 'inventory': {'apple': 1}}],
                                                        [])
                                                       ])
def test_negative_order_case(order, warehouses, expected):
    assert expected == InventoryAllocator().make_order(order, warehouses)
