<div align="center">
    <a href="https://delightful-genie-8b46b0.netlify.app/"><img src="https://cdn-icons-png.flaticon.com/512/7452/7452157.png" width="18%" height="18%"></a>
    <h1>Image Drop Backend</h1>
    <p>
    A CRUD application that allows multiple users to share pictures on an online platform. The application also allows users to comment on each other post's and delete a particular post whenever they want.
    </p>
</div>

<hr>

## Technology Stack

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Render](https://render.com/)

## Installation

These steps can be followed to locally installing and setting up the project.

1. Clone the repo
2. `cd repo-name`
3. Create a virtualenv: `$ mkvirtualenv env` or `$ python -m venv env`
4. Activate env : `$ source env/bin/activate`
5. Install dependencies : `$ pip install -r requirements.txt`
6. Run project : `uvicorn main:app --reload`

## Local Setup 

These steps can be followed to locally setup the API endpoints. This is independent of the above mentioned production setup.

Currently the REST API has the following endpoints available for access:-

| Endpoint       |  Functionality            |
| :--------------| :------------------------ |
| **\login**  | Endpoint to signin an user with username and password |
| **\users**  | Endpoint to register an user. |
| **\posts**  | Endpoint to create a post. |
| **\posts\all**  | Endpoint to fetch all posts. |
| **\posts\image**  | Endpoint to upload an image. |
| **\posts\delete\{id}**  | Endpoint to delete a particular post using its id. |
| **\comments\all{post_id}**  | Endpoint to fetch all comments of a particular post. |
| **\comments\create**  | Endpoint to create a comment. |
