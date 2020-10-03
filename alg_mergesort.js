// function mergeSort (arr) {
//     if (arr.length < 2) return arr;
//     var middleIndex = Math.floor(arr.length / 2);
//     var firstHalf = arr.slice(0, middleIndex);
//     var secondHalf = arr.slice(middleIndex);
//
//     return merge(mergeSort(firstHalf), mergeSort(secondHalf));
// }
//
// function merge (array1, array2) {
//     var result = [];
//     while (array1.length && array2.length) {
//       var minElem;
//       if (array1[0] < array2[0]) minElem = array1.shift();
//       else minElem = array2.shift();
//       result.push(minElem);
//     }
//
//     if (array1.length) result = result.concat(array1);
//     else result = result.concat(array2);
//     return result;
// }
//
// console.log(mergeSort([6000, 34, 203, 3, 746, 200, 984, 198, 764, 1, 9, 1]))

function mergeSort(arr) {
 if (arr.length === 1) return arr;

 const middleIndex = Math.floor(arr.length / 2);
 const firstHalf = arr.slice(0, middleIndex);
 const secondHalf = arr.slice(middleIndex);

 return merge(mergeSort(firstHalf), mergeSort(secondHalf));
}

function merge(arr1, arr2) {
 const results = [];
 let secondIndex = 0;
 let firstIndex = 0;

 while(firstIndex < arr1.length) {
   const firstNumber = arr1[firstIndex];
   const secondNumber = arr2[secondIndex];

   if (firstNumber > secondNumber) {
     results.push(secondNumber);
     secondIndex++;
   } else {
     results.push(firstNumber);
     firstIndex++;
   }
 }

 return results.concat(arr2.slice(secondIndex));
}


console.log(mergeSort([5, 2, 6, 3, 4, 7, 7]));
