# import os 
# from textSummarizer.logging import logger
# from transformers import PegasusTokenizer
# from datasets import load_from_disk
# from textSummarizer.entity import DataTransformationConfig

# class DataTransformation:
#     def __init__(self, config: DataTransformationConfig):
#         self.config = config
#         try:
#             # Initialisation du tokenizer Pegasus
#             self.tokenizer = PegasusTokenizer.from_pretrained(
#                 config.tokenizer_name, 
#                 model_max_length=1024,
#                 use_fast=False
#             )
#             # Configuration spécifique pour Pegasus
#             self.tokenizer.pad_token = self.tokenizer.eos_token
#         except Exception as e:
#             logger.error(f"Erreur d'initialisation du tokenizer: {e}")
#             raise

#     def convert_examples_to_features(self, example_batch):
#         """Convertit un batch d'exemples en features pour l'entraînement"""
#         try:
#             # Encodage des entrées (dialogue)
#             input_encodings = self.tokenizer(
#                 example_batch['dialogue'],
#                 max_length=1024,
#                 truncation=True,
#                 padding="max_length",
#                 return_tensors="pt"
#             )
            
#             # Encodage des cibles (summary)
#             with self.tokenizer.as_target_tokenizer():
#                 target_encodings = self.tokenizer(
#                     example_batch['summary'],
#                     max_length=128,
#                     truncation=True,
#                     padding="max_length",
#                     return_tensors="pt"
#                 )

#             return {
#                 'input_ids': input_encodings['input_ids'],
#                 'attention_mask': input_encodings['attention_mask'],
#                 'labels': target_encodings['input_ids']
#             }
#         except Exception as e:
#             logger.error(f"Erreur de conversion du batch: {e}")
#             raise

#     def convert(self):
#         """Exécute la transformation complète du dataset"""
#         try:
#             # Chargement des données
#             dataset_samsum = load_from_disk(self.config.data_path)
#             logger.info(f"Dataset chargé avec {len(dataset_samsum)} exemples")
            
#             # Transformation
#             dataset_samsum_pt = dataset_samsum.map(
#                 self.convert_examples_to_features,
#                 batched=True,
#                 batch_size=4,  # Taille de batch réduite pour stabilité
#                 remove_columns=dataset_samsum.column_names  # Supprime les colonnes originales
#             )
            
#             # Sauvegarde
#             output_path = os.path.join(self.config.root_dir, "samsum_dataset")
#             os.makedirs(self.config.root_dir, exist_ok=True)
#             dataset_samsum_pt.save_to_disk(output_path)
#             logger.info(f"Dataset transformé sauvegardé dans {output_path}")
            
#             return dataset_samsum_pt
            
#         except Exception as e:
#             logger.error(f"Échec de la transformation des données: {e}")
#             raise