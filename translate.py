from deep_translator import GoogleTranslator

text=GoogleTranslator(
    source="en",
    target="tamil"
)

result = text.translate("how")

print(result)