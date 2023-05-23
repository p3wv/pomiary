import chardet

with open('/Users/dlaczegociasteczkochinskie/Desktop/cuprum/pomiary_py/hydro/monthly_hydro_extracted_zips/mies_2019.csv', 'rb') as f:
    text = f.read()

result = chardet.detect(text)

print('Detected encoding:', result['encoding'])
print('Confidence:', result['confidence'])