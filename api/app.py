from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
from litestar import Litestar, get
from litestar.config.cors import CORSConfig
from litestar.openapi import OpenAPIConfig
from litestar.openapi.spec import Components, SecurityScheme, Tag
from litestar.openapi.plugins import ScalarRenderPlugin, SwaggerRenderPlugin
from litestar.response.redirect import ASGIRedirectResponse
from sqlalchemy.ext.asyncio import create_async_engine

from routes.v1.router import V1Router
from routes.aai.router import AAIRouter
from models import User


@asynccontextmanager
async def db_connection(app: Litestar) -> AsyncGenerator:
    engine = getattr(app.state, "engine", None)
    if engine is None:
        engine = create_async_engine("sqlite+aiosqlite:///users.db", echo=True)
        app.state.engine = engine

    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    
    try:
        yield
    finally:
        await engine.dispose()
        
@get('/', include_in_schema=False)
async def root2schema() -> ASGIRedirectResponse:
    return ASGIRedirectResponse('/schema')

cors_config = CORSConfig(
    allow_origins=['*'],
    allow_methods=['GET', 'POST']
)

app = Litestar(
    lifespan=[db_connection],
    route_handlers=[root2schema, AAIRouter, V1Router],
    cors_config=cors_config,
    openapi_config=OpenAPIConfig(
        title='DILS API',
        description='API to test cryptography concepts',
        version="1.0.0",
        security=[{"BearerToken": []}],
        components=Components(
            security_schemes={
                "BearerToken": SecurityScheme(
                    type="http",
                    scheme="bearer",
                )
            },
        ),
        render_plugins=[SwaggerRenderPlugin(), ScalarRenderPlugin()],
    ),
)