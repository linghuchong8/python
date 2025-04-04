def decode_data(data: bytes):
    try:
        # print("gbk解码异常, 使用utf-8解码：", err)
        msg = data.decode("UTF-8")
    except UnicodeDecodeError as err:
        msg = data.decode("GBK")
        
    return msg