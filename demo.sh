# GET Test
curl --request GET http://localhost:5000/

# POST JSON
curl --header "Content-Type: application/json" --request POST --data '{"method": "hflip", "input":"data/demo/The-Hill.webm", "output":"data/demo/output.webm"}' http://localhost:5000/ffmpeg
curl --header "Content-Type: application/json" --request POST --data '{"method": "vflip", "input":"data/demo/The-Hill.webm", "output":"data/demo/output.webm"}' http://localhost:5000/ffmpeg
curl --header "Content-Type: application/json" --request POST --data '{"method": "convert_mp4_h264", "input":"data/demo/The-Hill.webm", "output":"data/demo/output.mp4"}' http://localhost:5000/ffmpeg