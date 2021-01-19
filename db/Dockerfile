
# Derived from official mysql image (our base image)
FROM mysql:5.7
# Add a database
# Add the content of the .sql file to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY ./CreateTable.sql/ /docker-entrypoint-initdb.d/