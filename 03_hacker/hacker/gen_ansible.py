import yaml


def gen_ansible():
    yaml_path = "../materials"
    with open(f"{yaml_path}/todo.yml", 'r') as stream:
        try:
            todo = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    ansible_tasks = []

    for package in todo['server']['install_packages']:
        ansible_tasks.append({
            'name': f"Install {package}",
            'apt': {
                'name': package,
                'state': 'present'
            }
        })

    for filename in todo['server']['exploit_files']:
        ansible_tasks.append({
            'name': f"Copy {filename}",
            'copy': {
                'src': filename,
                'dest': f"./{filename}"
            }
        })

    for filename in todo['server']['exploit_files']:
        args = ""
        if filename == "consumer.py":
            args += ' -e ' + ' '.join(todo['bad_guys'])
        ansible_tasks.append({
            'name': f"Run {filename}",
            'command': f"python3 {filename}{args}"
        })

    with open(f"{yaml_path}/deploy.yml", 'w') as outfile:
        yaml.dump(ansible_tasks, outfile, default_flow_style=False)


if __name__ == '__main__':
    gen_ansible()
