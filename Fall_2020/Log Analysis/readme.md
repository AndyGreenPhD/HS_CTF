# Log Analysis questions

# All questions use ![this file](apache-access-logs-loganalysis), originally found at [https://gist.github.com/rm-hull/bd60aed44024e9986e3c](https://gist.github.com/rm-hull/bd60aed44024e9986e3c)

## Question 1 (Difficulty level 1)
**Initial Information:**  
What HTTP request was made on 13/Dec/2015:13:39:18?

**Hints:**  
None given

**Answer:**  
"GET /robots.txt HTTP/1.1"

## Question 2 (Difficulty level 2)
**Initial Information:**  
How many instances of status code 404 occurred?

 **Hints:**  
 None given

**Answer:**  
6  

grep -c '404' apache-access-logs

## Question 3 (Difficulty level 3)
**Initial Information:**  
How many instances of HEAD, POST, and GET HTTP requests are there? When entering your answer, be sure to separate the values with commas.

**Hints:**  
None given

**Answer:**
1, 431, 578  

Can be done via awk or via grep  

    awk '{print $6}' apache-access-logs | sort -n | uniq -c

a) awk '{print $6}' apache-access-logs  
For each record i.e line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables.  In Apache access logs, the type of request is listed 6th, meaning the six variable is used.  

b) sort -n  
sorts lines and gets all requests which are the same  

c) uniq -c  
Counts unique frequency

## Question 4 (Difficulty level 4)
**Initial Information:**  
What is the total size of the HTTP requests sent and received by IP address 188.191.175.166?

**Hint:**  
None given

**Answer:**  
52542  

    grep 188.191.175.166 apache-access-logs | awk '{sum+=$10} END {print sum}'

a) grep 188.191.175.166 apache-access-logs  
greps for IP in the apache-access-logs

b) awk '{sum+=$10} END {print sum}'  
Uses awk to add the output of the 10th variable in the output of the grep statement, which is the size of the object returned to client

## Question 5 (Difficulty level 5) (Cooper to rewrite using IP address with higher count)
**Initial Information:**  
Which IP address made the most requests to the Apache web server?

**Hint:**  
None given

**Answer:**  
191.182.199.16  

    awk '{print $1}' apache-access-logs | sort -n | uniq -c | sort -n

a) awk '{print $1}'  
For each record i.e line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables. In Apache access logs, the IP address is listed first, meaning the first variable is used.  

b)  sort -n  
This will sort the lines and get all the ip which are same.  

c) uniq -c  
This will get a count of unique frequencies of IP addresses.  

d) sort -n  
sorts by frequency.
