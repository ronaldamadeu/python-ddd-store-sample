from src.domains.product import Product

def test_should_creaete_product():
    product: Product = Product(
        name="PS5", 
        description="Console ps5 slim", 
        price=499
    )
    
    assert product.name == "PS5"
    assert product.description == "Console ps5 slim"
    assert product.price == 499.0