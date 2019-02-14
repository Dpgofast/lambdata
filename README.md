# LambData

## A Python package with helpful utility functions for Data Science

** A one stop shop for your data science import needs. By no means exclusive or anywhere near an actual one stop shop, but here we are anyway.**
![Goat]('data:image/jpeg;base64,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')
