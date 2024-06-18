To run this
docker build -t api-book .
docker run -d --name test-api -p 8042:8042 api-book
docker run --net=host -it -e NGROK_AUTHTOKEN=2i1JvEkHHxSMhxnHZxONx1prTaG_6ticoiUaMgZX8Qs2aTyJv ngrok/ngrok:latest http --domain=primary-happily-worm.ngrok-free.app 8042
