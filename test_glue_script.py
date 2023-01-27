import sys
import pytest

from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

import glue_script


@pytest.fixture(scope="module", autouse=True)
def glue_context():
    sys.argv.append("--JOB_NAME")
    sys.argv.append("test_count")

    args = getResolvedOptions(sys.argv, ["JOB_NAME"])
    context = GlueContext(SparkContext.getOrCreate())
    job = Job(context)
    job.init(args["JOB_NAME"], args)

    yield (context)

    job.commit()


def test_counts(glue_context):
    dyf = glue_script.read_json(
        glue_context, "s3://awsglue-datasets/examples/us-legislators/all/persons.json"
    )
    assert dyf.toDF().count() == 1961
