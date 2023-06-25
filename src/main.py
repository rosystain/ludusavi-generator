import yaml, os, sys

def check_ludusavi_yaml(yaml_path):
    if os.path.isfile(yaml_path):
        with open(yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

def check_savedata(install_dir):
    for folder in os.listdir(install_dir):
        folder_path = os.path.join(install_dir, folder)
        if os.path.isdir(folder_path) and 'save' in folder.lower():
            return folder_path

def apply_template(game_name, save_path, save_tag):
    data = {
        game_name:{
            'files':
                {
                    save_path:
                        {
                            'tags':[
                                save_tag
                            ],
                            'when':[
                                {
                                    'os':'windows'
                                }
                            ]
                        }
                }
        }
    }
    return data

def convert_placeholder(path, base):
    document_path = os.path.join(os.path.expanduser("~"),"Documents")
    appdata_path = os.environ['APPDATA']
    if base in path:
        relpath = os.path.relpath(path,start=base)
        result = os.path.join('<base>',relpath)
        return result.replace("\\", "/")
    elif document_path in path:
        relpath = os.path.relpath(path,start=document_path)
        result = os.path.join('<winDocuments>',relpath)
        return result.replace("\\", "/")
    elif appdata_path in path:
        relpath = os.path.relpath(path,start=appdata_path)
        result = os.path.join('<winAppData>',relpath)
        return result.replace("\\", "/")
    else:
        return path

def create_yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, indent=2, default_flow_style=False, sort_keys=False, allow_unicode=True)

def update_yaml(data, path):
    with open(path, 'r', encoding='utf-8') as f:
        olddata = yaml.safe_load(f)
    data[game_name]['files'].update(olddata[game_name]['files'])
    create_yaml(data, path)

if __name__ == '__main__':
    game_name = sys.argv[2]
    install_dir = sys.argv[3]
    save_path = convert_placeholder(sys.argv[4], install_dir)
    yaml_path = os.path.join(install_dir, '.ludusavi.yaml')
    save_tag = sys.argv[5]
    if sys.argv[1] == 'build':
        create_yaml(apply_template(game_name, save_path, save_tag), yaml_path)
    if sys.argv[1] == 'add':
        update_yaml(apply_template(game_name, save_path, save_tag), yaml_path)
        