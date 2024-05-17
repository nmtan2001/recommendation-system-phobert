console.log('New code');

document.addEventListener('DOMContentLoaded', function () {
    var scrapeTexts = document.getElementById('scrapeTexts');
    var overallSentiment = document.getElementById('overallSentiment');
    
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const currentUrl = tabs[0].url;
        console.log('Current URL:', currentUrl);

        // Extract the common prefix
        const commonPrefix = currentUrl.split('/')[2];
        console.log('Common Prefix:', commonPrefix);
        
        // tiki
        if (commonPrefix === 'tiki.vn') {
            console.log('tiki');
            document.getElementById('current-common').textContent = commonPrefix;

            scrapeTexts.addEventListener('click', async () => {
                // Get current active tab
                let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

                // Define variables to track sentiment counts
                var positiveCount = 0;
                var negativeCount = 0;

                // Mark the start time
                const startTime = performance.now();
                
                // Function to fetch and process reviews for a specific page
                async function fetchAndProcessReviews(pageNumber) {
                    // Execute script to parse texts on page
                    const resultArray = await chrome.scripting.executeScript({
                        target: { tabId: tab.id },
                        func: scrapeTextFromPage,
                        args: [pageNumber, positiveCount, negativeCount] // Pass the page number and counts to the function
                    });
                    console.log('pos:', resultArray[0].result.positive, 'neg:', resultArray[0].result.negative);
                    // Update overall sentiment display
                    updateOverallSentiment(resultArray[0].result);
                }

                // Function to scrape text from page
                async function scrapeTextFromPage(pageNumber, positiveCount, negativeCount) {
                    // Define the selector for the pagination buttons
                    const paginationSelector = '.customer-reviews__pagination .btn';
                    const nextPageButton = document.querySelector(`${paginationSelector}.next`);

                    // Select all comment elements
                    var commentElements = document.querySelectorAll('.style__StyledComment-sc-1y8vww-5.dpVjwc.review-comment');

                    // Process each comment
                    for (let i = 0; i < commentElements.length; i++) {
                        const commentElement = commentElements[i];
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
                            if (content == "") {
                                console.log('skipped');
                                continue;
                            }
                            // Remove "Thu gọn" if it exists
                            content = content.replace(/Thu gọn$/, '').trim();

                            // Send the content to the server for sentiment analysis
                            await new Promise(resolve => {
                                chrome.runtime.sendMessage({ par: content }, function (response) {
                                    var sentimentResult = response.farewell;
                                    console.log('Received sentiment result:', sentimentResult, 'Phrase:', content);
                                    // Update sentiment counts based on the received value
                                    if (sentimentResult === 0) {
                                        negativeCount++;
                                    } else if (sentimentResult === 1) {
                                        positiveCount++;
                                    }
                                    resolve(sentimentResult);
                                });
                            });
                        }
                    }

                    console.log('total pos:', positiveCount, 'total neg:', negativeCount, 'page', pageNumber);

                    // Click the next page button if it exists
                    if (nextPageButton) {
                        nextPageButton.click();
                        // Wait for a short delay for the page content to load
                        await new Promise(resolve => setTimeout(resolve, 2000));
                        // Recursively call scrapeTextFromPage for the next page and return its promise
                        return scrapeTextFromPage(pageNumber + 1, positiveCount, negativeCount);
                    } else {
                        // If there is no next page, return a promise that resolves with the final counts
                        return { positive: positiveCount, negative: negativeCount };
                    }
                }

                // Function to update overall sentiment display
                function updateOverallSentiment(result) {
                    // Determine the overall sentiment
                    var overallSentimentUpdate = (result.positive > result.negative) ? "Positive" : "Negative";
                    console.log('Total Positive:', result.positive, 'Total Negative:', result.negative);
                    console.log('Overall Sentiment:', overallSentimentUpdate);
                    overallSentiment.textContent = overallSentimentUpdate;
                    positiveNum.textContent = result.positive;
                    negativeNum.textContent = result.negative;

                    // Mark the end time
                    const endTime = performance.now();
                    const duration = endTime - startTime;
                    console.log(`Script execution time: ${duration} milliseconds`);
                }

                // Start fetching and processing reviews from the first page
                fetchAndProcessReviews(1);
            });
        } else {
            document.getElementById('current-common').textContent = 'Currently not supported';
        }
    });
});
