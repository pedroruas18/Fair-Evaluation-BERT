# Download the datasets
wget https://yadi.sk/d/lQ8bAhFMnjSvTA
tar -xvf coling_datasets.tar.gaz
rm coling_datasets.tar.gaz


# Generate a joint train+dev folder for the NCBI-Disease corpus
mkdir coling_datasets/ncbi/processed_train_dev
cp -r coling_datasets/ncbi/processed_train/* coling_datasets/ncbi/processed_train_dev/
cp -r coling_datasets/ncbi/processed_dev/* coling_datasets/ncbi/processed_train_dev/

# Generate Refined test sets for the 3 datasets
mkdir preprocessed/

mkdir preprocessed/ncbi_disease/
python process_data.py --train_data_folder coling_datasets/ncbi/processed_traindev/ --test_data_folder coling_datasets/ncbi/processed_test/  --save_to preprocessed/ncbi_disease/
python generate_dicts.py ncbi_disease

mkdir preprocessed/bc5cdr_medic/
python process_data.py --train_data_folder coling_datasets/bc5cdr-disease/processed_traindev/ --test_data_folder coling_datasets/bc5cdr-disease/processed_test/  --save_to preprocessed/bc5cdr_medic_/
python generate_dicts.py bc5cdr_medic

mkdir preprocessed/bc5cdr_chem/
python process_data.py --train_data_folder coling_datasets/bc5cdr-chemical/processed_traindev/ --test_data_folder coling_datasets/bc5cdr-chemical/processed_test/  --save_to preprocessed/bc5cdr_chem/
python generate_dicts.py bc5cdr_chem


In each of the output dirs there wiil be the files 'test.json' and 'test_refined.json'.