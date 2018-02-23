# Graphql-django


### Create VirtualEnv
```shell
virtualenv (name)

```

### Active virtualEnv
```shell
source (name)/bin/activate

```

### Install packages
```shell
pip install -r requirements.txt

```


### Run project

```python
python  manage.py runserver

```

# Users

### CreateUser

```json

mutation {
  createUser(username: "carloske", email: "carlskE@git.com", password: "122m11++111") {
    user {
      id
      email
      username
    }
  }
}

```


### All users

```json

query {
  users {
    id
    email
  }
}

```

# Ingredients


### All ingredients

```json

query {
  allIngredients {
    id
    name
    category {
      id
    }
  }
}

```

