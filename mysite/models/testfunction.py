from text_processing import word_segmentation, clean_text
from predict1 import predict_sentiment
from transformers import AutoTokenizer, RobertaForSequenceClassification

#run beforehand
#vncorenlp -Xmx2g /mnt/d/ALLIN/Diploma/project/mysite/VnCoreNLP/VnCoreNLP-1.2.jar -p 9000 -a "wseg"
# Define the model name/path
model_name = "phobert_sentiment_analysis_new"

# Load the model
model = RobertaForSequenceClassification.from_pretrained(model_name)

# Load the tokenizer as well
tokenizer = AutoTokenizer.from_pretrained(model_name)

def test_clean_trailing_repeating():
    assert clean_text(" ngonnnnn  đẹppppppp   ") == "ngon đẹp"

def test_clean_replace_time_money():
    assert clean_text("1tr 1k 1pt 1p 1h t2") == "1 triệu đồng 1 nghìn đồng 1 phần trăm 1 phút 1 giờ thứ 2"

def test_clean_teencode():
    assert clean_text("cx tạm nma dùng đt xem yt o kê, nên mua") == "cũng tạm nhưng mà dùng điện thoại xem youtube ok nên mua"

def test_segmentation():
    assert word_segmentation(clean_text("cx tạm nma dùng đt xem yt o kê, nên mua")) == "cũng tạm nhưng_mà dùng điện_thoại xem youtube ok nên mua" 

def test_predict_sentiment():
    assert predict_sentiment(model,tokenizer,"cx tạm nma dùng đt xem yt o kê, nên mua") == 1    