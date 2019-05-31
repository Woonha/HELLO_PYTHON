// Returns the first character of the string str
var firstCharacter = function(str) {
    return str.slice(0, 1);
};

// Returns the last character of a string str
var lastCharacter = function(str) {
    return str.slice(-1);
};

// Returns the string that results from removing the first
//  and last characters from str
var middleCharacters = function(str) {
    return str.slice(1, -1);
};

var isPalindrome = function(str) {
    if (str.length <= 1) {
        if (str.length === 0) {
            return false;
        }
        else {
            return true;
        }
    } else {
        if (firstCharacter(str) !== lastCharacter(str)) {
            return false;
        }
        else {
            return isPalindrome(middleCharacters(str));
        }
    }
};

var checkPalindrome = function(str) {
    println("Is this word a palindrome? " + str);
    println(isPalindrome(str));
};

checkPalindrome("a");
Program.assertEqual(isPalindrome("a"), true);
checkPalindrome("motor");
Program.assertEqual(isPalindrome("motor"), false);
checkPalindrome("rotor");
Program.assertEqual(isPalindrome("rotor"), true);
checkPalindrome("abcdedcba");
Program.assertEqual(isPalindrome("abcdedcba"), true);
checkPalindrome("array");
Program.assertEqual(isPalindrome("array"), false);

