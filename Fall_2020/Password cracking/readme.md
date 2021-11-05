# Password cracking questions

## Question  1 (Difficulty level 1)  
**Initial information:**  
A network engineer working for Hooplah Corporation has captured some unusual network traffic on Vlan 3. While inspecting the .pcap file, a string of text was discovered. Try to decode the message!  

**SSBhbSBhIGg0eDByLCBmZWFyIG0z**

**Hint:**  
Decryption does not equal decoding!

**Answer:**  
I am a h4x0r, fear m3  

Base64 encoded. Can be decoded at ![https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

## Question 2 (Difficulty level 2)
**Initial information:**  
A super-secret group of hacktivists have tried to authenticate to a FBI honeypot. The following hashed password was captured. Try to decrypt it!  

**482C811DA5D5B4BC6D497FFA98491E38**

**Hint:**  
None given

**Answer:**  
password123  

MD5 Hash crackable at ![https://crackstation.net](https://crackstation.net)

## Question 3 (Difficulty level 3)
**Initial information:**  
Security engineers have used an exploit to capture hashed Microsoft Windows credentials. The problem is we can’t read them, find a way to crack it!

**878D8014606CDA29677A44EFA1353FC7**

**Hint:**  
None given

**Answer:**  
secret  

NTLM hash crackable via ![https://crackstation.net](https://crackstation.net)

## Question 4 (Difficulty level 4)
**Initial information:**  
We've been passed another code by one of our people in the field. It's an old code, but it checks out.  

**Ilv ecs oefne**

**Hint:**  
None given

**Answer:**  
I love fences  

Railfence cipher

## Question 5 (Difficulty level 5)
**Initial information:**  
Security analysts have obtained a password hash that cannot be read unless it is cracked. Thankfully, this appears to be a hash that can be cracked with the help of the “rockyou” password file.  If you don’t already have this file, you can download it from ![https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)  

**C69b755b65e3d5a3546edb23bbd186d9**

**Hint:**  
None given

**Answer:**  
renzo121  

Can be cracked using hashcat with the default rockyou.txt wordlist
