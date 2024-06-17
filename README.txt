To run this
docker build -t api-book .
docker run -d --name test-api -p 8042:8042 api-book
