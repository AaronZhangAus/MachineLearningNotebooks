from azureml.core import Workspace, Experiment, ScriptRunConfig
from azureml.widgets import RunDetails


#connect to workspace from config.json file
# to be continued from here... unable to sign in Azure portal on
# laptop
ws=Workspace.from_config("config.json")

experiment = Experiment(workspace=ws, name='day1-experiment-hello')

config = ScriptRunConfig(source_directory='./tutorials/get-started-day1/code/hello', script='hello.py', compute_target='cpu-cluster')

run = experiment.submit(config)
RunDetails(run).show()

