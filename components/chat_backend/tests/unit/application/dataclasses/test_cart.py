def test__find_position(cart, product_1, cart_position_1):
    cart_position_1.product = product_1

    cart.positions = [cart_position_1]

    found = cart.find_position(product_1)
    assert found == cart_position_1


def test__find_position__not_found(cart, product_2, product_1, cart_position_1):
    cart_position_1.product = product_2

    cart.positions = [cart_position_1]

    found = cart.find_position(product_1)
    assert found is None
