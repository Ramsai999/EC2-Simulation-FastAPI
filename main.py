from fastapi import FastAPI
import subprocess

app = FastAPI()

container_name = "my-sim-instance"

@app.get("/")
def home():
    return {"message": "Welcome to EC2 Simulation!"}

@app.post("/create")
def create_instance():
    # Build and run the Docker container
    subprocess.run(["docker", "build", "-t", container_name, "."], check=True)
    subprocess.run(["docker", "run", "-d", "--name", container_name, container_name])
    return {"message": "Instance created"}

@app.post("/run")
def run_script():
    # Execute the bash script inside the container
    output = subprocess.check_output(["docker", "exec", container_name, "bash", "/docker_script.sh"])
    return {"output": output.decode()}

@app.post("/terminate")
def terminate():
    # Stop and remove the container
    subprocess.run(["docker", "stop", container_name])
    subprocess.run(["docker", "rm", container_name])
    return {"message": "Instance terminated"}
