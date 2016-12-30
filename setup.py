from distutils.core import setup
setup(
    name = "Currency-converter",
    py_modules = ["currencyc"],
    entry_points = {"console_scripts": ["currencyc=currencyConverter4.0:main"]},
    version = "4.0",
    description = "Currency converter can exchange between more than 30 currencies",
    author = "Jaime Enríquez",
    author_email = "j.enriquezballe@gmail.com",
    url = "https://github.com/ebjaime/Currency-Converter",
    keywords = ["currency", "converter", "currency-converter", "money"]
)
