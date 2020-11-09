# Async SQLAlchemy Databases

Alongside <a href="https://github.com/encode/databases" class="external-link" target="_blank">`encode/databases`</a> you can also use native SQLAlchemy asyncio support.

**THIS SUPPORT IS CURRENTLY IN BETA STAGE, DO NOT USE IT IN PRODUCTION!**

Since SQLite is currently not supported we'll use **PostgreSQL**, which does require you to have a running image of PostgreSQL.

This tutorial also specifically expects `SQLAlchemy >= 1.4`, since it is currently in beta you will need to specify the version since pypi automatically will not install it.

!!! tip
    We strongly suggest going through the non async tutorial first ([SQL (Relational) Databases](../tutorial/sql-databases.md){.internal-link target=_blank}), since this tutorial will mostly cover the async parts of SQLAlchemy.

## File structure

For these examples, let's say you have a directory named `my_super_project` that contains a sub-directory called `sql_app` with a structure like this:

```
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```

The file `__init__.py` is just an empty file, but it tells Python that `sql_app` with all its modules (Python files) is a package.

Now let's see what each file/module does.
    
## Create the `SQLAlchemy` parts¶

* Import `create_async_engine`.
* Create a `PostgreSQL` url, notice how we add **asyncpg** to the string, this is the postgres async client.
* Create an async engine with the Postgres url.

```Python hl_lines="1  4  6"
{!../../../docs_src/async_sql_databases/sql_app/database.py!}
```

## Create models and schemas

This step in unchanged from the non-async way, so we'll just copy the code in, if you want more detail on how it works ([SQL (Relational) Databases](../tutorial/sql-databases.md){.internal-link target=_blank}).

```Python
{!../../../docs_src/async_sql_databases/sql_app/models.py!}
```

```Python
{!../../../docs_src/async_sql_databases/sql_app/schemas.py!}
```

## CRUD utils

```Python
{!../../../docs_src/async_sql_databases/sql_app/crud.py!}
```

!!! Note
    Notice that as we communicate with the database using `await`, the *function* is declared with `async`.

## Main FastAPI app

```Python
{!../../../docs_src/async_sql_databases/sql_app/main.py!}
```

## More info

You can read more about <a href="https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html" class="external-link" target="_blank">`encode/databases` at its Docs page</a>.
