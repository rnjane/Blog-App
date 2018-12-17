## Blog-App

A django API for a blogging app

# Description

As an admin
I log to the system.
I create an articcle;
I can also view the article
I can choose to edit when necessary
I can chose to delete when necessary
I can also to create/edit/delete categories

For other public users
They can view the articles and they do not have to login.

## Documentation

1. Login - provides user login.
`POST login/` sample body
`{
    "username": "rnjane", "password": "faraday2"
}`

2. Categories - Provides for creating a category and viewing all categories. Requires authentication.
`POST category/` sample body
`{
    "name": "sample caegory"
}`

`GET category` - returns all categories added.

3. Category details - Provides for edit and delete for a category.
`PATCH category/<int:pk>` - Edit a category, whose PK is specified. sample body:
{
    "name": "new name here"
}
`DELETE category/<int:pk>` - Deletes a category whose PK is provided.

4. Create article - create an article
`POST create-article/` sample body:
{
    "title": "testarticle",
    "content": "sample content goes here", 
    "category": "writing"
} - Also, ensure you specify an image for the article.

5. Artciles - View all articles
`GET articles/` - no authentication. returns all created articles.

6. Article Details - View a single article, edit and delete.
`GET article/<int:pk>` - returns  an article whose PK is specified
`DELETE article/<int:pk>` - deletes an article whose PK is specified
`PATCH article/<int:pk>` - Edits an article whose pk is specified. Sample body:
{
    "title": "new title"
    "content: "new content"
}
### Dependencies

- Python3

### Getting Started

1. Clone the repository at https://github.com/rnjane/Blog-App.git
2. Create a virtualenvironment - `virtualenv -p python3 venv`. Activate the virtualenv.
3. CD into `Blog-App`. Install the project requirements `pip install -r requirements.txt`
4. Run migrations `python manage.py migrate`
5. Create a user `python manage.py createsuperuser`
6. Run the application `python manage.py runserver`
7. Access the API endpoints using Postman. Login with the superuser credentials used.


## Testing

After setting up the application, run `python manage.py test`