"""
Async SQLAlchemy engine and session factory.
Pattern is identical to what was used in the URL shortener — async engine,
async_sessionmaker, get_db dependency injected via FastAPI Depends().
"""
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings


# ── Declarative Base ──────────────────────────────────────────────────────────
# Every ORM model inherits from this Base.
# SQLAlchemy uses it to track all table definitions.
class Base(DeclarativeBase):
    pass


# ── Async Engine ──────────────────────────────────────────────────────────────
engine = create_async_engine(
    settings.database_url,
    echo=False,       # Set True during development to see SQL in the console
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,   # Test each connection before use (handles DB restarts)
)


# ── Session Factory ───────────────────────────────────────────────────────────
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    # expire_on_commit=False: after db.commit(), objects keep their attribute values.
    # Without this, accessing doc.id after a commit would trigger another DB query.
)


# ── FastAPI Dependency ────────────────────────────────────────────────────────
async def get_db() -> AsyncSession:
    """
    Yields an AsyncSession for one request, then closes it automatically.
    Rolls back on any unhandled exception to keep the DB state clean.

    Usage in routes:
        async def my_route(db: AsyncSession = Depends(get_db)):
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise