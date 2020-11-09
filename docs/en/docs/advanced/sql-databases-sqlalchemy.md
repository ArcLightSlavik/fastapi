# Async SQLAlchemy Databases

Alongside <a href="https://github.com/encode/databases" class="external-link" target="_blank">`encode/databases`</a> you can also use native SQLAlchemy asyncio support.

!!! warning
    SQLAlchemy asyncio support is currently in beta and is not stable.
    
    This tutorial expects SQLAlchemy >= 1.4.


!!! tip
    We strongly suggest going through the non async tutorial first ([SQL (Relational) Databases](../tutorial/sql-databases.md){.internal-link target=_blank}), since this tutorial only cover the async parts of SQLAlchemy.

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
* Create a url for database URL for SQLAlchemy.
* Create an async engine with the database url.

```Python hl_lines="1  4  7"
{!../../../docs_src/async_sql_databases/sql_app/database.py!}
```

!!! tip
    If your using postgresql you need to append `asyncpg` to the database string, as shown above.
    
    You will also need to `pip install asyncpg`

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

## Check it

You can copy this code as is, and see the docs at <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

There you can see all your API documented and interact with it:

<img src="/img/tutorial/sql-databases/image01.png">


## More info

You can read more about <a href="https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html" class="external-link" target="_blank">`encode/databases` at its Docs page</a>.
