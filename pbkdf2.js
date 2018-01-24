var CryptoJS = require("crypto-js");
var password = 'Secret Passphrase';
console.log('Password: '+password);

var salt = CryptoJS.lib.WordArray.random(128/8);
var key128Bits = CryptoJS.PBKDF2(password, salt, { keySize: 128/32 });
var key256Bits = CryptoJS.PBKDF2(password, salt, { keySize: 256/32 });
var key512Bits = CryptoJS.PBKDF2(password, salt, { keySize: 512/32 });
var key128Bits1000Iterations = CryptoJS.PBKDF2(password, salt, { keySize: 128/32, iterations: 1000 });
var key256Bits1000Iterations = CryptoJS.PBKDF2(password, salt, { keySize: 256/32, iterations: 1000 });
var key512Bits1000Iterations = CryptoJS.PBKDF2(password, salt, { keySize: 512/32, iterations: 1000 });

console.log('key(128bits): '+key128Bits);
console.log('key(256bits): '+key256Bits);
console.log('key(512bits): '+key512Bits);
console.log('key(128bits,1000it): '+key128Bits1000Iterations);
console.log('key(256bits,1000it): '+key256Bits1000Iterations);
console.log('key(512bits,1000it): '+key512Bits1000Iterations);
console.log();
