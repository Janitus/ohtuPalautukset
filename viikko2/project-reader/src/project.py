class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        output = f"Name: {self.name}\n"
        output += f"Description: {self.description}\n"
        output += f"License: {self.license}\n\n"
        output += "Authors:\n"
        for author in self.authors:
            output += f"- {author}\n"
        output += "\nDependencies:\n"
        for dep in self.dependencies:
            output += f"- {dep}\n"
        output += "\nDevelopment dependencies:\n"
        for dev_dep in self.dev_dependencies:
            output += f"- {dev_dep}\n"
        return output