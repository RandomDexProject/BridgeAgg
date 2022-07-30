import os
from fastapi import FastAPI

import Routers


ALLOWED_HOSTS = ["*"]


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        route.operation_id = route.name  # in this case, 'read_items'


def config(
        DOMAIN: str,
        PREFIX: str):
    '''
    init of Fastapi application :)
    '''
    if DOMAIN is None:
        DOMAIN = os.getenv("DOMAIN")
        if DOMAIN is None:
            raise ValueError(
                "can't find DOMAIN var in enviromental variables ")
    if PREFIX is not None:
        root_path = PREFIX
    else:
        root_path = "/api/bridge/v1"

    print(root_path)
    app = FastAPI(
        description="Fancy 😎",
        title="BridgeAggregator-v1",
        docs_url="/docs",
        openapi_url="/openapi.json",
        root_path_in_servers=False,
        debug=True,
        root_path=root_path,
        servers=[
            {"url": f'{DOMAIN}{root_path}', "description": "v1"}
        ],
    )
    app.include_router(Routers.routers)
    use_route_names_as_operation_ids(
        app)
        
    return app
