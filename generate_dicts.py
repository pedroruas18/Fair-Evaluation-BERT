import json
import os
import sys

# GOAL: import processed datasets into dicts

# create train_dev processed
dataset = sys.argv[1]

out_dir = '../data/corpora/preprocessed/' + dataset + '/'
# ----------------------------------------------------------------------------
#                              TEST
# ----------------------------------------------------------------------------
dataset_up = {'bc5cdr_medic':'bc5cdr-disease', 'bc5cdr_chem': 'bc5cdr-chemical', 'ncbi_disease': 'ncbi'}

test_dir = 'coling_datasets/' + dataset_up[dataset] + '/processed_test/'
test = {}

test_files = os.listdir(test_dir)

for filename in test_files:
    doc_id = filename.strip('.concept')
    doc_annots = []

    with open(test_dir + filename, 'r') as in_file:
        data = in_file.readlines()
        in_file.close()
        

        for line in data:
            line_data = line.split('||')
            entity_text = line_data[3]
            kb_ids = line_data[4].strip('\n')
            final_id = ''

            if '|' in kb_ids:
                kb_ids = kb_ids.split('|') 

            else:
                kb_ids = [kb_ids]

            for kb_id in kb_ids:

                if kb_id[0] == 'D' or kb_id[0] == 'C':
                    final_id += 'MESH_' + kb_id + '|'
                
                else:
                    final_id += 'OMIM_' + kb_id + '|'

            final_id = final_id[:-1]
            doc_annots.append((final_id, entity_text))
    
    test[doc_id] = doc_annots

# Output
test_output = json.dumps(test, indent=4)

with open(out_dir + 'test.json', 'w') as out_file:
    out_file.write(test_output)
    out_file.close

# ----------------------------------------------------------------------------
#                              TEST-Refined
# ----------------------------------------------------------------------------
#test_refined_dir = 'coling_datasets' + dataset + 'processed_test_refined/'
test_refined_dir = 'preprocessed/' + dataset + '/'
test_refined = {}

with open(test_refined_dir + '0.concept', 'r') as in_file_2:
    data2 = in_file_2.readlines()
    in_file_2.close()
    
    for line in data2:
        line_data = line.split('||')
        doc_id = line_data[0]
        entity_text = line_data[3]
        
        kb_ids = line_data[4].strip('\n')
        final_id = ''
        
        if '|' in kb_ids:
            kb_ids = kb_ids.split('|') 

        else:
            kb_ids = [kb_ids]

        for kb_id in kb_ids:

            if kb_id[0] == 'D' or kb_id[0] == 'C':
                final_id += 'MESH_' + kb_id + '|'
            
            else:
                final_id += 'OMIM_' + kb_id + '|'

        final_id = final_id[:-1]
        #kb_id = line_data[4].strip('\n')
        
        if doc_id in test_refined.keys():
            test_refined[doc_id].append((final_id, entity_text))
        
        else:
            test_refined[doc_id] = [(final_id, entity_text)]

# Output
test_refined_output = json.dumps(test_refined, indent=4)

with open(out_dir + 'test_refined.json', 'w') as out_file2:
    out_file2.write(test_refined_output)
    out_file2.close