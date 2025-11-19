---
title: Rijndael / AES (128 bit) in VB.net, PHP, Python
date: 2012-11-21T20:00:23-06:00
excerpt: Being able to transport encrypted data is important in some of my projects at work. One-way hashes using MD5 usually suffice for most encryption purposes but Symmetric Encryption algorithms are important for encrypting and then decrypting data. For this, we use the Rijndael and AES algorithm in a few different languages.
layout: post
permalink: 2012/11/rijndael-encryption-and-decryption-vb-net-php-python/
tags:
  - AES
  - Encryption
  - PHP
  - Python
  - Rijndael
  - VB.net
---
Being able to transport encrypted data is important in some of my projects at work. One-way hashes using MD5 usually suffice for most encryption purposes but Symmetric Encryption algorithms are important for encrypting and then decrypting data. For this, we use the Rijndael and AES algorithm in a few different languages. Here is what we do for VB.net, PHP, and Python. I also take no responsibility for misuse of this code.

Note: You will see a string replace which is necessary for passing encrypted data through a URL.

**VB.net:**
{% highlight vb %}
' Keys required for Symmetric encryption / decryption
Dim rijnKey As Byte() = {&H1, &H2, &H3, &H4, &H5, &H6, &H7, &H8, &H9, &H10, &H11, &H12, &H13, &H14, &H15, &H16}
Dim rijnIV As Byte() = {&H1, &H2, &H3, &H4, &H5, &H6, &H7, &H8, &H9, &H10, &H11, &H12, &H13, &H14, &H15, &H16}

Function Decrypt(S As String)
  If S = "" Then
    Return S
  End If

  ' Turn the cipherText into a ByteArray from Base64
  Dim cipherText As Byte()

  Try
    ' Replace any + that will lead to the error
    cipherText = Convert.FromBase64String(S.Replace("BIN00101011BIN", "+"))
  Catch ex As Exception
    ' There is a problem with the string, perhaps it has bad base64 padding
    Return S
  End Try

  'Creates the default implementation, which is RijndaelManaged.
  Dim rijn As SymmetricAlgorithm = SymmetricAlgorithm.Create()
  Try
    ' Create the streams used for decryption.
    Using msDecrypt As New MemoryStream(cipherText)
      Using csDecrypt As New CryptoStream(msDecrypt, rijn.CreateDecryptor(rijnKey, rijnIV), CryptoStreamMode.Read)
        Using srDecrypt As New StreamReader(csDecrypt)
        ' Read the decrypted bytes from the decrypting stream and place them in a string.
        S = srDecrypt.ReadToEnd()
        End Using
      End Using
    End Using
  Catch E As CryptographicException
    Return S
  End Try

  Return S
End Function

Function Encrypt(S As String)
  'Creates the default implementation, which is RijndaelManaged.
  Dim rijn As SymmetricAlgorithm = SymmetricAlgorithm.Create()
  Dim encrypted() As Byte
  Using msEncrypt As New MemoryStream()
    Dim csEncrypt As New CryptoStream(msEncrypt, rijn.CreateEncryptor(rijnKey, rijnIV), CryptoStreamMode.Write)
    Using swEncrypt As New StreamWriter(csEncrypt)
      'Write all data to the stream.
      swEncrypt.Write(S)
    End Using
    encrypted = msEncrypt.toArray()
  End Using

  ' You cannot convert the byte to a string or you will get strange characters so base64 encode the string
  ' Replace any + that will lead to the error
  Return Convert.ToBase64String(encrypted).Replace("+", "BIN00101011BIN")
End Function
{% endhighlight %}

**PHP:**
{% highlight php %}
$rijnKey = "\x1\x2\x3\x4\x5\x6\x7\x8\x9\x10\x11\x12\x13\x14\x15\x16";
$rijnIV = "\x1\x2\x3\x4\x5\x6\x7\x8\x9\x10\x11\x12\x13\x14\x15\x16";

function Decrypt($s){
  global $rijnKey, $rijnIV;`

  if ($s == "") { return $s; }

  // Turn the cipherText into a ByteArray from Base64
  try {
    $s = str_replace("BIN00101011BIN", "+", $s);
    $s = base64_decode($s);
    $s = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, $rijnKey, $s, MCRYPT_MODE_CBC, $rijnIV);

  } catch(Exception $e) {
    // There is a problem with the string, perhaps it has bad base64 padding
    // Do Nothing
  }

  return $s;
}

function Encrypt($s){
  global $rijnKey, $rijnIV;

  // Have to pad if it is too small
  $block = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, 'cbc');
  $pad = $block - (strlen($s) % $block);
  $s .= str_repeat(chr($pad), $pad);

  $s = mcrypt_encrypt(MCRYPT_RIJNDAEL_128, $rijnKey, $s, MCRYPT_MODE_CBC, $rijnIV);
  $s = base64_encode($s);
  $s = str_replace("+", "BIN00101011BIN", $s);

  return $s;
}
{% endhighlight %}

**Python 2.7**

_You must first install the pyCrypto package which gives you access to AES functions. If you are using Windows, you can go to <http://www.voidspace.org.uk/python/modules.shtml#index> to download the pyCrypto binary._

{% highlight python %}

from Crypto.Cipher import AES
import base64
import os

key = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15\x16"
iv = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15\x16"
text = "10"
replace_plus = "BIN00101011BIN"

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 16

def repeat_to_length(string_to_expand, length):
return (string_to_expand * ((length/len(string_to_expand))+1))[:length]

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) \
* chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s : s[0:-ord(s[-1])]

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
def EncodeAES(s):
  c = AES.new(key, AES.MODE_CBC, iv)
  s = pad(s)
  s = c.encrypt(s)
  s = base64.b64encode(s)
  return s.replace("+", replace_plus)

def DecodeAES(enc):
  c = AES.new(key, AES.MODE_CBC, iv)
  enc = enc.replace(replace_plus, "+")
  enc = base64.b64decode(enc)
  enc = c.decrypt(enc)
  return unpad(enc)

# encode a string
encoded = EncodeAES(text)
print 'Encrypted string:', encoded

# decode the encoded string
decoded = DecodeAES(encoded)
print 'Decrypted string:', decoded
{% endhighlight %}