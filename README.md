# SoftDesk
 
SoftDesk Support is designed to help businesses manage and track technical issues efficiently. The API is built with Django and Django REST Framework, following best practices for security, data protection, and energy-efficient coding.

## Features

- **User Authentication and Authorization :** The API uses JSON Web Tokens (JWT) for user authentication and sets access permissions to resources by user group.
- **Data Protection :** Complies with GDPR regulations to ensure user data protection and privacy.
- **Green Code Practices :** Implements optimized and simplified code to promote energy efficiency and reduce server overconsumption.

## How to run
Once the code has been downloaded, go to the project directory and enter the following commands in terminal

*install all the depedencies with pipenv :*
```
pipenv install
```
*make migrations :*
```
python manage.py makemigrations
python manage.py migrate
```
*run the code :*
```
python manage.py runserver
```

> [!NOTE]
> The commands above are for Windows use. Go to the official [Python documentation](https://docs.python.org/3/tutorial/venv.html) for MacOS or Unix usage.
<br><br>

## Endpoints

Here is a list of all available endpoints in the API and their descriptions:

### Authentication
| **Endpoint**                             | **Method**      | **Description**                                                   |
|------------------------------------------|-----------------|-------------------------------------------------------------------|
| **/api/connection/**                     | POST            | *Authenticate.*                                                   |
| **/api/refresh-token/**                  | POST            | *Refresh token.*                                                  |

### Users
| **Endpoint**                             | **Method**      | **Description**                                                   |
|------------------------------------------|-----------------|-------------------------------------------------------------------|
| **/api/users/**                          | GET             | *Retrieve a list of all users.*                                   |
| **/api/users/**                          | POST            | *Create a new user.*                                              |
| **/api/users/{user_id}/**                | GET             | *Retrieve details of a specific user.*                            |
| **/api/users/{user_id}/**                | PUT             | *Update a specific user.*                                         |
| **/api/users/{user_id}/**                | DELETE          | *Delete a specific user.*                                         |

### Projects
| **Endpoint**                             | **Method**      | **Description**                                                   |
|------------------------------------------|-----------------|-------------------------------------------------------------------|
| **/api/projects/**                       | GET             | *Retrieve a list of all projects.*                                |
| **/api/projects/**                       | POST            | *Create a new project.*                                           |
| **/api/projects/{project_id}/**          | GET             | *Retrieve details of a specific project.*                         |
| **/api/projects/{project_id}/**          | PUT             | *Update a specific project.*                                      |
| **/api/projects/{project_id}/**          | DELETE          | *Delete a specific project.*                                      |

### Issues
| **Endpoint**                             | **Method**      | **Description**                                                   |
|------------------------------------------|-----------------|-------------------------------------------------------------------|
| **/api/projects/{project_id}/issues/**   | GET             | *Retrieve a list of all issues for a specific project.*           |
| **/api/projects/{project_id}/issues/**   | POST            | *Create a new issue in a specific project.*                       |
| **/api/projects/{project_id}/issues/{issue_id}/** | GET | *Retrieve details of a specific issue.*                           |
| **/api/projects/{project_id}/issues/{issue_id}/** | PUT | *Update a specific issue.*                                        |
| **/api/projects/{project_id}/issues/{issue_id}/** | DELETE | *Delete a specific issue.*                                        |

### Comments
| **Endpoint**                             | **Method**      | **Description**                                                   |
|------------------------------------------|-----------------|-------------------------------------------------------------------|
| **/api/projects/{project_id}/issues/{issue_id}/comments/** | GET  | *Retrieve a list of all comments for a specific issue.*           |
| **/api/projects/{project_id}/issues/{issue_id}/comments/** | POST | *Create a new comment on a specific issue.*                       |
| **/api/projects/{project_id}/issues/{issue_id}/comments/{comment_id}/** | GET | *Retrieve details of a specific comment.*                        |
| **/api/projects/{project_id}/issues/{issue_id}/comments/{comment_id}/** | PUT | *Update a specific comment.*                                      |
| **/api/projects/{project_id}/issues/{issue_id}/comments/{comment_id}/** | DELETE | *Delete a specific comment.*                                     |

## Contact
Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
