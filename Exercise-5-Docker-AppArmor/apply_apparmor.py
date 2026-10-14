
import docker

client = docker.from_env()

image_tag = "flask-apparmor"

print("Building Docker image...")
client.images.build(path=".", tag=image_tag)

print("Running container with AppArmor profile...")
try:
    container = client.containers.run(
        image_tag,
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
        name="flask-apparmor-sdk"
    )

    print(f"Container started: {container.short_id}")

    info = client.api.inspect_container(container.id)
    security_options = info["HostConfig"].get("SecurityOpt")

    print("Configured security options:", security_options)

    print("Note: Configuration does not prove that AppArmor enforcement is active.")

except docker.errors.APIError as error:
    print("Docker could not start the container with this profile.")
    print(error)

finally:
    try:
        container.stop()
        container.remove()
        print("Container stopped and removed.")
    except (NameError, docker.errors.NotFound):
        pass
