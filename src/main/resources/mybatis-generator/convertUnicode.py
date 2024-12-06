
def decode_unicode_escapes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        decoded_content = content.encode().decode('unicode_escape')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(decoded_content)

# 指定你的文件路径
file_path = 'mybatisGeneratorinit.properties'
decode_unicode_escapes(file_path)