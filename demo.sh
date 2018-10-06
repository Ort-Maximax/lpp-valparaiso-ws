# GET Test
curl --request GET http://localhost:5000/

# POST JSON
curl --header "Content-Type: application/json" --request POST --data '{"method": "hflip", "path":"/data/demo/image.png"}' http://localhost:5000/ffmpeg