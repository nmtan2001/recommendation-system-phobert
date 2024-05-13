from vncorenlp import VnCoreNLP

# Initialize VnCoreNLP with the desired annotators
vncore_nlp = VnCoreNLP("VnCoreNLP-1.2.jar", annotators="wseg,pos,ner,parse")

# Define a function to perform word segmentation
def word_segmentation(text):
    segmented_text = vncore_nlp.tokenize(text)
    # Convert each segment to string
    segmented_text = [str(segment) for segment in segmented_text]
    # Join the segmented words into a single string
    segmented_text_str = " ".join(segmented_text)
    return segmented_text_str


# Example usage
text = "Xin chào, đây là một ví dụ về word segmentation."
segmented_text = word_segmentation(text)
print(segmented_text)

# vncorenlp -Xmx2g /mnt/d/ALLIN/Diploma/project/VnCoreNLP/VnCoreNLP-1.2.jar -p 9000 -a "wseg"

