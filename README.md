# Constructi0nzone

This repository contains the challenge I made for the toulouse hacking convention 2025 and its writeup, this is the first challenge I make. Feel free to send me feedback on discord `daresse`  or on linkedin https://www.linkedin.com/in/thomas-hernandez-328571249/ :D

to run it on your machine just clone this repository 
 `git clone https://github.com/daresse/web-constructi0nzone-thcon2025 `
navigate to the root of the repository and run 
`flask run`

or build the docker : 
`docker-compose build --no-cache` 
and run it : 
`docker-compose up -d` 
### Challenge Information

| **Title**                | Constructi0nzone                                               |
| ------------------------ | ------------------------------------------------------- |
| **Category**             | Web                                            |
| **Description**          | ` We're looking  for informations about this gang... the XSS, Xtreme Scavenger Squad. We don't have much right now but take a look at their new website and try to get whatever you can, a list of their members could be great.`                                                                              |
| **Author**               | daresse                                             |
| **Difficulty (/10)**     | first flag : 3 // Second flag : 5                                                       |
| **Is Remote**            | Yes                                                      |
| **Has attachments**      | No                                                     |
| **Estimated solve time** | ~ 1h10     (1rst flag : 25min  // 2nd flag : 45mins )                                             |
| **Solve instructions**   | see write-up                                   |
| **Flag**                 | 1 : **`THC{N0t_S_ppos3d_To_b3_hEr3}`** <br>2 : **`THC{WTF_1S_V3rIFying_US3R_INP_T}`**                                |


### Write up

#### First flag : 
To solve the first flag, we need to analyze the provided website and identify the `get parameter in the URL` when consulting the members file.
we replace this with `0` to get access to the dev's file and get access to the url of the unfinished part of the site. Once we have the url, we have to change our user agent to "`XSS_SUPER_NAV`" (not case sensitive) to bypass the UA filter. For the IP filter, we need to add a parameter X-Forwarded-For with a valid url (starting with `192.168`, `192.168.0.3` works). **FIRST FLAG IS OBTAINED ON ACCESSING THIS PAGE.**

#### Second flag :
Once this is done we have access to the operation page where we can access the ongoing operations using the members ids but this gives you no information about the members list. We have to use a SQL injection to obtain the members name with a `Union attack` to access the users table. Problem is, there's an homemade filter built in the application that disallows spaces in the SQL query. To bypass this, we need to replace the space with `/**/` which will be interpreted as a space by the DBMS. The following payload should retrieve the flag : `'/**/Union/**/SELECT/**/username,1,1/**/from/**/users/**/--;`
### Attached files

None
