from collections import defaultdict


class InventoryAllocator:
    def make_order(self, order, warehouses):
        original_order = order.copy()
        order_tracker = defaultdict(int)
        cheapest_shipment = []

        # checking if any item values in the order are <= 0
        for key in order:
            if order[key] <= 0:
                return []

        for warehouse in warehouses:
            warehouse_result = {}
            for key in order:
                if key in warehouse['inventory']:

                    taken = 0
                    while warehouse['inventory'][key] > 0 and order[key] > 0:
                        order[key] -= 1
                        warehouse['inventory'][key] -= 1
                        taken += 1

                    order_tracker[key] += taken
                    if taken > 0:
                        warehouse_result[key] = taken

            if warehouse_result != {}:
                cheapest_shipment.append({warehouse['name']: warehouse_result})

        # checking if order was fulfilled or not
        if original_order == dict(order_tracker):
            return cheapest_shipment
        return []


