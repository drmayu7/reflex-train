page_registry = {}

def register_page(route: str):
    """
    Decorator to register a page function with a specific route.

    Args:
        route (str): The URL path for the page.

    Returns:
        function: The decorator function.
    """

    def decorator(func):
        page_registry[route] = func
        return func

    return decorator


# Import all page modules to ensure they are registered
from . import about
from . import contact
from . import pricing
