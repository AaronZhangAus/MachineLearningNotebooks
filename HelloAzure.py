from azureml.core import VERSION,Workspace

#connect to workspace from config.json file
ws=Workspace.from_config("config.json")
print(VERSION)