def decode_data(data):
    try:
        msg = data.decode("GBK")
    except UnicodeDecodeError as err:
        # print("gbk解码异常, 使用utf-8解码：", err)
        msg = data.decode("UTF-8")
        
    return msg