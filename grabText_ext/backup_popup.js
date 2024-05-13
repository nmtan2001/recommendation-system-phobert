let scrapeTexts = document.getElementById('scrapeTexts');

scrapeTexts.addEventListener('click', async () => {
    // Get current active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    //Execute script to parse texts on page
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: scrapeTextFrompage,
    });
})
//Function
function scrapeTextFrompage() {
    // Tiki
    var commentElements = document.querySelectorAll('.style__StyledComment-sc-1y8vww-5.dpVjwc.review-comment');

    // Iterate over each comment element
    commentElements.forEach(function(commentElement) {
        // Get the content inside the 'review-comment__content' span
        var contentSpan = commentElement.querySelector('.review-comment__content span');
        if (contentSpan) {
            var content = contentSpan.textContent.trim(); // Get the text content and remove leading/trailing whitespace
            console.log(content);
            chrome.runtime.sendMessage(
                { par: content },
                function (response) {
                    result = response.farewell;
                    console.log(result)
                }
            )
        } else {
            // If there's no span, try to find the content inside a div
            var contentDiv = commentElement.querySelector('.review-comment__content');
            if (contentDiv) {
                var content = contentDiv.textContent.trim(); // Get the text content and remove leading/trailing whitespace
                console.log(content);
                chrome.runtime.sendMessage(
                    { par: content },
                    function (response) {
                        result = response.farewell;
                        console.log(result)
                    }
                )
            }
        }
    });

}