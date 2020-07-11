const Language = require('@google-cloud/language');
// Instantiates a client
const language = new Language.LanguageServiceClient();
// Post Message, Score, Magnitude to Keen
const KeenTracking = require('keen-tracking');
// Create your Client Credentials which can be found inside of your 'Access' tab
const client = new KeenTracking({
  projectId: 'Replace with your project id',
  writeKey: 'Replace with your write key'
});
exports.anthemcNLP =  (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
    /* this handles CORS preflight check */
    if (req.method === 'OPTIONS') {
      // Send response to OPTIONS requests
      res.set('Access-Control-Allow-Methods', 'GET');
      res.set('Access-Control-Allow-Headers', 'Content-Type');
      res.set('Access-Control-Max-Age', '3600');
      res.status(204).send('');
      return;
    }
    // this handles cors for the regular request
    res.set('Access-Control-Allow-Origin', '*');
    if (req.body.review_text == undefined) {
      res.status(400).send("No review text provided");
      return;
    }
    // Ingest the review_text and assign to the constant 'document' 
    const document = {
      content: req.body.review_text,
      type: 'PLAIN_TEXT',
    };
    // Google's NLP Language API request is analyzing the text and assigning Sentiment, Magnitude
    language
        .analyzeSentiment({
            document: document
        })
        .then(results => {
            const sentiment = results[0].documentSentiment;
            console.log(`Document sentiment:`);
            console.log(`  Score: ${sentiment.score}`);
            console.log(`  Magnitude: ${sentiment.magnitude}`);
            res.setHeader('Content-Type', 'application/json');
            var resultObj = {};
            resultObj.score = sentiment.score;
            resultObj.magnitude = sentiment.magnitude;
            // Record the event with sentiment and magnitude score to Keen 
            client
              .recordEvent('FormResult', {
                text: req.body.review_text,
                score: sentiment.score,
                magnitude: sentiment.magnitude
              })
              .then(results => {
                  res.setHeader('Content-Type', 'application/json');
                res.end(JSON.stringify({ message: "ok" }));
                return;
              })
              .catch(err => {
                  res.status(500).send(`Error in invoking Keen API: ${err}`);
                  return;
              });
        })
        .catch(err => {
            res.status(500).send(`Error in invoking NLP API: ${err}`);
            return;
        });
}
