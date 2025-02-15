import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Add project root to sys.path (one level above 'alembic')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your models and database URL
from models import Base  # Make sure this is your SQLAlchemy Base
from database import DATABASE_URL  # Your DB URL from database.py

config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Assign your model metadata to target_metadata
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

