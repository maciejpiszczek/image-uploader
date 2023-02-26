# Image Uploader API
RESTful API for uploading images.

## Tech Stack
- Django
- Django REST Framework
- PostgreSQL
- Redis
- Docker

## Requirements
Image Uploader API requires the following to run:
* Python 3.11
* latest version od Docker
* latest version of docker-compose

## How to run?

1. Clone this GitHub repository (use one of the following commands, depending on what method you use)  
**HTTPS:**  
`git clone https://github.com/maciejpiszczek/image-uploader.git`  
**SSH:**  
`git clone git@github.com:maciejpiszczek/image-uploader.git`
2. Go to the project directory:  
`cd image-uploader`
3. Provide .env file with necessary environmental variables (see env/.env-default for reference).
4. For development app run command in your terminal:  
`docker compose up --build`
