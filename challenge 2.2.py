def linear_search_product(product_list, target_product):
    """
    Perform a linear search to find the target product in the list.

    Parameters:
    product_list (list): A list of products.
    target_product (str): The target product to search for.

    Returns:
    list: A list of indices of all occurrences of the target product, or an empty list if not found.
    """
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    
    return indices

# Example usage
products = ['Apple', 'Banana', 'Apple', 'Orange', 'Apple']
target_product = 'Apple'
result = linear_search_product(products, target_product)
print('Indices of occurrences of', target_product, ':', result)