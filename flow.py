from prefect import flow
from prefect_gcp.cloud_storage import GcsBucket
gcp_cloud_storage_bucket_block = GcsBucket.load("gcs-results")

@flow(log_prints=True, persist_result=True)
def my_flow(name: str = "world"):
    print(f"Hello, {name}!")
    return name
