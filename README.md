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

```

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

```

query {
  users {
    id
    email
  }
}

```

# Ingredients


### All ingredients

```

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

