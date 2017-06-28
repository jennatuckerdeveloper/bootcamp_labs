var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};


function findRarestValue(jsObj) {
    var freq = {};
    for (var i in namesToAges) {
        if (namesToAges[i] in freq) {
            freq[namesToAges[i]] += 1;
        } else {
            freq[namesToAges[i]] = 1
        }
    }
    var low = Object.values(freq);
    var answerVal = Math.min.apply(null, low);
    for (var key in freq) {
        if (freq[key] === answerVal) {
            return key
        }
            }

}

function findRarestExamples(jsObj) {
    var ages = [];
    var age = parseInt(findRarestValue(jsObj));
    for (var key in namesToAges) {
        if (namesToAges[key] === age) {
            ages.push(key)
        }
    }
    return ages
}


console.log(findRarestExamples(namesToAges));
