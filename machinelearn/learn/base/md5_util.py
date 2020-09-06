import hashlib


def getMd5 (productId, productSeqDate, prdoductSeqId):
    str = productId + productSeqDate + prdoductSeqId
    return hashlib.md5(str.encode(encoding="UTF-8")).hexdigest().lower()