from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

text = open("output/transcript.txt", encoding="utf-8").read()

model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

inputs = tokenizer(text, return_tensors="pt")

tamil_token_id = tokenizer.convert_tokens_to_ids("tam_Taml")
generated = model.generate(**inputs, forced_bos_token_id=tamil_token_id)

translated = tokenizer.batch_decode(generated, skip_special_tokens=True)[0]

open("output/translated.txt", "w", encoding="utf-8").write(translated)

print("Tamil translation completed successfully")
