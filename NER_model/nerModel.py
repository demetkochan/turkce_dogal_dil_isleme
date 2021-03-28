from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("savasy/bert-base-turkish-ner-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-ner-cased")
ner = pipeline('ner', model=model, tokenizer=tokenizer)


print((ner("Demet üniversite öğrencisidir")))

""""B" means the token begins an entity, 
"I" means it is inside an entity, 
"O" means it is outside an entity, 
and "" means no entity tag is set."""