console.log('Changed code');

document.addEventListener('DOMContentLoaded', function () {
    var scrapeTexts = document.getElementById('scrapeTexts');
    var overallSentiment = document.getElementById('overallSentiment');

    scrapeTexts.addEventListener('click', async () => {
        // Get current active tab
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        
        // Execute script to parse texts on page
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            func: scrapeTextFromPage,
        }).then((resultArray) => {
            const result = resultArray[0].result;
            console.log('update: ', result);
            overallSentiment.textContent = result;

        }).catch((error) => {
            console.error('Error:', error);
        });
    });

    // Function to scrape text from page
    async function scrapeTextFromPage() {
        return new Promise((resolve, reject) => {
            var positiveCount = 0;
            var negativeCount = 0;
            var processedCount = 0; // Track the number of processed comments
            // Select all comment elements
            var commentElements = document.querySelectorAll('.style__StyledComment-sc-1y8vww-5.dpVjwc.review-comment');
            
            // Iterate over each comment element
            commentElements.forEach(async (commentElement, index) => {
                // Get the content inside the 'review-comment__content' span or div
                var contentElement = commentElement.querySelector('.review-comment__content');
                var content = "";

                if (contentElement) {
                    // Check if there is a "Xem thêm" button
                    var showMoreButton = contentElement.querySelector('.show-more-content');
                    if (showMoreButton) {
                        // Simulate a click event on the "Xem thêm" button to reveal the full content
                        showMoreButton.click();
                        // Wait for a short delay for the content to expand
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    }
                    
                    // Get the content after potential expansion
                    content = contentElement.textContent.trim();
                    // Remove "Thu gọn" if it exists
                    content = content.replace(/Thu gọn$/, '').trim();
                }

                // Send the content to the server for sentiment analysis
                chrome.runtime.sendMessage({ par: content }, function (response) {
                    var result = response.farewell;
                    console.log(result);
                    if (result !== undefined) {
                        // Update sentiment counts based on the received value
                        if (result === 0) {
                            negativeCount++;
                        } else {
                            positiveCount++;
                        }
                    }
                    // Increment the processed count
                    processedCount++;
                    // Check if all comments are processed
                    if (processedCount === commentElements.length) {
                        // All comments are processed, print counts and determine overall sentiment
                        var overallSentimentUpdate = (positiveCount > negativeCount) ? "Positive" : "Negative";
                        console.log('total pos:', positiveCount, 'total neg:', negativeCount);
                        console.log(overallSentimentUpdate);
                        resolve(overallSentimentUpdate); // Resolve the promise with the overall sentiment
                    }
                });
            });
        });
    }
});
