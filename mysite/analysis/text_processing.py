import string
import re
from vncorenlp import VnCoreNLP


vnp = VnCoreNLP("/mnt/d/ALLIN/Diploma/project/mysite/VnCoreNLP/VnCoreNLP-1.2.jar", annotators="wseg")


# Define a function to perform word segmentation
def word_segmentation(text):
    segmented_text = vnp.tokenize(text)
    # Flatten the list of lists
    segmented_text_flat = [word for segment in segmented_text for word in segment]
    # Join the segmented words into a single string
    segmented_text_str = " ".join(segmented_text_flat)
    return segmented_text_str


def clean_text(text):
    text = text.lower()
    # text = re.sub(emoji_pattern, " ", text)
    replace_list = {
        'òa': 'oà', 'óa': 'oá', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'òe': 'oè', 'óe': 'oé','ỏe': 'oẻ',
        'õe': 'oẽ', 'ọe': 'oẹ', 'ùy': 'uỳ', 'úy': 'uý', 'ủy': 'uỷ', 'ũy': 'uỹ','ụy': 'uỵ', 'uả': 'ủa',
        'ả': 'ả', 'ố': 'ố', 'u´': 'ố','ỗ': 'ỗ', 'ồ': 'ồ', 'ổ': 'ổ', 'ấ': 'ấ', 'ẫ': 'ẫ', 'ẩ': 'ẩ',
        'ầ': 'ầ', 'ỏ': 'ỏ', 'ề': 'ề','ễ': 'ễ', ' ể ': 'ể', 'ắ': 'ắ', 'ủ': 'ủ', 'ế': 'ế', 'ở': 'ở', 'ỉ': 'ỉ',
        'ẻ': 'ẻ', 'àk': ' à ','aˋ': 'à', 'iˋ': 'ì', 'ă´': 'ắ','ử': 'ử', 'e˜': 'ẽ', 'y˜': 'ỹ', 'a´': 'á',
        #Quy các icon về 2 loại emoji: Tích cực hoặc tiêu cực
        "👹": "tiêu cực", "👻": " tích cực ", "💃": " tích cực ",'🤙': ' tích cực ', '👍': ' tích cực ',
        "💄": " tích cực ", "💎": " tích cực ", "💩": " tích cực ","😕": "tiêu cực", "😱": "tiêu cực", "😸": " tích cực ",
        "😾": "tiêu cực", "🚫": "tiêu cực",  "🤬": "tiêu cực","🧚": " tích cực ", "🧡": " tích cực ",'🐶':' tích cực ',
        '👎': ' tiêu cực ', '😣': ' tiêu cực ','✨': ' tích cực ', '❣': ' tích cực ','☀': ' tích cực ',
        '♥': ' tích cực ', '🤩': ' tích cực ', 'like': ' tích cực ', '💌': ' tích cực ',
        '🤣': ' tích cực ', '🖤': ' tích cực ', '🤤': ' tích cực ', ':(': ' tiêu cực ', '😢': ' tiêu cực ',
        '❤': ' tích cực ', '😍': ' tích cực ', '😘': ' tích cực ', '😪': ' tiêu cực ', '😊': ' tích cực ',
        '?': ' ? ', '😁': ' tích cực ', '💖': ' tích cực ', '😟': ' tiêu cực ', '😭': ' tiêu cực ',
        '💯': ' tích cực ', '💗': ' tích cực ', '♡': ' tích cực ', '💜': ' tích cực ', '🤗': ' tích cực ',
        '^^': ' tích cực ', '😨': ' tiêu cực ', '☺': ' tích cực ', '💋': ' tích cực ', '👌': ' tích cực ',
        '😖': ' tiêu cực ', '😀': ' tích cực ', ':((': ' tiêu cực ', '😡': ' tiêu cực ', '😠': ' tiêu cực ',
        '😒': ' tiêu cực ', '🙂': ' tích cực ', '😏': ' tiêu cực ', '😝': ' tích cực ', '😄': ' tích cực ',
        '😙': ' tích cực ', '😤': ' tiêu cực ', '😎': ' tích cực ', '😆': ' tích cực ', '💚': ' tích cực ',
        '✌': ' tích cực ', '💕': ' tích cực ', '😞': ' tiêu cực ', '😓': ' tiêu cực ', '️🆗️': ' tích cực ',
        '😉': ' tích cực ', '😂': ' tích cực ', ':v': '  tích cực ', '=))': '  tích cực ', '😋': ' tích cực ',
        '💓': ' tích cực ', '😐': ' tiêu cực ', ':3': ' tích cực ', '😫': ' tiêu cực ', '😥': ' tiêu cực ',
        '😃': ' tích cực ', '😬': ' tiêu cực ', '😌': ' tiêu cực ', '💛': ' tích cực ', '🤝': ' tích cực ', '🎈': ' tích cực ',
        '😗': ' tích cực ', '🤔': ' tiêu cực ', '😑': ' tiêu cực ', '🔥': ' tiêu cực ', '🙏': ' tiêu cực ',
        '🆗': ' tích cực ', '😻': ' tích cực ', '💙': ' tích cực ', '💟': ' tích cực ',
        '😚': ' tích cực ', '❌': ' tiêu cực ', '👏': ' tích cực ', ';)': ' tích cực ', '<3': ' tích cực ',
        '🌝': ' tích cực ',  '🌷': ' tích cực ', '🌸': ' tích cực ', '🌺': ' tích cực ',
        '🌼': ' tích cực ', '🍓': ' tích cực ', '🐅': ' tích cực ', '🐾': ' tích cực ', '👉': ' tích cực ',
        '💐': ' tích cực ', '💞': ' tích cực ', '💥': ' tích cực ', '💪': ' tích cực ',
        '💰': ' tích cực ',  '😇': ' tích cực ', '😛': ' tích cực ', '😜': ' tích cực ',
        '🙃': ' tích cực ', '🤑': ' tích cực ', '🤪': ' tích cực ','☹': ' tiêu cực ',  '💀': ' tiêu cực ',
        '😔': ' tiêu cực ', '😧': ' tiêu cực ', '😩': ' tiêu cực ', '😰': ' tiêu cực ', '😳': ' tiêu cực ',
        '😵': ' tiêu cực ', '😶': ' tiêu cực ', '🙁': ' tiêu cực ', '🎉': ' tích cực ',  "🤢": " tiêu cực ", "😤": " tiêu cực ",
        "😿": " tiêu cực ","☹️": " tiêu cực ", "💔": " tiêu cực ",  "👿": " tiêu cực ", "😅": " tích cực ",
        "😺": " tích cực ",   "😽": " tích cực ", "🙌": " tích cực ", "👋": " tích cực ",  "❤️": " tích cực ",  "💘": " tích cực ",
        "💝": " tích cực ", "🌹": " tích cực ", "🌻": " tích cực ", "🍀": " tích cực ", "🎶": " tích cực ",
        "👑": " tích cực ", "🌞": " tích cực ", "⭐": " tích cực ", "🌈": " tích cực ", "💅": " tích cực ",  "👠": " tích cực ",
        "🎀": " tích cực ", "🎁": " tích cực ",  "🔝": " tích cực ", "🆙": " tích cực ", "🆒": " tích cực ",
        "🏅": " tích cực ", "🥇": " tích cực ", "🥈": " tích cực ", "🥉": " tích cực ", "🏆": " tích cực ",
        "🎖": " tích cực ", "🏵": " tích cực ", "🎗": " tích cực ",  "🎊": " tích cực ",
        "🍻": " tích cực ", "🍺": " tích cực ", "🥂": " tích cực ", "🍷": " tích cực ", "🍸": " tích cực ",
        ':))': ' tích cực ', ':)': ' tích cực ',  '><': ' tích cực ', ':>' : ' tích cực ',
        #Chuẩn hóa 1 số sentiment words/English words
        #okay
        ' ô kêi ': ' ok ', 'okie': ' ok ', ' o kê': ' ok ', ' okey ': ' ok ', ' ôkê ': ' ok ', ' oki ': ' ok ', ' oke ':  ' ok ',' okay ':' ok ',' okê ':' ok ',
        #cám ơn
        ' tks ': ' cám ơn ', ' thks ': ' cám ơn ', ' thanks ': ' cám ơn ', ' ths ': ' cám ơn ', ' thank ': ' cám ơn ',  'thask' : 'cám ơn',
        #tôi
         ' t ': ' tôi ', 'mk' : 'mình', 'mìk': ' mình ', ' m ': ' mình ', ' mik ': ' mình ',
         #Không
        ' kg ': ' không ',' not ': ' không ', 'kg': ' không ', ' k ': ' không ',' kh ':' không ','kô':' không ',' hok ':' không '
        ,' kp ': ' không phải ', ' kphai ' : 'không phải',' kô ': ' không ', 'ko' : ' không ',' ko ': ' không ', 'khong': ' không ',
        #được
        ' đx ': ' được ', 'đx': ' được ',' dk ': ' được ','dk': ' được ', ' dc ': ' được ', 'dc': ' được ', ' đk ': ' được ','đk': ' được ', 'đc' : 'được', ' đc ': ' được ',
        #cười/slangs
        ' he he ': ' tích cực ','hehe': ' tích cực ','hihi': ' tích cực ', 'haha': ' tích cực ', 'hjhj': ' tích cực ', 'kkk' :' tích cực ', 'loz' : ' tiêu cực '
        , 'lol': ' tiêu cực ',' cc ': ' tiêu cực ', 'cute': ' dễ thương ','huh': ' tiêu cực ', 'buoi' : ' tiêu cực ',' kẹc ' : ' tiêu cực ', 'nma' : ' nhưng mà ',
        ' vs ': ' với ', 'wa': ' quá ', 'wá': ' quá', ' j ': ' gì ', '“': ' ', ' iu ' : 'yêu',  ' thick ': ' thích ', 'sấ': ' xấu ', 'qá': ' quá ' , ' tot ': ' tốt ',
        'bt': ' bình thường ', 'hnao' : 'hôm nào',  'hnay' : 'hôm nay', 'đthoai' : 'điện thoại', ' tl ': ' trả lời ', ' r ': ' rồi ',' nt ': ' nhắn tin ',' tl ': ' trả lời '
        ,' sài ': ' xài ','bjo':' bao giờ ','dep': ' đẹp ',' xau ': ' xấu ','hàg': ' hàng ', 'qủa': ' quả ', '%': ' phần trăm ', 'ns' : 'nói', 'ms' : 'mới',
         'hqa': ' hôm qua ', 'mn' : 'mọi người', 'ròi' : 'rồi', 'mng' : 'mọi người', 'ròy': ' rồi ', 'hk': ' không ', 'trl': 'trả lời', 'ns' : ' nói ', 'chs' : 'chơi', 'ptrăm' : 'phần trăm',
        ' s ': ' sao ', ' tuột ': ' tụt ', 'nv': ' nhân viên ', 'ad' : 'nhân viên', 'ads' : 'nhân viên', 'mún': ' muốn ', 'cx' : 'cũng', 'nge' : ' nghe ', 'toẹt': ' tuyệt ',
        #english words
        ' sz ': ' cỡ ', 'size': ' cỡ ', ' luv ' :'yêu' , 'love' : 'yêu ', ' wow ' : 'tuyệt vời', ' woah ' : 'tuyện vời',
        'authentic': ' chuẩn chính hãng ',' aut ': ' chuẩn chính hãng ', ' auth ': ' chuẩn chính hãng ', ' store ': ' cửa hàng ',
        'shop': ' cửa hàng ', 'sp': ' sản phẩm ', 'gud': ' tốt ','god': ' tốt ','wel done':' rất tốt ', 'good': ' tốt ', 'gút': ' tốt ',
        'gut': ' tốt ', ' nice ': ' tốt ', 'perfect': 'rất tốt',
        'time': ' thời gian ', ' ship ': ' giao hàng ',  'qc' : 'quảng cáo',
        'product': 'sản phẩm', 'quality': 'chất lượng', ' chat ':' chất ', 'excelent': 'hoàn hảo', 'bad': 'tệ','fresh': ' tươi ','sad': ' tệ ', 'ship' : 'giao hàng', 'shipper' : ' người giao hàng', 'sipper' :'người giao hàng',
        'date': ' hạn sử dụng ', 'hsd': ' hạn sử dụng ','quickly': ' nhanh ', 'quick': ' nhanh ','fast': ' nhanh ','delivery': ' giao hàng ',' síp ': ' giao hàng ', 'tgd': 'cửa hàng', 'tgđ' : 'cửa hàng', 'tiki' : 'cửa hàng',
        'beautiful': ' đẹp tuyệt vời ',  ' shopE ': ' cửa hàng ',' order ': ' đặt hàng ', 'sendo' : 'cửa hàng', 'amazon' : 'cửa hàng', 'cellphoneS' : 'cửa hàng', 'biuti' : 'đẹp tuyệt vời',
        'chất lg': ' chất lượng ',' sd ': ' sử dụng ',' dt ': ' điện thoại ','đt ': ' điện thoại ' ,' wfi ': ' wifi ', 'wf' : 'wifi' ,
        'thik': ' thích ',' sop ': ' cửa hàng ', ' fbook ' : ' facebook ' ,' fb ': ' facebook ', ' face ': ' facebook ', ' very ': ' rất ','quả ng ':' quảng  ', 'ins' : 'instagram', 'insta' : 'instagram',
        'delicious': ' ngon ', 'lác': ' lag ', 'lắc': ' lag ', 'wed': 'web', 'wep': ' web ','fake': ' giả mạo ',
        ' por ': ' tệ ',' poor ': ' tệ ', 'ib':' nhắn tin ', 'rep':' trả lời ','fback':' feedback ','fedback':' feedback ',
        'dt ': ' điện thoại ',  'youtobe': ' youtube ', 'ytube' : 'youtube', 'yt' : 'youtube',

        #less than 3 * converted to 1 *, over 3 * converted to 5 *
        '⭐': 'star ', '*': 'star ', '🌟': 'star ',
        '6 sao': ' 5star ','6 star': ' 5star ', '5star': ' 5star ','5 sao': ' 5star ','5sao': ' 5star ',
        'starstarstarstarstar': ' 5star ', '1 sao': ' 1star ', '1sao': ' 1star ','2 sao':' 1star ','2sao':' 1star ',
        '2 starstar':' 1star ','1star': ' 1star ', '0 sao': ' 1star ', '0star': ' 1star ',}

    for k, v in replace_list.items():
      text = text.replace(k, v)
    text = re.sub(r'(\d+)p ', r'\1 phút ', text) #replace minute
    text = re.sub(r'(\d+)pt ', r'\1 phần trăm ', text) #replace percentage
    text = re.sub(r't(\d+)', r'thứ \1 ', text) #replace minute
    text = re.sub(r'(\d+)h', r'\1 giờ', text) #replace percentage
    text = re.sub(r'(\d+)k', r'\1 nghìn đồng', text) #replace money
    text = re.sub(r'(\d+)tr', r'\1 triệu đồng', text) #replace money
    text = re.sub(r'([a-z]+?)\1+',r'\1', text) #Reduces consecutive repeating characters to a single character.
    text = re.sub(r"(\w)\s*([{}])\s*(\w)".format(re.escape(string.punctuation)), r"\1 \3", text)  # Removes punctuation after word characters
    text = re.sub(r"(\w)([" + string.punctuation + "])", r"\1", text)  # Removes punctuation after word characters
    text = re.sub(f"([{string.punctuation}])([{string.punctuation}])+", r"\1", text)  # Remove repeated consecutive punctuation marks
    text = text.strip()  # Remove leading and trailing whitespaces
    # While loops to remove leading and trailing punctuation and whitespace characters.
    while text.endswith(tuple(string.punctuation + string.whitespace)):
        text = text[:-1]
    while text.startswith(tuple(string.punctuation + string.whitespace)):
        text = text[1:]
    text = re.sub(r"\s+", " ", text)  # Replace multiple consecutive whitespaces with a single space

    return text