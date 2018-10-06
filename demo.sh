# GET Test
curl --request GET http://localhost:5000/

# POST JSON
curl --header "Content-Type: application/json" --request POST --data '{"method": "hflip", "input":"data/demo/The-Hill.webm", "output":"data/demo/output.webm"}' http://localhost:5000/ffmpeg