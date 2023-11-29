# my-project

<details>
<summary>Solution components :</summary>
 1. To setup the CD I followed the following guide : https://devpress.csdn.net/cicd/62ec237989d9027116a10405.html the steps were perfectly described.
 
 2. To make sure the deploy is only being done when the test succeeded I added the following code to run-tests.yml :

         if: success()
    
           - uses: actions/checkout@v1
           - name: Copy repository contents via scp
             uses: appleboy/scp-action@master
             with:
    
               host: ${{ secrets.HOST }}
               username: ${{ secrets.USERNAME }}
               port: ${{ secrets.PORT }}
               key: ${{ secrets.SSHKEY }}
               source: "."
               target: "/var/www/html"
           - name: Executing remote command
             uses: appleboy/ssh-action@master
             with:
               host: ${{ secrets.HOST }}
               USERNAME: ${{ secrets.USERNAME }}
               PORT: ${{ secrets.PORT }}
               KEY: ${{ secrets.SSHKEY }}
               script: ls
</code>

4. Search the web for a example requirement.txt file copied it, run tests launched and failed. alot of python modules but pytest was missing, added it to the txt file.
</details>

<details>
<summary>encountered problems :</summary>
1. When following the guide to setup the CD it all went smooth except the part that the deploy would fail on finding the private key (which happend after problem 3). searched the web and found the solution beside the private key also the comments needed to be added.

-----BEGIN OPENSSH PRIVATE KEY-----

-----END OPENSSH PRIVATE KEY-----

2. Was a bit lost with the requirement.txt file and how to get this one so I searched the web for examples. (see solution 3)

3. When adding the secrets for my solution I had no idea where to add them since there are multiply spots to add them at setting on your repository and the guide I used was a bit outdated. So at first I tought I was just doing it wrong but encountered a fresh guide for this part on youtube.
</details>

<details>
<summary>extra: </summary>
When doing this assignment/module 8(deploying your projects) I got lost many times, but after reading the same thing over and over and redoing certain steps again it all seems to get working. But everything in this last module is something I have alot to learn about and how everything works exactly it's almost like learning how to drive. You only really learn it by doing it alot after you got your license.

</details>
