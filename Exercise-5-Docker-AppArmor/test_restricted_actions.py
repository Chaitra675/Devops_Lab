
import docker

client = docker.from_env()
container = None

try:
    print("Starting container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor",
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
        name="flask-apparmor-test-actions"
    )

    print(f"Container started: {container.short_id}")

    tests = [
        ("Read /etc/passwd", "cat /etc/passwd"),
        ("Execute /bin/bash", "/bin/bash --version")
    ]

    for description, command in tests:
        result = container.exec_run(command)
        print(f"\nTest: {description}")
        print(f"Exit code: {result.exit_code}")
        print(result.output.decode(errors="replace") or "(no output)")

except docker.errors.DockerException as error:
    print("Docker operation failed:", error)

finally:
    if container is not None:
        try:
            container.stop()
            container.remove()
            print("\nContainer stopped and removed.")
        except docker.errors.DockerException as error:
            print("Cleanup issue:", error)
