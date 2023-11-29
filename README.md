# my-project

<summary>Solution components :</summary>
 1. To setup the CD I followed the following guide : https://devpress.csdn.net/cicd/62ec237989d9027116a10405.html the steps were perfectly described.
 
 2. To make sure the deploy is only being done when the test is complete I used the following code inside the deploy.yml file :

        on: 
            workflow_run:
             workflows: ["Run Tests"]
              types:
               - completed
</code>

3. Search the web for a example requirement.txt file copied it, run tests launched and failed. alot of python modules but pytest was missing, added it to the txt file.
</details>


<summary>encountered problems :</summary>
1. When following the guide to setup the CD it all went smooth except the part that the deploy would fail on finding the private key (which happend after problem 3). searched the web and found the solution beside the private key also the comments needed to be added.

-----BEGIN OPENSSH PRIVATE KEY-----

-----END OPENSSH PRIVATE KEY-----

2. Was a bit lost with the requirement.txt file and how to get this one so I searched the web for examples. (see solution 3)

3. When adding the secrets for my solution I had no idea where to add them since there are multiply spots to add them at setting on your repository and the guide I used was a bit outdated. So at first I tought I was just doing it wrong but encountered a fresh guide for this part on youtube.

</details>
