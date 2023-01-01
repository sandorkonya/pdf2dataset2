from pdf2dataset import download
import shutil
import os

output_dir = os.path.abspath("bench")

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

download(
    processes_count=16,
    thread_count=32,
    url_list="../tests/test_files/test.parquet.gzip",
    output_folder=output_dir,
    output_format="files",
    input_format="parquet",
    url_col="url",
    caption_col="description",
    enable_wandb=False,
    number_sample_per_shard=10,
    distributor="multiprocessing",
)

# rm -rf bench
