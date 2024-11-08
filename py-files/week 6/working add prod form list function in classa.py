def add_products_from_list(self, product_data):
    """Use lambda and map to add products from a nested list."""
    # Lambda function to create the correct product type
    create_product = lambda p: (FoodProduct(p[0], p[1], p[2], p[3], p[4], p[5])
                                if len(p) == 6
                                else Product(p[0], p[1], p[2]))

    # Use map to apply the lambda function and add products
    list(map(lambda p: self.add_product(create_product(p)), product_data))