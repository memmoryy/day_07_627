import yaml,os
class GetData:
    @classmethod
    def get_yaml_data(cls,name):
        with open("./Data" + os.sep + name) as f:
            return yaml.safe_load(f)