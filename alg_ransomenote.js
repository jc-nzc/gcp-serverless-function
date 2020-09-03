// Time Complexity and Big O Notation

// Constant RunTime O(1) will only execute the same number of operations regardless of inputs

// Linear RunTime O(n) operations increase proportionally to the input ; o for function, n for size of the input

// Exponential RunTime O(n^2) evaluate all possibilities; for every added input, it takes an exponential jump; inefficient, slow, avoid

// Logrithmic RunTime O(n²) Ex. Binary Search, Sorted, 2 inputs, reduces throughout the search by cutting the input in half




function harmlessRansomNote(noteText, magazineText){
  var noteArr = noteText.split(' ');
  var magazineArr = magazineText.split(' ');
  var magazineObj = {};

  magazineArr.forEach(word => {
    if(!magazineObj[word]) magazineObj[word] = 0;
    magazineObj[word]++;
  });

  var noteIsPossible = true;
  noteArr.forEach(word => {
    if (magazineObj[word]) {
      magazineObj[word]--;
      if (magazineObj[word] < 0) noteIsPossible = false;
    }
    else noteIsPossible = false;
  });

  return noteIsPossible;
}

harmlessRansomNote('this is a secret note for you from a secret admirer', 'puerto rico is a place of great wonder and excitement it has many secret waterfall locations that i am an admirer of you must hike quite a distance to find the secret places as they are far from populated areas but it is worth the effort a tip i have for you is to go early in the morning when it is not so hot out also note that you must wear hiking boots this is one of the best places i have ever visited');
