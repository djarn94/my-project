# my-project

<summary>Solution components :</summary>
 *1.To setup the CD I followed the following guide : https://devpress.csdn.net/cicd/62ec237989d9027116a10405.html the steps were perfectly described.
 *2.to make sure the deploy is only being done when the test is complete I used the following code :
'''
        on: 
          workflow_run:
            workflows: ["Run Tests"]
            types:
             - completed
'''
inside my deploy.yml file.<
