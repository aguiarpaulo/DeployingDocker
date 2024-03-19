# DeployingDocker

Start the image:
docker build -t my-test-image .

run container
docker run -d -p 8501:8501 --name my-test-container first-docker-app