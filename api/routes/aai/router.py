from litestar import Router
from routes.aai.controllers.basic import BasicController


AAIRouter = Router(
    path="/aai",
    tags=["AAI"],   
    route_handlers=[
        BasicController
    ]
)