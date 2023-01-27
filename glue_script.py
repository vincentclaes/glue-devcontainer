import sys
import logging

from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

logger = logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()


class GluePythonSampleTest:
    def __init__(self):
        params = []
        if '--JOB_NAME' in sys.argv:
            params.append('JOB_NAME')
        args = getResolvedOptions(sys.argv, params)

        self.context = GlueContext(SparkContext.getOrCreate())
        self.job = Job(self.context)

        if 'JOB_NAME' in args:
            jobname = args['JOB_NAME']
        else:
            jobname = "test"
        logger.debug(f"jobname is {jobname}")
        self.job.init(jobname, args)

    def run(self):
        df = read_json(self.context, "s3://awsglue-datasets/examples/us-legislators/all/persons.json")
        df.printSchema()
        df.show(3)
        self.job.commit()


def read_json(glue_context, path):
    logger.info(f"reading a dataset from {path}")
    dynamicframe = glue_context.create_dynamic_frame.from_options(
        connection_type='s3',
        connection_options={
            'paths': [path],
            'recurse': True
        },
        format='json'
    )
    return dynamicframe


if __name__ == '__main__':
    GluePythonSampleTest().run()