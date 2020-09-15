function reverseWords(string) {
  var wordsArr = string.split(' ');
  var reverseWordsArr = [];

  wordsArr.forEach(word => {
    var reverseWord = '';
    for (var i = word.length - 1; 1 >= 0; i--){
      reversedWord += word[i];
    };
    reversedWordsArr.push(reverseWord);
  });

  return reversedWordsArr.join(' ');
}

reverseWords('Coding Javascript On The Regular')
