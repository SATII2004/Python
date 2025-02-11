import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
from sacrebleu import corpus_bleu
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer

# Load the model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-es"  # English to Spanish translation
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Evaluation function
def evaluate_translation(reference, hypothesis):
    bleu = corpus_bleu([reference], [hypothesis]).score / 100
    meteor = meteor_score(reference, hypothesis)
    rouge = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    rouge_score = rouge.score(reference, hypothesis)['rougeL'].fmeasure
    return bleu, meteor, rouge_score

# Translation function
def translate_text(input_text):
    tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**tokens)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Streamlit Interface
st.title("Interactive Machine Translation System")
st.markdown("Translate English text into Spanish and evaluate the model's performance.")

input_text = st.text_area("Enter English text:")
if st.button("Translate"):
    if input_text.strip():
        # Perform translation
        translated_text = translate_text(input_text)
        st.write("**Translated Text:**", translated_text)

        # Evaluate translation
        reference = st.text_area("Enter the reference translation (for evaluation):")
        if reference.strip():
            bleu, meteor, rouge = evaluate_translation(reference, translated_text)
            st.write(f"**BLEU Score:** {bleu:.2f}")
            st.write(f"**METEOR Score:** {meteor:.2f}")
            st.write(f"**ROUGE-L Score:** {rouge:.2f}")

            # Check thresholds
            if bleu < 0.70 and meteor < 0.70 and rouge < 0.70:
                st.error("The model's performance is below the threshold. Suggestions for improvement:")
                st.markdown("""
                - Increase the dataset size with more examples.
                - Fine-tune the model with domain-specific data.
                - Experiment with hyperparameters like learning rate and batch size.
                """)
            else:
                st.success("The model's performance is satisfactory!")
    else:
        st.error("Please enter text to translate.")
