from prefect.infrastructure import DockerContainer

docker_block = DockerContainer(image="jrvdocker/a_project_template:latest")
docker_block.save("docker-custom-image")
