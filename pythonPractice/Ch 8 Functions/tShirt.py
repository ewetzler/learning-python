def makeShirt(size='large', text='I love Python'):
    """Display a message about the size and text for a shirt"""
    print(f"\nYou ordered a {size.lower()} shirt with the following message:")
    print(f"\t{text}")

makeShirt()
makeShirt(size='medium')
makeShirt('small', 'Dump Trump')