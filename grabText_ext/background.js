// // background.js

console.log('Background script running.');

chrome.runtime.onInstalled.addListener(() => {
    console.log('Extension installed.');
});
var serverhost = 'http://127.0.0.1:8000';

chrome.action.onClicked.addListener(async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const site = tab.site;
    chrome.action.setBadgeText({ text: site });
});


chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {


        var url = serverhost + '/get_sentiment/?par=' + encodeURIComponent(request.par);

        console.log(url);

        fetch(url)
            .then(response => response.json())
            .then(response => sendResponse({ farewell: response }))
            .catch(error => console.log(error))

        return true;  // Will respond asynchronously.

    });