if __name__ == "__main__":
    import sys
    import yaml
    from jinja2 import Template

    with open("variables.yml", "r") as f:
        variables = yaml.safe_load(f)

    with open("docker-compose.yml.tpl") as f:
        template = Template(f.read())

    docker_compose_content = template.render(variables)

    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose_content)

    print("Fichier `docker-compose.yml` généré avec succès.")
