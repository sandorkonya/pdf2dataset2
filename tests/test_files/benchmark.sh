set -e
rm -rf bench
pdf2dataset --url_list test.parquet.gzip --input_format "parquet"\
         --url_col "url" --caption_col "description" --output_format webdataset\
           --output_folder bench --processes_count 16 --thread_count 64\
             --enable_wandb True
#rm -rf bench