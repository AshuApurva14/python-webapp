# python-webapp
This is a python web application.

### cicd pipeline 


for python version,I have used matrix strategy.

GitHub has a few special contexts that you can access as part of your workflows. Matrix is one of these. By defining the matrix as part of the strategy, python-version has now become a property of the matrix context. This means that you can access any variable defined as part of the matrix with the dot (.) syntax, for example, matrix.python-version.
