from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        project_name = data['tool']['poetry']['name']
        project_description = data['tool']['poetry']['description']
        dependencies = list(data['tool']['poetry']['dependencies'].keys())
        dev_dependencies = list(data['tool']['poetry']['group']['dev']['dependencies'].keys())
        license = data['tool']['poetry']['license']
        authors = data['tool']['poetry']['authors']

        return Project(project_name, project_description, license, authors, dependencies, dev_dependencies)