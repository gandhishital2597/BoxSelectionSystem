from itertools import permutations

from .models import Box


def can_fit(product_dimensions, box_dimensions):
    """
    Check whether a product can fit inside a box
    in any possible orientation.
    """

    for dimensions in permutations(product_dimensions):

        if all(
            dimensions[i] <= box_dimensions[i]
            for i in range(3)
        ):
            return True

    return False


def recommend_box(order):

    items = order.items.select_related('product')

    total_weight = 0
    total_volume = 0

    products = []

    # Calculate total weight and volume
    for item in items:

        product = item.product

        total_weight += product.weight * item.quantity

        product_volume = (
            product.length *
            product.width *
            product.height
        )

        total_volume += product_volume * item.quantity

        # Add every product according to quantity
        for _ in range(item.quantity):
            products.append(product)

    suitable_boxes = []

    # Check all available boxes
    for box in Box.objects.all():

        # 1. Check weight
        if box.max_weight < total_weight:
            continue

        # 2. Check total volume
        box_volume = (
            box.length *
            box.width *
            box.height
        )

        if box_volume < total_volume:
            continue

        # 3. Check dimensions
        box_dimensions = (
            box.length,
            box.width,
            box.height
        )

        all_products_fit = True

        for product in products:

            product_dimensions = (
                product.length,
                product.width,
                product.height
            )

            if not can_fit(
                product_dimensions,
                box_dimensions
            ):
                all_products_fit = False
                break

        if all_products_fit:
            suitable_boxes.append(box)

    # No box found
    if not suitable_boxes:
        return None

    # Sort by cost
    suitable_boxes.sort(
        key=lambda box: box.cost
    )

    # Return cheapest suitable box
    return suitable_boxes[0]
