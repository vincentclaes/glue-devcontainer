# Glue Devcontainer

## Run glue_script.py from CLI
```
PROFILE_NAME=default
docker run -it -v ~/.aws:/home/glue_user/.aws -v $PWD:/home/glue_user/workspace/ -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 --name glue_spark_submit amazon/aws-glue-libs:glue_libs_3.0.0_image_01 spark-submit /home/glue_user/workspace/glue_script.py

root
|-- family_name: string
|-- name: string
|-- links: array
|    |-- element: struct
|    |    |-- note: string
|    |    |-- url: string
|-- gender: string
|-- image: string
|-- identifiers: array
|    |-- element: struct
|    |    |-- scheme: string
|    |    |-- identifier: string
|-- other_names: array
|    |-- element: struct
|    |    |-- lang: string
|    |    |-- note: string
|    |    |-- name: string
|-- sort_name: string
|-- images: array
|    |-- element: struct
|    |    |-- url: string
|-- given_name: string
|-- birth_date: string
|-- id: string
|-- contact_details: array
|    |-- element: struct
|    |    |-- type: string
|    |    |-- value: string
|-- death_date: string

```



## VS Code Devcontainer

### Setup
With VS Code you can use a docker image as a basis for your development.

- Install VS Code Remote Development. vscode id: `ms-vscode-remote.vscode-remote-extensionpack`
- CMD + Shift + P > Preferences: Open Workspace Settings (JSON)
- Add the following JSON:
```
{
    "python.defaultInterpreterPath": "/usr/bin/python3",
    "python.analysis.extraPaths": [
        "/home/glue_user/aws-glue-libs/PyGlue.zip:/home/glue_user/spark/python/lib/py4j-0.10.9-src.zip:/home/glue_user/spark/python/",
    ]
}
```

- Start Glue Pyspark shell in a Docker container:

```bash
AWS_PROFILE=default
docker run -it -v ~/.aws:/home/glue_user/.aws -v $PWD:/home/glue_user/workspace/ -e AWS_PROFILE=$AWS_PROFILE -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 --name glue_pyspark amazon/aws-glue-libs:glue_libs_3.0.0_image_01 pyspark 
```
- Choose Remote Explorer in the navigation pane, and choose the container `amazon/aws-glue-libs:glue_libs_3.0.0_image_01`.
- Right-click and choose Attach to Container > Confirm the Pop-up by pressing "Got it"
- In the left pane, choose "Open folder" > /home/glue_user/workspace

### Run glue_script.py
- run `spark-submit /home/glue_user/workspace/glue_script.py` from the terminal
- or you can do Run > Start Without Debugging

### Debug glue_script.py
- Left click to add a breakpoint (red dot) next to the line number you want to inspect.
- Run > Start Debugging > current file
![debugging](assets/debugging.png)

### Spark UI
http://localhost:4041/jobs/

## Run tests in CICD

You can run the tests in your CICD system using the following command.
```bash
PROFILE_NAME=default
docker run -it -v ~/.aws:/home/glue_user/.aws -v $PWD:/home/glue_user/workspace/ -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 --name glue_pytest amazon/aws-glue-libs:glue_libs_3.0.0_image_01 -c "python3 -m pytest --disable-warnings"

starting org.apache.spark.deploy.history.HistoryServer, logging to /home/glue_user/spark/logs/spark-glue_user-org.apache.spark.deploy.history.HistoryServer-1-1c10b4d7ca53.out
====================================================== test session starts =======================================================
platform linux -- Python 3.7.15, pytest-6.2.3, py-1.11.0, pluggy-0.13.1
rootdir: /home/glue_user/workspace
plugins: anyio-3.6.2
collected 1 item                                                                                                                 

test_glue_script.py .                                                                                                      [100%]

================================================= 1 passed, 1 warning in 20.19s ==================================================
```
