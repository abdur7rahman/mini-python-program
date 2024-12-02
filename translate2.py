from translate import Translator

# Initialize translator for Tamil
translator = Translator(to_lang="ta")  # "ta" is the language code for Tamil
translation = translator.translate("mathematics")
print(translation)
